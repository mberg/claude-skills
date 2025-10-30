# Selection Components

Components for selecting from options: checkboxes, radio buttons, dropdowns, and more.

---

## CheckboxGroup

Multiple selection from a list of options.

**Properties:**
- `name` - Field identifier (required)
- `label` - Group label (optional)
- `data-source` - Options source (static or dynamic)
- `required` - Must select at least one (default: false)
- `init-value` - Pre-selected options (array)

### Static Options

```json
{
  "type": "CheckboxGroup",
  "name": "interests",
  "label": "Select your interests:",
  "data-source": {
    "type": "static",
    "values": [
      "Sports",
      "Music",
      "Travel",
      "Food",
      "Technology"
    ]
  }
}
```

### Dynamic Options (from server)

```json
{
  "id": "PREFERENCES",
  "data": {
    "type": "object",
    "properties": {
      "categories": {
        "type": "array",
        "items": { "type": "string" },
        "__example__": ["Books", "Movies", "Games"]
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "CheckboxGroup",
        "name": "selected_categories",
        "label": "Choose categories:",
        "data-source": {
          "type": "dynamic",
          "values": "${data.categories}"
        }
      }
    ]
  }
}
```

### Form Value

Selected items stored as array:

```json
${form.interests}  // ["Sports", "Music"]
```

### CheckboxGroup Limits

- Minimum 1 option, maximum 20 options
- Cannot require selection in v4.0 (always optional)
- v5.0+: `required: true` supported

---

## RadioButtonsGroup

Single selection from a list of options.

**Properties:**
- `name` - Field identifier (required)
- `label` - Group label (optional)
- `data-source` - Options source (static or dynamic)
- `required` - Must select one (default: false)
- `init-value` - Pre-selected option (string, not array)

### Static Radio Buttons

```json
{
  "type": "RadioButtonsGroup",
  "name": "shipping_method",
  "label": "Select shipping method:",
  "data-source": {
    "type": "static",
    "values": [
      "Standard (5-7 days)",
      "Express (2-3 days)",
      "Overnight"
    ]
  },
  "required": true
}
```

### Form Value

Single selected item:

```json
${form.shipping_method}  // "Express (2-3 days)"
```

### RadioButtonsGroup Limits

- Minimum 1 option, maximum 20 options
- User must select exactly one (or zero if not required)

---

## Dropdown

Dropdown selector with static or dynamic options.

**Properties:**
- `name` - Field identifier (required)
- `label` - Field label
- `data-source` - Options source
- `required` - Must select (default: false)
- `init-value` - Pre-selected option

### Static Dropdown

```json
{
  "type": "Dropdown",
  "name": "country",
  "label": "Country",
  "data-source": {
    "type": "static",
    "values": [
      "United States",
      "Canada",
      "Mexico",
      "United Kingdom"
    ]
  },
  "required": true
}
```

### Dynamic Dropdown

```json
{
  "type": "Dropdown",
  "name": "product",
  "label": "Select Product",
  "data-source": {
    "type": "dynamic",
    "values": "${data.products}"
  }
}
```

### Dropdown with Images (v5.0+)

Dropdowns can include thumbnail images with options:

```json
{
  "type": "Dropdown",
  "name": "color_choice",
  "label": "Choose Color",
  "data-source": {
    "type": "dynamic",
    "values": "${data.colors}"
  }
}
```

Server provides:
```json
{
  "colors": [
    {
      "title": "Red",
      "description": "Bright red",
      "image": "https://example.com/red.jpg"
    },
    {
      "title": "Blue",
      "description": "Deep blue",
      "image": "https://example.com/blue.jpg"
    }
  ]
}
```

Options display with thumbnails.

### Dropdown Limits

- Static: 1-200 options
- Dynamic with images: 1-100 options
- Dynamic without images: 1-200 options

---

## OptIn

Checkbox with optional action link (like newsletter signup).

