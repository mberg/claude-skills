# Validation Rules & Constraints

Rules and limits for building valid WhatsApp Flows.

---

## Character Limits

| Component | Limit | Notes |
|-----------|-------|-------|
| TextHeading | 80 | Bold weight optional |
| TextSubheading | 80 | - |
| TextBody | 4096 | Markdown v5.1+ |
| TextCaption | 409 | Markdown v5.1+ |
| RichText | 4096 | Full markdown v5.1+ |
| TextInput | 80 | Default max-length |
| TextArea | 600 | Default max-length |
| Footer label | 30 | Button text |
| OptIn label | 80 | Checkbox label |
| OptIn description | 200 | Optional text |
| EmbeddedLink text | 25 | Link text |

---

## Component Limits Per Screen

| Component | Max per Screen | Notes |
|-----------|---|---|
| Image | 3 | Visual content |
| ImageCarousel | 2 | v7.1+ |
| EmbeddedLink | 2 | Secondary actions |
| OptIn | 5 | Checkboxes |
| Footer | 1 | Primary action |
| RichText | 1 | (v5.1-v6.2 standalone) |
| NavigationList | 2 | v6.2+ |
| Components total | 50 | All components |

---

## Option Limits

| Component | Min | Max | Notes |
|-----------|-----|-----|-------|
| CheckboxGroup | 1 | 20 | Multiple select |
| RadioButtonsGroup | 1 | 20 | Single select |
| Dropdown (static) | 1 | 200 | Static values |
| Dropdown (dynamic, no img) | 1 | 200 | From server |
| Dropdown (dynamic, with img) | 1 | 100 | Images included |
| OptIn | 1 | 5 | Per screen |
| ChipsSelector | 2 | 20 | Multi-select |
| NavigationList | 1 | 20 | Rich items |

---

## Screen Limits

- Maximum screens: Unlimited
- Maximum screens per flow: Practical limit ~50-100
- Minimum screens: 1 (single terminal)
- Terminal screens: Can have 0-n (typically SUCCESS + ERROR)
- Reserved IDs: `SUCCESS` only

---

## Flow JSON Size

- Maximum Flow JSON size: 10MB
- Practical limit: 500KB-1MB for performance
- Includes all screens, components, data schemas
- Large flows = slow load times

---

## Field Name Rules

Field names (in `name` property):
- Alphanumeric and underscore: `[a-zA-Z0-9_]`
- Start with letter or underscore
- Case-sensitive (`first_name` ≠ `firstName`)
- No spaces or special characters
- Recommended: snake_case (first_name)

---

## Screen ID Rules

Screen IDs must:
- Be unique across flow
- Alphanumeric and underscore: `[a-zA-Z0-9_]`
- Not be `SUCCESS` (reserved)
- Be referenced in routing_model
- Match navigation targets exactly

---

## Data Schema Rules

Every dynamic field needs `__example__`:

```json
{
  "type": "object",
  "properties": {
    "products": {
      "type": "array",
      "items": { "type": "string" },
      "__example__": ["Product A", "Product B"]
    },
    "total": {
      "type": "number",
      "__example__": 99.99
    }
  }
}
```

Without `__example__`, preview fails.

---

## Image URL Rules

- Must be HTTPS (no HTTP)
- Must be publicly accessible
- No redirects preferred
- Recommended size: 600x400px
- Max size: 300KB

---

## Validation Rules Summary

### Required

- Flow JSON must be valid JSON
- `version` property required
- `screens` array required
- Each screen must have `id` and `layout`
- Terminal screens must have Footer with complete action

### Conditional

- If using `routing_model`, must have `data_api_version`
- If using dynamic data, must have `__example__`
- If Footer in If/Switch, must be in all branches
- If using `sensitive` array, fields must exist

### Field Names

- `name` required for input components
- Field names must be unique per screen
- Field names alphanumeric + underscore

### Screen IDs

- Must be unique
- Cannot be `SUCCESS` (reserved)
- Used in routing_model if present

---

## Common Validation Errors

### Error: Missing `__example__`

```json
// Wrong:
"data": {
  "products": {
    "type": "array",
    "items": { "type": "string" }
  }
}

// Right:
"data": {
  "products": {
    "type": "array",
    "items": { "type": "string" },
    "__example__": ["Product A"]
  }
}
```

### Error: Footer in If without else

```json
// Wrong:
{
  "type": "If",
  "condition": "${form.agree}",
  "then": [
    {
      "type": "Footer",
      "label": "Continue"
    }
  ]
}

// Right:
{
  "type": "If",
  "condition": "${form.agree}",
  "then": [
    {
      "type": "Footer",
      "label": "Continue"
    }
  ],
  "else": [
    {
      "type": "Footer",
      "label": "Continue",
      "enabled": false
    }
  ]
}
```

### Error: Non-existent screen in routing

```json
// Wrong:
{
  "routing_model": {
    "SCREEN_A": ["SCREEN_B"]
  },
  "screens": [
    { "id": "SCREEN_A", "layout": {} }
    // SCREEN_B missing!
  ]
}

// Right:
{
  "routing_model": {
    "SCREEN_A": ["SCREEN_B"],
    "SCREEN_B": ["SUCCESS"]
  },
  "screens": [
    { "id": "SCREEN_A", "layout": {} },
    { "id": "SCREEN_B", "layout": {} }
  ]
}
```

---

## Testing & Validation

Use Python validation script (validate_flow.py) to catch errors:

```bash
python validation/validate_flow.py my_flow.json
```

Checks:
- Valid JSON structure
- Required properties
- Field name uniqueness
- Screen ID validity
- Routing model consistency
- Data schema completeness
- Character limits
- Component limits

---

## Best Practices for Valid Flows

1. **Validate early** - Use tools before deploying
2. **Test all paths** - Ensure every route works
3. **Use examples** - Always provide `__example__` values
4. **Meaningful names** - Clear field and screen names
5. **Document structure** - Comment complex flows
6. **Version control** - Track changes
7. **Incremental changes** - Modify and test small changes
8. **Preview mode** - Test with example data
9. **Mobile testing** - Verify on actual device
10. **Error scenarios** - Test invalid inputs

---

## Next Steps

- Use **validation scripts** in `validation/` directory
- See **examples** in `examples/` directory
- Learn **version features** in `19-version-features.md`
