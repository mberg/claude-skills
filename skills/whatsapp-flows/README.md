# WhatsApp Flows Skill

Expert guidance for authoring WhatsApp Business Account Flows with comprehensive progressive reference documentation and validation tools.

## Quick Start

1. **New to Flows?** Start here:
   - `reference/01-core-structure.md` - Understand Flow JSON structure
   - `reference/02-data-model.md` - Learn data binding and user input

2. **Building your first flow?** Follow the examples:
   - `examples/01-simple-form.json` - Multi-screen survey form
   - `examples/02-conditional-flow.json` - Conditional branching
   - `examples/03-product-selection.json` - Dynamic server data

3. **Validate your flow:**
   ```bash
   python validation/validate_flow.py your-flow.json
   python validation/validate_components.py your-flow.json
   ```

## Documentation Structure

The skill uses **progressive reference loading** - load what you need, when you need it:

### Core (Always Available)
- `01-core-structure.md` - Flow JSON structure, screens, layouts
- `02-data-model.md` - Static/dynamic data, form binding, data schema

### Components (Load by Category)
- `03-text-components.md` - TextHeading, TextBody, RichText, etc.
- `04-input-components.md` - TextInput, TextArea, validation
- `05-selection-components.md` - Dropdowns, checkboxes, radio buttons
- `06-date-time-components.md` - DatePicker, CalendarPicker
- `07-media-components.md` - Image, PhotoPicker, DocumentPicker, ImageCarousel
- `08-rich-content.md` - RichText with markdown formatting
- `09-navigation-components.md` - NavigationList, ChipsSelector, EmbeddedLink

### Logic & Advanced
- `10-conditional-logic.md` - If/Switch components for branching
- `11-nested-expressions.md` - Calculations and complex logic (v6.0+)
- `12-global-referencing.md` - Access data from any screen (v4.0+)

### Actions & Routing
- `13-actions.md` - navigate, data_exchange, complete, update_data, open_url
- `14-footer-component.md` - Primary action button
- `15-routing-model.md` - Server-driven flow control
- `16-data-endpoints.md` - Backend integration and dynamic data

### Quality & Reference
- `17-validation-rules.md` - Character limits, component constraints
- `18-sensitive-data.md` - Protecting passwords, SSNs, etc. (v5.1+)
- `19-version-features.md` - Feature availability by version
- `20-quick-reference.md` - Quick lookup cheat sheet

## Key Components

### Text
- TextHeading (80 chars) - Top titles
- TextSubheading (80 chars) - Subtitles
- TextBody (4096 chars) - Body text with markdown support
- TextCaption (409 chars) - Small supplementary text
- RichText (4096 chars) - Full markdown formatting (v5.1+)

### Input
- TextInput - Single line, 7 input types (email, phone, password, etc.)
- TextArea - Multi-line, 600 chars default
- DatePicker - Native date selection
- CalendarPicker - Calendar with range selection (v6.1+)
- PhotoPicker - Image upload (v5.0+)
- DocumentPicker - File upload (v5.0+)

### Selection
- CheckboxGroup - Multiple selection (max 20)
- RadioButtonsGroup - Single selection (max 20)
- Dropdown - Dropdown list (max 200 static, 100 with images)
- OptIn - Checkbox with action link (max 5 per screen)
- ChipsSelector - Button-like multi-select (v6.3+, 2-20 options)
- NavigationList - Rich items with descriptions (v6.2+, 1-20 items)

### Media
- Image - Display image (max 3 per screen)
- ImageCarousel - Slide images (v7.1+, 1-3 images, max 2 per screen)

### Navigation & Actions
- Footer - Primary button (required on terminal screens)
- EmbeddedLink - Secondary link (max 2 per screen)
- If/Switch - Conditional rendering

## Actions

