# Data Model: Static vs Dynamic Properties

Understanding how data flows through your WhatsApp Flow is crucial for building interactive experiences. This guide covers form inputs, screen data, and dynamic binding.

---

## Two Types of Data

### Static Data
Fixed strings, numbers, or arrays defined directly in Flow JSON.

```json
{
  "type": "TextBody",
  "text": "Hello, welcome!"
}
```

### Dynamic Data
Values provided by:
1. **User input** via form fields (`${form.field_name}`)
2. **Server endpoints** via screen data (`${data.field_name}`)
3. **Global references** from other screens (`${screen.SCREEN_ID.form.field}`)
4. **Nested expressions** with calculations (`${1 + 2}`)

---

## Form Data: User Input

When users fill out input components (TextInput, DatePicker, Dropdown, etc.), their values are stored in the `form` object.

### Form Binding Syntax

```json
${form.field_name}
```

- `field_name` must match the component's `name` property
- Available after user provides value
- Persists across screens via global referencing

### Example: Simple Form Data

```json
{
  "screens": [
    {
      "id": "COLLECT_NAME",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextInput",
            "name": "first_name",
            "label": "First Name",
            "required": true
          },
          {
            "type": "TextInput",
            "name": "last_name",
            "label": "Last Name"
          },
          {
            "type": "Footer",
            "label": "Continue",
            "on-click-action": {
              "action": "navigate",
              "next_screen": "CONFIRMATION"
            }
          }
        ]
      }
    },
    {
      "id": "CONFIRMATION",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "You entered: ${form.first_name} ${form.last_name}"
          },
          {
            "type": "Footer",
            "label": "Confirm"
          }
        ]
      }
    }
  ]
}
```

Here:
- User enters `first_name` and `last_name` in COLLECT_NAME
- On CONFIRMATION screen, `${form.first_name}` and `${form.last_name}` display their values
- Form data persists across all screens in the flow

### Form Field Data Types

Form values are always strings unless component specifies otherwise:

```json
{
  "type": "TextInput",
  "name": "email",
  "input-type": "email"
}
```

Component `input-type` options:
- `text` - String (default)
- `number` - Numeric string (validated as number)
- `email` - Email string (validated format)
- `phone` - Phone string (validated format)
- `password` - Masked string
- `passcode` - Numeric string, masked
- `date` - Date string (YYYY-MM-DD)

---

## Screen Data: From Server

Server endpoints can send dynamic data to populate lists, prices, inventory, etc.

### Screen Data Declaration

Define expected data structure using JSON Schema:

```json
{
  "id": "PRODUCT_SELECTION",
  "data": {
    "type": "object",
    "properties": {
      "products": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": { "type": "string" },
            "name": { "type": "string" },
            "price": { "type": "number" },
            "in_stock": { "type": "boolean" }
          }
        },
        "__example__": [
          {
            "id": "SKU001",
            "name": "Laptop",
            "price": 999.99,
            "in_stock": true
          }
        ]
      },
      "currency": {
        "type": "string",
        "__example__": "USD"
      }
    }
  },
  "layout": { ... }
}
```

**Critical**: Every dynamic field must have `__example__` for preview mode.

### Screen Data Binding Syntax

```json
${data.field_name}
```

- `field_name` corresponds to properties in screen's `data` declaration
- Available only after data_exchange action completes
- Provides server-driven content

### Example: Dynamic Dropdown

```json
{
  "id": "CITY_SELECTION",
  "data": {
    "type": "object",
    "properties": {
      "cities": {
        "type": "array",
        "items": { "type": "string" },
        "__example__": ["New York", "Los Angeles", "Chicago"]
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Select Your City"
      },
      {
        "type": "Dropdown",
        "name": "selected_city",
        "data-source": {
          "type": "dynamic",
          "values": "${data.cities}"
        }
      },
      {
        "type": "Footer",
        "label": "Confirm"
      }
    ]
  }
}
```

Server provides `cities` array, dropdown displays options dynamically.

---

## Form vs Data: When to Use Each