**Properties:**
- `name` - Field identifier (required)
- `label` - Checkbox label (required, max 80 chars)
- `description` - Additional info (optional, max 200 chars)
- `action-url` - URL for "Learn more" link (optional)
- `action-text` - Link text (optional, default: "Learn more")
- `required` - Must be checked (default: false)

### Basic OptIn

```json
{
  "type": "OptIn",
  "name": "newsletter",
  "label": "Subscribe to our newsletter"
}
```

### OptIn with Description and Link

```json
{
  "type": "OptIn",
  "name": "terms_agree",
  "label": "I agree to the Terms of Service",
  "description": "Please read our full terms before proceeding",
  "action-url": "https://example.com/terms",
  "action-text": "View Terms",
  "required": true
}
```

### Multiple OptIn Components

You can have multiple OptIn on one screen (max 5 per screen):

```json
{
  "type": "OptIn",
  "name": "marketing",
  "label": "Send me marketing emails"
},
{
  "type": "OptIn",
  "name": "sms",
  "label": "Send me SMS updates",
  "required": false
}
```

### Form Values

Each OptIn stores boolean:

```json
${form.newsletter}  // true or false
${form.terms_agree} // true or false
```

### OptIn Constraints

- Maximum 5 per screen
- Label max 80 characters
- Description max 200 characters
- Can trigger `open_url`, `navigate`, or `data_exchange` actions

---

## Comparing Selection Components

| Component | Selection | Limit | Use Case |
|-----------|-----------|-------|----------|
| CheckboxGroup | Multiple | 20 options | "Select all that apply" |
| RadioButtonsGroup | Single | 20 options | Required single choice |
| Dropdown | Single | 200 static, 100 with images | Long lists, space-constrained |
| OptIn | True/False | 5 per screen | Agreements, subscriptions |

---

## Actions on Selection

Selection components can trigger actions without a Footer:

```json
{
  "type": "Dropdown",
  "name": "category",
  "label": "Select Category",
  "data-source": {
    "type": "static",
    "values": ["A", "B", "C"]
  },
  "on-select-action": {
    "action": "data_exchange",
    "payload": {
      "selected_category": "${form.category}"
    }
  }
}
```

When user selects, action fires immediately (no button needed).

---

## Conditional Dropdowns

Show/hide options based on previous selections:

```json
{
  "id": "CATEGORY_PRODUCT",
  "data": {
    "type": "object",
    "properties": {
      "products_by_category": {
        "type": "object",
        "__example__": {}
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "Dropdown",
        "name": "category",
        "label": "Category",
        "data-source": {
          "type": "static",
          "values": ["Electronics", "Clothing", "Food"]
        },
        "on-select-action": {
          "action": "data_exchange",
          "payload": { "category": "${form.category}" }
        }
      },
      {
        "type": "Dropdown",
        "name": "product",
        "label": "Product",
        "data-source": {
          "type": "dynamic",
          "values": "${data.products_by_category[${form.category}]}"
        }
      }
    ]
  }
}
```

---

## Best Practices

1. **Use appropriate component** - Checkboxes for multiple, radio for single, dropdown for long lists
2. **Limit options to 5-7** when possible - More becomes overwhelming
3. **Sort options logically** - Alphabetical, frequency, or importance
4. **Provide clear labels** - "Shipping Method" not "Shipping"
5. **Set required only when necessary** - Not all selections are mandatory
6. **Pre-populate when possible** - Use `init-value` for defaults
7. **Use dynamic data for changing options** - Server-provided lists
8. **Validate selections** - Double-check in data_exchange
9. **Don't mix component types on screen** - Consistency matters
10. **Consider UX for mobile** - Dropdowns preferred for long lists (smaller tap targets)

---

## Next Steps

- Learn **date/time components** in `06-date-time-components.md`
- Learn **media components** in `07-media-components.md`
- Learn **actions on selection** in `13-actions.md`
