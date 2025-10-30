# Conditional Logic: If & Switch (v4.0+)

Control flow behavior with conditional rendering and branching logic.

---

## If Component

Conditional rendering: show different content based on an expression.

**Properties:**
- `condition` - Boolean expression to evaluate
- `then` - Components to render if condition is true
- `else` - Components to render if condition is false (optional)

### Basic If

```json
{
  "type": "If",
  "condition": "${form.has_account}",
  "then": [
    {
      "type": "TextBody",
      "text": "Welcome back!"
    }
  ],
  "else": [
    {
      "type": "TextBody",
      "text": "Please create an account to continue"
    }
  ]
}
```

### If with Nested Expression

```json
{
  "type": "If",
  "condition": "${`${form.age} >= 18`}",
  "then": [
    {
      "type": "TextBody",
      "text": "You are eligible"
    }
  ],
  "else": [
    {
      "type": "TextBody",
      "text": "You must be 18 or older"
    }
  ]
}
```

### If with Complex Conditions

```json
{
  "type": "If",
  "condition": "${`${form.country} == 'USA' && ${form.age} >= 18`}",
  "then": [
    {
      "type": "TextBody",
      "text": "You are eligible for this service"
    }
  ]
}
```

---

## Switch Component

Multi-way branching based on a value.

**Properties:**
- `value` - The value to match against
- `cases` - Array of case objects with `value` and `children`
- `default` - Components if no case matches (optional)

### Basic Switch

```json
{
  "type": "Switch",
  "value": "${form.account_type}",
  "cases": [
    {
      "value": "free",
      "children": [
        {
          "type": "TextBody",
          "text": "You have a free account with basic features"
        }
      ]
    },
    {
      "value": "premium",
      "children": [
        {
          "type": "TextBody",
          "text": "You have premium access with all features"
        }
      ]
    },
    {
      "value": "enterprise",
      "children": [
        {
          "type": "TextBody",
          "text": "You have enterprise support"
        }
      ]
    }
  ],
  "default": [
    {
      "type": "TextBody",
      "text": "Unknown account type"
    }
  ]
}
```

### Switch on Data

Switch based on server-provided data:

```json
{
  "type": "Switch",
  "value": "${data.order_status}",
  "cases": [
    {
      "value": "pending",
      "children": [
        {
          "type": "TextBody",
          "text": "Your order is being processed"
        }
      ]
    },
    {
      "value": "shipped",
      "children": [
        {
          "type": "TextBody",
          "text": "Your order has shipped"
        }
      ]
    },
    {
      "value": "delivered",
      "children": [
        {
          "type": "TextBody",
          "text": "Your order has been delivered"
        }
      ]
    }
  ]
}
```

---

## If vs Switch

Use **If** for:
- Boolean conditions
- Comparisons (`>`, `<`, `==`)
- Logical operators (`&&`, `||`)
- Two-way branching (then/else)

Use **Switch** for:
- Multiple discrete values
- String matching
- Exhaustive cases
- Cleaner than nested If statements

---

## Conditional Inputs

Show/hide input fields based on selections:

```json
{
  "id": "ADDRESS_FORM",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "RadioButtonsGroup",
        "name": "address_type",
        "label": "Address Type",
        "data-source": {
          "type": "static",
          "values": ["Home", "Work", "Other"]
        },
        "required": true
      },
      {
        "type": "If",
        "condition": "${`${form.address_type} == 'Other'`}",
        "then": [
          {
            "type": "TextInput",
            "name": "other_type",
            "label": "Please specify",
            "required": true
          }
        ]
      },
      {
        "type": "TextInput",
        "name": "street",
        "label": "Street Address",
        "required": true
      },
      {
        "type": "Footer",
        "label": "Continue"
      }
    ]
  }
}
```

---

## Conditional Footer

Show/hide Footer based on form state:

**Important**: If Footer is inside If component, it must be in **both** then and else branches.

```json
{
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "Accept terms?"
      },
      {
        "type": "CheckboxGroup",
        "name": "accepted_terms",
        "data-source": {
          "type": "static",
          "values": ["I accept terms and conditions"]
        }
      },
      {
        "type": "If",
        "condition": "${form.accepted_terms}",
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
    ]
  }
}
```

---

## Nested Conditionals

Up to 3 levels of nesting allowed:

```json
{
  "type": "If",
  "condition": "${`${form.has_discount} == true`}",
  "then": [
    {
      "type": "TextBody",
      "text": "You have a discount code"
    },
    {
      "type": "If",
      "condition": "${`${form.discount_percent} > 20`}",
      "then": [
        {
          "type": "TextBody",
          "text": "Great! You have a premium discount (>20%)"
        }
      ],
      "else": [
        {
          "type": "TextBody",
          "text": "You have a standard discount (≤20%)"
        }
      ]
    }
  ]
}
```