```json
// Navigate to screen
{ "action": "navigate", "next_screen": "SCREEN_NAME" }

// Send data to server
{ "action": "data_exchange", "payload": { "field": "value" } }

// Complete flow
{ "action": "complete", "payload": { "result": "data" } }

// Update screen state
{ "action": "update_data", "payload": { "field": "value" } }

// Open URL
{ "action": "open_url", "url": "https://example.com" }
```

## Data Binding

```json
// Form input (user enters)
${form.field_name}

// Server data (from endpoint)
${data.field_name}

// Global reference (any screen)
${screen.SCREEN_NAME.form.field}
${screen.SCREEN_NAME.data.field}

// Expression (calculation)
${`${form.age} >= 18`}
${`${form.price} * ${form.quantity}`}
```

## Common Limits

- Components per screen: 50
- TextHeading/TextSubheading: 80 characters
- TextBody/RichText: 4096 characters
- TextCaption: 409 characters
- TextInput: 80 characters (configurable)
- TextArea: 600 characters (configurable)
- Dropdown options (static): 200 max
- Dropdown options (with images): 100 max
- Select options: 20 max
- Images per screen: 3 max
- OptIn per screen: 5 max
- EmbeddedLink per screen: 2 max
- Flow JSON size: 10MB max

## Validation Tools

### validate_flow.py
Validates overall Flow JSON structure:
- Required properties (version, screens)
- Screen definitions and uniqueness
- Layout and component structure
- Routing model consistency
- Data schema completeness

```bash
python validation/validate_flow.py my-flow.json
```

### validate_components.py
Validates individual components:
- Component type validation
- Character limits
- Option counts
- Required properties
- Input type validation

```bash
python validation/validate_components.py my-flow.json
```

## Version Support

Current: 7.1 (Latest)
Supported: 4.0 - 7.1

Key versions:
- **v4.0**: If/Switch, optional Form, global references, routing_model
- **v5.0**: PhotoPicker, DocumentPicker
- **v5.1**: RichText, markdown, sensitive data masking
- **v6.0**: update_data, open_url, nested expressions
- **v6.1**: CalendarPicker
- **v6.2**: NavigationList, pattern validation
- **v6.3**: RichText + Footer combination, ChipsSelector
- **v7.0**: ImageCarousel improvements
- **v7.1**: Latest with all features

See `reference/19-version-features.md` for complete feature matrix.

## Best Practices

1. **Validate early** - Use validation tools before deploying
2. **Test all paths** - Ensure every flow branch works
3. **Server-side validation** - Never trust client-only validation
4. **HTTPS only** - All image URLs must be HTTPS
5. **User-friendly messages** - Clear instructions and error messages
6. **Minimal data collection** - Only ask what you need
7. **Secure sensitive data** - Mark passwords, SSNs as sensitive
8. **Progressive enhancement** - Start simple, add features gradually
9. **Mobile-first design** - Test on actual WhatsApp mobile
10. **Clear screen progression** - Users should understand flow

## Examples

### Simple Form
See `examples/01-simple-form.json` for a customer survey with:
- Multi-screen form
- Global references for review
- Complete action with payload

### Conditional Flow
See `examples/02-conditional-flow.json` for age verification with:
- If component for branching
- Two different outcome paths
- Expression evaluation

### Product Selection
See `examples/03-product-selection.json` for e-commerce with:
- Dynamic dropdown from server
- Multi-step selection
- Global references across screens

## External Resources

- **WhatsApp Docs**: https://developers.facebook.com/docs/whatsapp/flows
- **Flow JSON Reference**: https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson
- **Components Reference**: https://developers.facebook.com/docs/whatsapp/flows/reference/components

## Getting Help

- Use `/whatsapp-reference [topic]` to load specific documentation
- Use `/validate-flow [path]` to validate your Flow JSON
- Use `/explain-component [name]` to get component details
- Check `reference/20-quick-reference.md` for quick lookup

## License

Part of Claude Code skill system. For use with WhatsApp Business Account flows development.
