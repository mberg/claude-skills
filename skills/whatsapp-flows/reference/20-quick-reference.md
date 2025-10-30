# Quick Component Reference

Quick lookup table of all WhatsApp Flow components.

---

## Text Components

| Component | Purpose | Max Chars | Markdown | v |
|-----------|---------|-----------|----------|---|
| TextHeading | Title text | 80 | No | 4.0 |
| TextSubheading | Subtitle | 80 | No | 4.0 |
| TextBody | Body text | 4096 | 5.1+ | 4.0 |
| TextCaption | Small text | 409 | 5.1+ | 4.0 |
| RichText | Formatted text | 4096 | Yes | 5.1 |

---

## Input Components

| Component | Input Type | Required | Max | v |
|-----------|-----------|----------|-----|---|
| TextInput | text/email/phone/number/password/passcode/date | Yes | 80 | 4.0 |
| TextArea | Multiline text | Yes | 600 | 4.0 |
| DatePicker | Date selection | Yes | - | 5.0 |
| CalendarPicker | Calendar (single/range) | Yes | - | 6.1 |
| PhotoPicker | Photo upload | Yes | - | 5.0 |
| DocumentPicker | Document upload | Yes | - | 5.0 |

---

## Selection Components

| Component | Selection | Max Options | v |
|-----------|-----------|-------------|---|
| CheckboxGroup | Multiple | 20 | 4.0 |
| RadioButtonsGroup | Single | 20 | 4.0 |
| Dropdown | Single (static/dynamic) | 200/100 | 4.0 |
| OptIn | Checkbox with link | 5/screen | 4.0 |
| ChipsSelector | Multiple (buttons) | 20 | 6.3 |
| NavigationList | Single (rich) | 20 | 6.2 |

---

## Media Components

| Component | Purpose | Max per Screen | v |
|-----------|---------|-----------------|---|
| Image | Display image | 3 | 4.0 |
| ImageCarousel | Slide images | 2 | 7.1 |

---

## Action Components

| Component | Purpose | Required | v |
|-----------|---------|----------|---|
| Footer | Primary button | Screen max 1 | 4.0 |
| EmbeddedLink | Secondary link | Screen max 2 | 4.0 |
| If | Conditional rendering | No | 4.0 |
| Switch | Multi-way conditional | No | 4.0 |

---

## Component Actions Support

| Component | navigate | data_exchange | complete | update_data | open_url |
|-----------|----------|---------------|----------|-------------|----------|
| Footer | ✓ | ✓ | ✓ | ✓ | ✗ |
| EmbeddedLink | ✓ | ✓ | ✗ | ✗ | ✓ |
| OptIn | ✓ | ✓ | ✗ | ✗ | ✓ |
| DatePicker | ✗ | ✓ | ✗ | ✗ | ✗ |
| Dropdown | ✓* | ✓ | ✗ | ✓ | ✗ |
| RadioButtons | ✓* | ✓ | ✗ | ✓ | ✗ |
| CheckboxGroup | ✓* | ✓ | ✗ | ✓ | ✗ |
| ChipsSelector | ✓* | ✓ | ✗ | ✓ | ✗ |
| NavigationList | ✓ | ✓ | ✗ | ✗ | ✗ |

*via on-select-action

---

## Actions Cheat Sheet

```json
// Navigate to screen
{
  "action": "navigate",
  "next_screen": "SCREEN_NAME"
}

// Send data to server
{
  "action": "data_exchange",
  "payload": { "field": "value" }
}

// Complete flow
{
  "action": "complete",
  "payload": { "result": "success" }
}

// Update screen data
{
  "action": "update_data",
  "payload": { "field": "new_value" }
}

// Open URL
{
  "action": "open_url",
  "url": "https://example.com"
}
```

---

## Data Binding Patterns

