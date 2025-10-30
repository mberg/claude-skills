#!/usr/bin/env python3
"""
Component-specific validator for WhatsApp Flows
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set
from colorama import Fore, Style, init

init(autoreset=True)


class ComponentValidator:
    """Validates individual components and their constraints"""

    # Component definitions with their constraints
    COMPONENTS = {
        "TextHeading": {
            "max_text": 80,
            "requires": ["text"],
        },
        "TextSubheading": {
            "max_text": 80,
            "requires": ["text"],
        },
        "TextBody": {
            "max_text": 4096,
            "requires": ["text"],
        },
        "TextCaption": {
            "max_text": 409,
            "requires": ["text"],
        },
        "RichText": {
            "max_text": 4096,
            "requires": ["text"],
            "markdown": True,
            "version": "5.1+",
        },
        "TextInput": {
            "requires": ["name"],
            "max_length_default": 80,
            "input_types": ["text", "number", "email", "password", "passcode", "phone", "date"],
        },
        "TextArea": {
            "requires": ["name"],
            "max_length_default": 600,
        },
        "CheckboxGroup": {
            "requires": ["name", "data-source"],
            "min_options": 1,
            "max_options": 20,
        },
        "RadioButtonsGroup": {
            "requires": ["name", "data-source"],
            "min_options": 1,
            "max_options": 20,
        },
        "Dropdown": {
            "requires": ["name", "data-source"],
            "max_options_static": 200,
            "max_options_dynamic": 100,
        },
        "OptIn": {
            "requires": ["name", "label"],
            "max_label": 80,
            "max_description": 200,
        },
        "DatePicker": {
            "requires": ["name"],
            "version": "5.0+",
        },
        "CalendarPicker": {
            "requires": ["name"],
            "version": "6.1+",
            "modes": ["single", "range"],
        },
        "PhotoPicker": {
            "requires": ["name"],
            "version": "5.0+",
        },
        "DocumentPicker": {
            "requires": ["name"],
            "version": "5.0+",
        },
        "Image": {
            "requires": ["src"],
            "scale_types": ["center-crop", "fill"],
        },
        "ImageCarousel": {
            "requires": ["images"],
            "version": "7.1+",
            "max_images": 3,
        },
        "NavigationList": {
            "requires": ["name", "data-source"],
            "max_items": 20,
            "version": "6.2+",
        },
        "ChipsSelector": {
            "requires": ["name", "data-source"],
            "min_options": 2,
            "max_options": 20,
            "version": "6.3+",
        },
        "EmbeddedLink": {
            "requires": ["text"],
            "max_text": 25,
        },
        "Footer": {
            "requires": ["label"],
            "max_label": 30,
        },
        "If": {
            "requires": ["condition", "then"],
            "version": "4.0+",
        },
        "Switch": {
            "requires": ["value", "cases"],
            "version": "4.0+",
        },
    }

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_component(self, component: Dict, screen_id: str, index: int) -> bool:
        """Validate a single component"""
        self.errors = []
        self.warnings = []

        comp_type = component.get("type")
        if not comp_type:
            self.errors.append(f"Screen '{screen_id}' component {index}: missing type")
            return False

        if comp_type not in self.COMPONENTS:
            self.errors.append(
                f"Screen '{screen_id}' component {index}: unknown type '{comp_type}'"
            )
            return False

        spec = self.COMPONENTS[comp_type]

        # Check required properties
        for required in spec.get("requires", []):
            if required not in component:
                self.errors.append(
                    f"Screen '{screen_id}' {comp_type} {index}: missing required '{required}'"
                )

        # Check text limits
        if "max_text" in spec:
            text = component.get("text", "")
            max_chars = spec["max_text"]
            if len(text) > max_chars:
                self.errors.append(
                    f"Screen '{screen_id}' {comp_type}: text exceeds {max_chars} chars ({len(text)})"
                )

        # Check label limits
        if "max_label" in spec:
            label = component.get("label", "")
            max_chars = spec["max_label"]
            if len(label) > max_chars:
                self.errors.append(
                    f"Screen '{screen_id}' {comp_type}: label exceeds {max_chars} chars"
                )

        # Check description limits
        if "max_description" in spec:
            desc = component.get("description", "")
            max_chars = spec["max_description"]
            if len(desc) > max_chars:
                self.errors.append(
                    f"Screen '{screen_id}' {comp_type}: description exceeds {max_chars} chars"
                )

        # Check input type
        if comp_type == "TextInput":
            input_type = component.get("input-type", "text")
            if input_type not in spec.get("input_types", []):
                self.errors.append(
                    f"Screen '{screen_id}' TextInput: invalid input-type '{input_type}'"
                )

        # Check data-source options
        if "data-source" in component:
            data_source = component.get("data-source", {})
            if isinstance(data_source, dict):
                ds_type = data_source.get("type")
                values = data_source.get("values", [])

                if isinstance(values, list):
                    opt_count = len(values)

                    if "min_options" in spec and opt_count < spec["min_options"]:
                        self.errors.append(
                            f"Screen '{screen_id}' {comp_type}: below minimum {spec['min_options']} options"
                        )

                    if "max_options" in spec and opt_count > spec["max_options"]:
                        self.errors.append(
                            f"Screen '{screen_id}' {comp_type}: exceeds {spec['max_options']} options"
                        )

                    if comp_type == "Dropdown":
                        max_static = spec.get("max_options_static", 200)
                        max_dynamic = spec.get("max_options_dynamic", 100)

                        if ds_type == "dynamic" and opt_count > max_dynamic:
                            self.errors.append(
                                f"Screen '{screen_id}' Dropdown: dynamic exceeds {max_dynamic} with images"
                            )
                        elif ds_type == "static" and opt_count > max_static:
                            self.errors.append(
                                f"Screen '{screen_id}' Dropdown: static exceeds {max_static} options"
                            )

        # Check image URL
        if comp_type == "Image":
            src = component.get("src", "")
            if src and not src.startswith("https://"):
                self.errors.append(
                    f"Screen '{screen_id}' Image: must use HTTPS URL"
                )

        # Check calendar mode
        if comp_type == "CalendarPicker":
            mode = component.get("mode", "single")
            if mode not in spec.get("modes", []):
                self.errors.append(
                    f"Screen '{screen_id}' CalendarPicker: invalid mode '{mode}'"
                )

        return len(self.errors) == 0

    def validate_all_components(self, flow_data: Dict) -> Tuple[int, int]:
        """Validate all components in flow - returns (errors, warnings)"""
        total_errors = 0
        total_warnings = 0

        screens = flow_data.get("screens", [])
        for screen in screens:
            if not isinstance(screen, dict):
                continue

            screen_id = screen.get("id", "unknown")
            layout = screen.get("layout", {})
            children = layout.get("children", [])

            for i, component in enumerate(children):
                if not isinstance(component, dict):
                    continue

                is_valid = self.validate_component(component, screen_id, i)
                total_errors += len(self.errors)
                total_warnings += len(self.warnings)

                if not is_valid:
                    for error in self.errors:
                        print(f"{Fore.RED}❌ {error}{Style.RESET_ALL}")
                    for warning in self.warnings:
                        print(f"{Fore.YELLOW}⚠ {warning}{Style.RESET_ALL}")

        return total_errors, total_warnings


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python validate_components.py <flow.json>")
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

    validator = ComponentValidator()
    errors, warnings = validator.validate_all_components(flow_data)

    print(f"\n{Fore.CYAN}Component Validation Results:{Style.RESET_ALL}")
    if errors == 0 and warnings == 0:
        print(f"{Fore.GREEN}✅ All components valid!{Style.RESET_ALL}\n")
    else:
        if errors > 0:
            print(f"{Fore.RED}{errors} error(s){Style.RESET_ALL}")
        if warnings > 0:
            print(f"{Fore.YELLOW}{warnings} warning(s){Style.RESET_ALL}")
        print()

    sys.exit(0 if errors == 0 else 1)


if __name__ == "__main__":
    main()