**Limit**: Maximum 3 levels of nesting.

---

## Common Conditional Patterns

### Payment Method Selection

```json
{
  "id": "PAYMENT",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "RadioButtonsGroup",
        "name": "payment_method",
        "label": "Payment Method",
        "data-source": {
          "type": "static",
          "values": ["Credit Card", "PayPal", "Bank Transfer"]
        },
        "required": true
      },
      {
        "type": "Switch",
        "value": "${form.payment_method}",
        "cases": [
          {
            "value": "Credit Card",
            "children": [
              {
                "type": "TextInput",
                "name": "card_number",
                "label": "Card Number",
                "required": true
              }
            ]
          },
          {
            "value": "PayPal",
            "children": [
              {
                "type": "TextInput",
                "name": "paypal_email",
                "label": "PayPal Email",
                "input-type": "email",
                "required": true
              }
            ]
          },
          {
            "value": "Bank Transfer",
            "children": [
              {
                "type": "TextBody",
                "text": "Bank details will be sent via email"
              }
            ]
          }
        ]
      },
      {
        "type": "Footer",
        "label": "Pay Now"
      }
    ]
  }
}
```

### Age-Based Flow

```json
{
  "type": "If",
  "condition": "${`${form.age} < 18`}",
  "then": [
    {
      "type": "TextBody",
      "text": "You must be 18+ to proceed. Parental consent required."
    },
    {
      "type": "TextInput",
      "name": "parent_email",
      "label": "Parent/Guardian Email",
      "input-type": "email",
      "required": true
    }
  ],
  "else": [
    {
      "type": "TextBody",
      "text": "You can proceed directly"
    }
  ]
}
```

### Membership Status

```json
{
  "id": "MEMBERSHIP_CHECK",
  "data": {
    "type": "object",
    "properties": {
      "membership_status": {
        "type": "string",
        "__example__": "active"
      },
      "member_discount": {
        "type": "number",
        "__example__": 0.15
      }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "Switch",
        "value": "${data.membership_status}",
        "cases": [
          {
            "value": "active",
            "children": [
              {
                "type": "TextBody",
                "text": "Welcome back member! You get ${`${data.member_discount * 100}`}% off"
              }
            ]
          },
          {
            "value": "expired",
            "children": [
              {
                "type": "TextBody",
                "text": "Your membership has expired. Renew to get exclusive benefits"
              }
            ]
          },
          {
            "value": "inactive",
            "children": [
              {
                "type": "TextBody",
                "text": "Join our membership program for exclusive discounts"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

---

## Conditional Logic Rules

1. **Conditions are boolean expressions**
   - Simple: `${form.field_name}`
   - Comparison: `${`${form.age} >= 18`}`
   - Logical: `${`${a} && ${b}`}`

2. **Footer in conditionals**
   - Must appear in both then and else branches
   - Or place Footer outside conditional

3. **Nesting limits**
   - Maximum 3 levels deep
   - Count from outermost to innermost

4. **Dynamic data access**
   - Use `${data.field}` from screen data
   - Available after data_exchange

5. **Form field values**
   - Use `${form.field_name}` for user inputs
   - Available immediately after user input

---

## Best Practices

1. **Keep conditions simple** - Nested 3+ levels is hard to maintain
2. **Use Switch for multiple cases** - Cleaner than nested If
3. **Test all branches** - Ensure every condition is reachable
4. **Avoid complex nested expressions** - Keep expressions readable
5. **Comment complex logic** (if tool supports) - Explain why
6. **Default case in Switch** - Handle unexpected values
7. **Order cases logically** - Most common first
8. **Avoid circular logic** - Don't branch back to same state
9. **Validate server-side** - Never trust only client logic
10. **User-friendly messaging** - Explain why fields appear/disappear

---

## Debugging Conditional Logic

Common issues:

**Field not showing up**
- Check condition syntax (backticks for expressions)
- Verify field name matches (case-sensitive)
- Ensure previous field has value

**Wrong branch executing**
- Test condition values manually
- Check for typos in string matches (case-sensitive)
- Verify comparison operators (`==` not `=`)

**Footer not appearing**
- If Footer in If component, add to both then/else
- Check condition properly evaluates

---

## Next Steps

- Learn **nested expressions** in `11-nested-expressions.md`
- Learn **actions** in `13-actions.md`
- Learn **routing** in `15-routing-model.md`