```json
// Form input
${form.field_name}

// Server data
${data.field_name}

// Global reference
${screen.SCREEN_NAME.form.field}
${screen.SCREEN_NAME.data.field}

// Expression
${`${form.age} >= 18`}
${`${form.price} * ${form.quantity}`}

// String concatenation
${`${form.first} + ' ' + ${form.last}`}
```

---

## Common Limits

| Item | Limit |
|------|-------|
| Screens per flow | Unlimited |
| Components per screen | 50 |
| Character: Heading | 80 |
| Character: Body | 4096 |
| Character: Caption | 409 |
| Character: TextInput | 80 |
| Character: TextArea | 600 |
| Images per screen | 3 |
| Carousel per screen | 2 |
| Dropdown options (static) | 200 |
| Dropdown options (with images) | 100 |
| Select options | 20 |
| OptIn per screen | 5 |
| EmbeddedLink per screen | 2 |
| NavigationList per screen | 2 |
| Flow JSON size | 10MB |

---

## Markdown Syntax

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold** text
*Italic* text
~~Strikethrough~~ (v6.0+)
`Inline code`

- Bullet list
- Another item

1. Numbered
2. List

[Link](https://example.com)

> Blockquote

| Header 1 | Header 2 |
|----------|----------|
| Cell     | Cell     |
```

---

## Version Feature Support

All features available in version 7.1 (latest). Check `19-version-features.md` for earlier versions.

---

## Field Name Rules

- Alphanumeric + underscore: `[a-zA-Z0-9_]`
- Start with letter/underscore
- Recommended: snake_case (`first_name`)
- Case-sensitive

---

## Input Types Reference

| Type | Format | Example | v |
|------|--------|---------|---|
| text | Any text | "hello" | 4.0 |
| number | Numeric | "42" | 4.0 |
| email | Email | "user@example.com" | 4.0 |
| phone | Phone | "+1234567890" | 4.0 |
| password | Masked | "*****" | 4.0 |
| passcode | Numeric masked | "****" | 4.0 |
| date | YYYY-MM-DD | "2024-03-15" | 5.0 |

---

## Common Flow Patterns

### Simple Form
TextInput → Footer navigate → SUCCESS

### Multi-Step
Screen 1 → Screen 2 → Screen 3 → SUCCESS

### Conditional
If condition → Branch A → SUCCESS
                Branch B → SUCCESS

### Validation
TextInput → Footer data_exchange → (valid) NEXT / (invalid) ERROR

### Dynamic
Dropdown on-select data_exchange → fetch options → update display

---

## Keyboard Shortcuts (Common IDEs)

- JSON format: Ctrl+Shift+I (VS Code)
- Validate JSON: Use online validator
- Tree view: IDE outline/symbols panel
- Search: Ctrl+F for screen IDs

---

## Debugging Checklist

- [ ] JSON valid (no syntax errors)
- [ ] All screen IDs unique
- [ ] All field names unique per screen
- [ ] All dynamic fields have `__example__`
- [ ] routing_model references existing screens
- [ ] Terminal screens have Footer
- [ ] Footer in If has else branch
- [ ] Image URLs are HTTPS
- [ ] Component counts within limits
- [ ] Character limits respected

---

## Learning Path

1. Start: `01-core-structure.md` and `02-data-model.md`
2. Components: `03-text-components.md` → `04-input-components.md` → `05-selection-components.md`
3. Advanced: `10-conditional-logic.md` → `13-actions.md`
4. Integration: `15-routing-model.md` → `16-data-endpoints.md`
5. Reference: This file for quick lookup

---

## External Resources

- Official Docs: https://developers.facebook.com/docs/whatsapp/flows
- Flow JSON Reference: https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson
- Components Reference: https://developers.facebook.com/docs/whatsapp/flows/reference/components

---

## Next Steps

- Use this as a **cheat sheet** while building
- Refer to **tier-specific docs** for detailed info
- Check **examples/** for complete flow samples
- Run **validate_flow.py** to catch errors