| Need | Use | Example |
|------|-----|---------|
| User enters text | Form | Name, email, address |
| Server provides options | Data | Product list, categories |
| User selects from list | Form (static) or Form (dynamic from data) | Dropdown from server list |
| Display user's choice | Form | Confirmation: "You selected ${form.choice}" |
| Display server info | Data | "Your balance: ${data.balance}" |
| Conditional logic | Form or Data | "if ${form.age} > 18" |

---

## Global Data Referencing (v4.0+)

Access form or data from ANY screen in the flow without passing it through navigate payloads.

### Global Reference Syntax

```json
${screen.SCREEN_ID.form.field_name}
${screen.SCREEN_ID.data.field_name}
```

### Example: Multi-Step Order Flow

```json
{
  "version": "7.1",
  "screens": [
    {
      "id": "PRODUCT_CHOICE",
      "data": {
        "type": "object",
        "properties": {
          "products": {
            "type": "array",
            "items": { "type": "object" },
            "__example__": []
          }
        }
      },
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "Dropdown",
            "name": "selected_product",
            "data-source": { "type": "dynamic", "values": "${data.products}" }
          },
          {
            "type": "Footer",
            "label": "Next",
            "on-click-action": {
              "action": "navigate",
              "next_screen": "SHIPPING"
            }
          }
        ]
      }
    },
    {
      "id": "SHIPPING",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Ship your ${screen.PRODUCT_CHOICE.form.selected_product} to:"
          },
          {
            "type": "TextInput",
            "name": "address"
          },
          {
            "type": "Footer",
            "label": "Review"
          }
        ]
      }
    },
    {
      "id": "REVIEW",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Product: ${screen.PRODUCT_CHOICE.form.selected_product}\nAddress: ${screen.SHIPPING.form.address}"
          },
          {
            "type": "Footer",
            "label": "Confirm"
          }
        ]
      }
    }
  ]
}
```

**Benefits**:
- No need to manually pass data through navigate payloads
- Forward references work (REVIEW references SHIPPING before it completes)
- Cleaner, more maintainable flows

---

## Navigate Payload (Traditional Approach)

Before global referencing (pre-v4.0), data was passed via navigate action:

```json
{
  "action": "navigate",
  "next_screen": "REVIEW",
  "payload": {
    "product": "${form.selected_product}",
    "quantity": "${form.quantity}"
  }
}
```

**Modern approach**: Use global references instead. Only use payload for small, specific hand-offs if needed.

---

## Form Component (Optional v4.0+)

Prior to v4.0, all inputs had to be wrapped in a Form component. Now it's optional.

### Without Form (Recommended)

```json
{
  "type": "TextInput",
  "name": "email",
  "label": "Email"
}
```

### With Form (Legacy, still supported)

```json
{
  "type": "Form",
  "children": [
    {
      "type": "TextInput",
      "name": "email",
      "label": "Email"
    }
  ]
}
```

Functionally equivalent. Prefer unwrapped approach for simpler JSON.

---

## Data Exchange Action

To fetch dynamic data from server, use `data_exchange` action:

```json
{
  "type": "Footer",
  "label": "Load Products",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "category": "${form.category}"
    }
  }
}
```

Server receives `payload`, returns data matching screen's `data` schema, components update automatically.

See `13-actions.md` and `16-data-endpoints.md` for details.

---

## Nested Expressions (v6.0+)

Combine data with calculations:

```json
${`${form.quantity} * ${data.unit_price}`}
```

See `11-nested-expressions.md` for full syntax and examples.

---

## Best Practices

1. **Declare all dynamic fields** in screen `data` with examples
2. **Use global references** instead of navigate payloads when possible
3. **Keep forms simple** - collect data that requires user input
4. **Fetch data on demand** - use data_exchange only when needed
5. **Always include `__example__`** in data properties
6. **Use meaningful field names** - `first_name` not `fn`
7. **Validate early** - use server data_exchange to validate form submission
8. **Mask sensitive data** - use `sensitive` array for passwords, SSNs, etc.

---

## Next Steps

- Learn **form input components** in `04-input-components.md`
- Learn **data validation** in `13-actions.md`
- Learn **conditional logic** in `10-conditional-logic.md`
- Learn **server integration** in `16-data-endpoints.md`
