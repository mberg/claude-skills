#!/usr/bin/env python3
"""
WhatsApp Flows Validator - Validates Flow JSON structure and constraints
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
from colorama import Fore, Style, init

init(autoreset=True)


class FlowValidator:
    """Validates WhatsApp Flow JSON files"""

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.screen_ids: Set[str] = set()
        self.field_names_by_screen: Dict[str, Set[str]] = {}

    def validate(self, flow_data: Dict) -> bool:
        """Main validation method - returns True if valid, False if errors"""
        self.errors = []
        self.warnings = []
        self.screen_ids = set()

        # Check required top-level properties
        if "version" not in flow_data:
            self.errors.append("Missing required property: version")
            return False

        if "screens" not in flow_data:
            self.errors.append("Missing required property: screens")
            return False

        version = flow_data.get("version")
        if not isinstance(version, str):
            self.errors.append(f"version must be string, got {type(version)}")
            return False

        screens = flow_data.get("screens", [])
        if not isinstance(screens, list) or len(screens) == 0:
            self.errors.append("screens must be non-empty array")
            return False

        # Validate screens
        self._validate_screens(screens)

        # Check routing model if present
        if "routing_model" in flow_data:
            self._validate_routing_model(flow_data.get("routing_model"), screens)

        # Check data_api_version if routing_model present
        if "routing_model" in flow_data and "data_api_version" not in flow_data:
            self.warnings.append("routing_model present but data_api_version missing")

        return len(self.errors) == 0

    def _validate_screens(self, screens: List[Dict]) -> None:
        """Validate all screens in flow"""
        for i, screen in enumerate(screens):
            if not isinstance(screen, dict):
                self.errors.append(f"Screen {i} is not an object")
                continue

            screen_id = screen.get("id")
            if not screen_id:
                self.errors.append(f"Screen {i} missing required property: id")
                continue

            if not isinstance(screen_id, str):
                self.errors.append(f"Screen {i}: id must be string")
                continue

            if screen_id == "SUCCESS":
                # SUCCESS is reserved but allowed
                pass

            if screen_id in self.screen_ids:
                self.errors.append(f"Duplicate screen ID: {screen_id}")
            else:
                self.screen_ids.add(screen_id)

            self._validate_screen_content(screen)

    def _validate_screen_content(self, screen: Dict) -> None:
        """Validate individual screen structure"""
        screen_id = screen.get("id", "unknown")

        # Validate layout
        if "layout" not in screen:
            self.errors.append(f"Screen '{screen_id}' missing required property: layout")
            return

        layout = screen.get("layout")
        if not isinstance(layout, dict):
            self.errors.append(f"Screen '{screen_id}': layout must be object")
            return

        if layout.get("type") != "SingleColumnLayout":
            self.errors.append(
                f"Screen '{screen_id}': only SingleColumnLayout supported"
            )
            return

        # Validate children components
        children = layout.get("children", [])
        if not isinstance(children, list):
            self.errors.append(f"Screen '{screen_id}': children must be array")
            return

        if len(children) > 50:
            self.errors.append(
                f"Screen '{screen_id}': maximum 50 components per screen, got {len(children)}"
            )

        # Track field names for uniqueness
        self.field_names_by_screen[screen_id] = set()

        # Validate each component
        for component in children:
            self._validate_component(component, screen_id)

        # Check terminal screen rules
        if screen.get("terminal"):
            self._validate_terminal_screen(screen)

        # Validate data schema if present
        if "data" in screen:
            self._validate_data_schema(screen.get("data"), screen_id)

        # Validate sensitive array
        if "sensitive" in screen:
            sensitive = screen.get("sensitive", [])
            if not isinstance(sensitive, list):
                self.errors.append(f"Screen '{screen_id}': sensitive must be array")
            else:
                # Check sensitive fields exist
                for field in sensitive:
                    if field not in self.field_names_by_screen[screen_id]:
                        self.warnings.append(
                            f"Screen '{screen_id}': sensitive field '{field}' not found in form"
                        )

    def _validate_component(self, component: Dict, screen_id: str) -> None:
        """Validate individual component"""
        if not isinstance(component, dict):
            self.errors.append(f"Screen '{screen_id}': component is not an object")
            return

        comp_type = component.get("type")
        if not comp_type:
            self.errors.append(f"Screen '{screen_id}': component missing type")
            return

        # Track field names
        if "name" in component:
            field_name = component.get("name")
            if field_name in self.field_names_by_screen[screen_id]:
                self.errors.append(
                    f"Screen '{screen_id}': duplicate field name '{field_name}'"
                )
            else:
                self.field_names_by_screen[screen_id].add(field_name)

        # Component-specific validation
        if comp_type == "TextHeading":
            text = component.get("text", "")
            if len(text) > 80:
                self.errors.append(
                    f"Screen '{screen_id}' TextHeading: text exceeds 80 characters"
                )

        elif comp_type == "TextBody":
            text = component.get("text", "")
            if len(text) > 4096:
                self.errors.append(
                    f"Screen '{screen_id}' TextBody: text exceeds 4096 characters"
                )

        elif comp_type == "TextCaption":
            text = component.get("text", "")
            if len(text) > 409:
                self.errors.append(
                    f"Screen '{screen_id}' TextCaption: text exceeds 409 characters"
                )

        elif comp_type == "TextInput":
            if "name" not in component:
                self.errors.append(f"Screen '{screen_id}' TextInput: missing name")
            max_length = component.get("max-length", 80)
            if not isinstance(max_length, int) or max_length < 1:
                self.errors.append(
                    f"Screen '{screen_id}' TextInput: invalid max-length"
                )

        elif comp_type == "TextArea":
            if "name" not in component:
                self.errors.append(f"Screen '{screen_id}' TextArea: missing name")

        elif comp_type == "Footer":
            label = component.get("label", "")
            if len(label) > 30:
                self.errors.append(
                    f"Screen '{screen_id}' Footer: label exceeds 30 characters"
                )

        elif comp_type == "EmbeddedLink":
            text = component.get("text", "")
            if len(text) > 25:
                self.errors.append(
                    f"Screen '{screen_id}' EmbeddedLink: text exceeds 25 characters"
                )

        elif comp_type == "OptIn":
            label = component.get("label", "")
            if len(label) > 80:
                self.errors.append(
                    f"Screen '{screen_id}' OptIn: label exceeds 80 characters"
                )
            description = component.get("description", "")
            if len(description) > 200:
                self.errors.append(
                    f"Screen '{screen_id}' OptIn: description exceeds 200 characters"
                )

        elif comp_type == "Image":
            src = component.get("src")
            if src and not src.startswith("https://"):
                self.errors.append(
                    f"Screen '{screen_id}' Image: URL must be HTTPS, got {src}"
                )

        elif comp_type in ["CheckboxGroup", "RadioButtonsGroup", "Dropdown"]:
            if "name" not in component:
                self.errors.append(f"Screen '{screen_id}' {comp_type}: missing name")
            data_source = component.get("data-source", {})
            if isinstance(data_source, dict):
                values = data_source.get("values", [])
                if isinstance(values, list):
                    if len(values) == 0:
                        self.errors.append(
                            f"Screen '{screen_id}' {comp_type}: no options provided"
                        )
                    if comp_type == "Dropdown" and len(values) > 200:
                        self.errors.append(
                            f"Screen '{screen_id}' Dropdown: exceeds 200 options"
                        )

        elif comp_type == "If":
            if "condition" not in component:
                self.errors.append(f"Screen '{screen_id}' If: missing condition")
            if "then" not in component:
                self.errors.append(f"Screen '{screen_id}' If: missing then branch")

        elif comp_type == "Switch":
            if "value" not in component:
                self.errors.append(f"Screen '{screen_id}' Switch: missing value")
            if "cases" not in component:
                self.errors.append(f"Screen '{screen_id}' Switch: missing cases")

    def _validate_terminal_screen(self, screen: Dict) -> None:
        """Validate terminal screen requirements"""
        screen_id = screen.get("id")
        children = screen.get("layout", {}).get("children", [])

        # Must have Footer component
        has_footer = any(c.get("type") == "Footer" for c in children if isinstance(c, dict))
        if not has_footer:
            self.errors.append(
                f"Terminal screen '{screen_id}' must have Footer component"
            )

    def _validate_data_schema(self, data_schema: Dict, screen_id: str) -> None:
        """Validate screen data schema has __example__ for all fields"""
        if not isinstance(data_schema, dict):
            return

        properties = data_schema.get("properties", {})
        if not isinstance(properties, dict):
            return

        for field_name, field_def in properties.items():
            if not isinstance(field_def, dict):
                continue

            if "__example__" not in field_def:
                self.warnings.append(
                    f"Screen '{screen_id}' data field '{field_name}': missing __example__"
                )

    def _validate_routing_model(
        self, routing_model: Dict, screens: List[Dict]
    ) -> None:
        """Validate routing model consistency"""
        if not isinstance(routing_model, dict):
            self.errors.append("routing_model must be object")
            return

        # Get all screen IDs from screens array
        valid_screens = {s.get("id") for s in screens if isinstance(s, dict)}

        # Check all routing references exist
        for source_screen, destinations in routing_model.items():
            if source_screen not in valid_screens:
                self.errors.append(
                    f"routing_model: source screen '{source_screen}' not found"
                )

            if not isinstance(destinations, list):
                self.errors.append(
                    f"routing_model '{source_screen}': destinations must be array"
                )
                continue

            if len(destinations) > 10:
                self.errors.append(
                    f"routing_model '{source_screen}': exceeds 10 maximum destinations"
                )

            for dest_screen in destinations:
                if dest_screen not in valid_screens:
                    self.errors.append(
                        f"routing_model: destination screen '{dest_screen}' not found"
                    )

    def print_results(self) -> None:
        """Print validation results to console"""
        if self.errors:
            print(f"\n{Fore.RED}❌ Validation Failed{Style.RESET_ALL}\n")
            print(f"{Fore.RED}Errors ({len(self.errors)}):{Style.RESET_ALL}")
            for error in self.errors:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n{Fore.YELLOW}⚠ Warnings ({len(self.warnings)}):{Style.RESET_ALL}")
            for warning in self.warnings:
                print(f"  • {warning}")

        if not self.errors and not self.warnings:
            print(f"\n{Fore.GREEN}✅ Flow is valid!{Style.RESET_ALL}\n")
        elif not self.errors:
            print(f"\n{Fore.GREEN}✅ Flow is valid (with warnings){Style.RESET_ALL}\n")


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python validate_flow.py <flow.json>")
        sys.exit(1)

    flow_path = Path(sys.argv[1])

    if not flow_path.exists():
        print(f"{Fore.RED}Error: File not found: {flow_path}{Style.RESET_ALL}")
        sys.exit(1)

    try:
        with open(flow_path, "r") as f:
            flow_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{Fore.RED}Error: Invalid JSON - {e}{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    validator = FlowValidator()
    is_valid = validator.validate(flow_data)
    validator.print_results()

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
