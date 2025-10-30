# Global Data Referencing (v4.0+)

Access form and data from any screen without passing through navigate payloads.

---

## Global Reference Syntax

```json
${screen.SCREEN_ID.form.field_name}
${screen.SCREEN_ID.data.field_name}
```

- `SCREEN_ID` - The screen you're referencing
- `form.field_name` - User input from that screen
- `data.field_name` - Server data from that screen

---

## Simple Global Reference Example

### Screen 1: Collect Name

```json
{
  "id": "GET_NAME",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextInput",
        "name": "first_name",
        "label": "First Name"
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
          "next_screen": "GET_EMAIL"
        }
      }
    ]
  }
}
```

### Screen 2: Collect Email (No Payload)

Instead of passing data via navigate payload, reference it globally:

```json
{
  "id": "GET_EMAIL",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "Hello, ${screen.GET_NAME.form.first_name}!"
      },
      {
        "type": "TextInput",
        "name": "email",
        "label": "Email",
        "input-type": "email"
      },
      {
        "type": "Footer",
        "label": "Continue"
      }
    ]
  }
}
```

### Screen 3: Review (Reference Both Previous Screens)

```json
{
  "id": "REVIEW",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Review Your Information"
      },
      {
        "type": "TextBody",
        "text": "Name: ${screen.GET_NAME.form.first_name} ${screen.GET_NAME.form.last_name}"
      },
      {
        "type": "TextBody",
        "text": "Email: ${screen.GET_EMAIL.form.email}"
      },
      {
        "type": "Footer",
        "label": "Confirm"
      }
    ]
  }
}
```

---

## Forward References

You can reference screens that haven't been filled yet (forward reference):

```json
{
  "id": "CONFIRMATION",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "You selected: ${screen.PRODUCT_PICKER.form.product}"
      },
      {
        "type": "Footer",
        "label": "Complete"
      }
    ]
  }
}
```

Even if `PRODUCT_PICKER` hasn't been filled yet, the reference will work once that screen is completed.

**Empty value handling**: If screen not yet filled, displays as empty or placeholder.

---

## Data From Server

Reference server-provided data from any screen:

### Screen with Server Data

```json
{
  "id": "PRODUCTS",
  "data": {
    "type": "object",
    "properties": {
      "available_products": {
        "type": "array",
        "items": { "type": "string" },
        "__example__": ["Widget A", "Widget B"]
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "Dropdown",
        "name": "selected_product",
        "label": "Select Product",
        "data-source": {
          "type": "dynamic",
          "values": "${data.available_products}"
        }
      }
    ]
  }
}
```

### Reference Product Data in Later Screen

```json
{
  "id": "DETAILS",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "Available products: ${screen.PRODUCTS.data.available_products}"
      }
    ]
  }
}
```

---

## Complex Global References

### Multi-Level Data Access

```json
{
  "id": "REVIEW",
  "data": {
    "type": "object",
    "properties": {
      "pricing": {
        "type": "object",
        "properties": {
          "subtotal": { "type": "number", "__example__": 100 },
          "tax": { "type": "number", "__example__": 10 }
        },
        "__example__": {}
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "Subtotal: ${screen.REVIEW.data.pricing.subtotal}"
      }
    ]
  }
}
```

---

## When to Use Global References

### Use Global References When:
- Needing to display information from earlier screens
- Avoiding complex navigate payloads
- Building review/confirmation screens
- Referencing the same data in multiple places
- Workflows with 3+ screens

### Use Navigate Payload When:
- Passing small specific values to next screen
- One-time data handoff
- Simple 2-screen flows
- Legacy code (pre-v4.0)

---

## Global References vs Navigate Payload

**Traditional (with payload):**

```json
{
  "type": "Footer",
  "label": "Next",
  "on-click-action": {
    "action": "navigate",
    "next_screen": "SCREEN_2",
    "payload": {
      "name": "${form.name}",
      "email": "${form.email}"
    }
  }
}
```

Then in SCREEN_2, access via payload (not directly supported in display, only in data_exchange).

**Modern (global references):**

```json
{
  "type": "Footer",
  "label": "Next",
  "on-click-action": {
    "action": "navigate",
    "next_screen": "SCREEN_2"
  }
}
```

In SCREEN_2:
```json
${screen.SCREEN_1.form.name}
${screen.SCREEN_1.form.email}
```

**Advantages of global references:**
- Simpler navigation (no payload needed)
- Easier review screens
- Reusable across multiple screens
- Forward references possible

---

## Practical Example: Multi-Step Checkout

```json
{
  "screens": [
    {
      "id": "SHIPPING",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextHeading",
            "text": "Shipping Address"
          },
          {
            "type": "TextInput",
            "name": "address",
            "label": "Street Address"
          },
          {
            "type": "Footer",
            "label": "Next"
          }
        ]
      }
    },
    {
      "id": "BILLING",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Ship to: ${screen.SHIPPING.form.address}"
          },
          {
            "type": "CheckboxGroup",
            "name": "same_as_shipping",
            "data-source": {
              "type": "static",
              "values": ["Use shipping address for billing"]
            }
          },
          {
            "type": "Footer",
            "label": "Next"
          }
        ]
      }
    },
    {
      "id": "PAYMENT",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextHeading",
            "text": "Payment"
          },
          {
            "type": "TextInput",
            "name": "card_number",
            "label": "Card Number"
          },
          {
            "type": "Footer",
            "label": "Review Order"
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
            "type": "TextHeading",
            "text": "Order Confirmation"
          },
          {
            "type": "TextBody",
            "text": "Shipping: ${screen.SHIPPING.form.address}"
          },
          {
            "type": "TextBody",
            "text": "Card: ****${`${screen.PAYMENT.form.card_number}`.slice(-4)}"
          },
          {
            "type": "Footer",
            "label": "Place Order"
          }
        ]
      }
    }
  ]
}
```

---

## Global References with Conditional Logic

Conditionally show information from other screens:

```json
{
  "id": "SUMMARY",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "If",
        "condition": "${screen.BILLING.form.same_as_shipping}",
        "then": [
          {
            "type": "TextBody",
            "text": "Billing matches shipping address"
          }
        ],
        "else": [
          {
            "type": "TextBody",
            "text": "Billing address: ${screen.BILLING.form.billing_address}"
          }
        ]
      }
    ]
  }
}
```

---

## Performance Considerations

Global references are resolved at runtime. For large flows:

1. **Avoid excessive global references** - Don't reference every field everywhere
2. **Use server-side aggregation** - For complex data relationships
3. **Clear field names** - Makes code more maintainable
4. **Limit forward references** - Don't reference screens too far ahead

---

## Best Practices

1. **Use global references for review screens** - Perfect use case
2. **Keep references simple** - One or two fields per reference
3. **Use meaningful names** - `${screen.ADDRESS.form.street}` is clear
4. **Avoid deep nesting** - Don't reference nested objects excessively
5. **Validate server-side** - Global refs are for display, not business logic
6. **Test forward references** - Ensure they handle empty states
7. **Document complex flows** - Help future maintainers understand flow
8. **Use consistent screen IDs** - Makes references predictable
9. **Consider readability** - Choose global refs over complex payloads
10. **Version your flows** - Global ref syntax may change in future versions

---

## Next Steps

- Learn **actions** in `13-actions.md`
- Learn **routing models** in `15-routing-model.md`
- Learn **server integration** in `16-data-endpoints.md`
