# Actions: navigate, data_exchange, complete, update_data, open_url

What happens when users interact with components.

---

## Overview of Actions

| Action | Purpose | Components | v6.0+ |
|--------|---------|-----------|-------|
| `navigate` | Move to another screen | Footer, EmbeddedLink, OptIn, selections | Base |
| `data_exchange` | Send/receive data from server | Footer, components, any | Base |
| `complete` | End flow with response | Footer (terminal screens) | Base |
| `update_data` | Update screen state | Footer, selections | v6.0+ |
| `open_url` | Open external link | EmbeddedLink, OptIn | v6.0+ |

---

## Navigate Action

Move to another screen in the flow.

```json
{
  "action": "navigate",
  "next_screen": "SCREEN_ID"
}
```

### Basic Navigate

```json
{
  "type": "Footer",
  "label": "Continue",
  "on-click-action": {
    "action": "navigate",
    "next_screen": "NEXT_SCREEN"
  }
}
```

### Navigate with Payload (Legacy)

Pass data to next screen:

```json
{
  "action": "navigate",
  "next_screen": "CONFIRMATION",
  "payload": {
    "product_id": "${form.selected_product}",
    "quantity": "${form.quantity}"
  }
}
```

**Modern approach**: Use global references instead of payload.

### Navigate Rules

- `next_screen` must exist in flow
- `next_screen` cannot be current screen (no self-navigation)
- Use routing_model if using data_api_version (v4.0+)
- Can navigate to any screen (no required sequence)

---

## Data Exchange Action

Send data to server endpoint and receive response.

```json
{
  "action": "data_exchange",
  "payload": {
    "field1": "${form.field1}",
    "field2": "${form.field2}"
  }
}
```

### Basic Data Exchange

```json
{
  "type": "Footer",
  "label": "Submit",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "email": "${form.email}",
      "message": "${form.message}"
    }
  }
}
```

Server receives JSON, processes, returns response matching screen's `data` schema.

### Data Exchange with Validation

```json
{
  "type": "Footer",
  "label": "Check Availability",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "email": "${form.email}",
      "check_type": "registration"
    }
  }
}
```

Server validates, returns:
```json
{
  "available": true,
  "message": "Email is available"
}
```

Component updates based on response.

### Data Exchange from Selections

Selection components can trigger data_exchange directly:

```json
{
  "type": "Dropdown",
  "name": "category",
  "label": "Category",
  "data-source": { "type": "static", "values": ["A", "B"] },
  "on-select-action": {
    "action": "data_exchange",
    "payload": { "category": "${form.category}" }
  }
}
```

---

## Complete Action

End the flow and return data to caller.

```json
{
  "action": "complete",
  "payload": {
    "status": "success",
    "user_email": "${form.email}",
    "order_id": "${data.order_id}"
  }
}
```

### Complete on Terminal Screen

Must be used on terminal screens (screens with `terminal: true`):

```json
{
  "id": "SUCCESS",
  "terminal": true,
  "success": true,
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Thank You!"
      },
      {
        "type": "Footer",
        "label": "Done",
        "on-click-action": {
          "action": "complete",
          "payload": {
            "order_id": "${data.order_id}"
          }
        }
      }
    ]
  }
}
```

### Payload in Complete

Include any data to return to caller:

```json
{
  "action": "complete",
  "payload": {
    "user_email": "${form.email}",
    "preferences": "${form.preferences}",
    "timestamp": "${data.completion_time}"
  }
}
```

Caller receives this data in response.

---

## Update Data Action (v6.0+)

Update screen state without navigating away. Useful for dynamic forms.

```json
{
  "action": "update_data",
  "payload": {
    "field1": "new_value",
    "field2": "another_value"
  }
}
```

### Update Selection Results

Dropdown selections can update data without navigation:

```json
{
  "type": "Dropdown",
  "name": "category",
  "label": "Category",
  "data-source": {
    "type": "static",
    "values": ["Electronics", "Clothing"]
  },
  "on-select-action": {
    "action": "update_data",
    "payload": {
      "selected_category": "${form.category}"
    }
  }
}
```

### Update with Server Call

Combination of data_exchange and local state:

```json
{
  "type": "Footer",
  "label": "Recalculate",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "quantity": "${form.quantity}",
      "unit_price": "${data.unit_price}"
    }
  }
}
```

Server returns updated data, component refreshes.

---

## Open URL Action (v6.0+)

Open external link (opens in browser).

```json
{
  "action": "open_url",
  "url": "https://example.com/terms"
}
```

### EmbeddedLink Opening URL

```json
{
  "type": "EmbeddedLink",
  "text": "Read Terms",
  "on-click-action": {
    "action": "open_url",
    "url": "https://example.com/terms"
  }
}
```

### OptIn with URL

```json
{
  "type": "OptIn",
  "name": "accept_terms",
  "label": "I accept the terms",
  "action-url": "https://example.com/terms",
  "action-text": "View Terms"
}
```

### Dynamic URLs

```json
{
  "type": "EmbeddedLink",
  "text": "View Order",
  "on-click-action": {
    "action": "open_url",
    "url": "https://example.com/orders/${form.order_id}"
  }
}
```

---

## Action Support by Component

| Component | navigate | data_exchange | complete | update_data | open_url |
|-----------|----------|---------------|----------|-------------|----------|
| Footer | ✓ | ✓ | ✓ | ✓ | ✗ |
| EmbeddedLink | ✓ | ✓ | ✗ | ✗ | ✓ |
| OptIn | ✓ | ✓ | ✗ | ✗ | ✓ |
| DatePicker | ✗ | ✓ | ✗ | ✗ | ✗ |
| Dropdown | ✓ (implicit) | ✓ | ✗ | ✓ | ✗ |
| RadioButtons | ✓ (implicit) | ✓ | ✗ | ✓ | ✗ |
| CheckboxGroup | ✓ (implicit) | ✓ | ✗ | ✓ | ✗ |
| ChipsSelector | ✓ (v6.3+) | ✓ | ✗ | ✓ (v7.1+) | ✗ |
| NavigationList | ✓ | ✓ | ✗ | ✗ | ✗ |

---

## Common Action Patterns

### Form Submission

```json
{
  "type": "Footer",
  "label": "Submit",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "name": "${form.name}",
      "email": "${form.email}",
      "message": "${form.message}"
    }
  }
}
```

Server validates, navigates to next screen or shows error.

### Multi-Step Flow

```json
{
  "type": "Footer",
  "label": "Next",
  "on-click-action": {
    "action": "navigate",
    "next_screen": "STEP_2"
  }
}
```

### Conditional Navigation

```json
{
  "type": "If",
  "condition": "${`${form.has_account} == true`}",
  "then": [
    {
      "type": "Footer",
      "label": "Login",
      "on-click-action": {
        "action": "navigate",
        "next_screen": "LOGIN"
      }
    }
  ],
  "else": [
    {
      "type": "Footer",
      "label": "Register",
      "on-click-action": {
        "action": "navigate",
        "next_screen": "REGISTER"
      }
    }
  ]
}
```

---

## Action Constraints

1. **Complete action only on terminal screens** - Don't use elsewhere
2. **Navigate target must exist** - References non-existent screen → error
3. **Data exchange requires endpoint** - Server must handle payload
4. **Update data on same screen** - Don't navigate elsewhere
5. **Open URL requires HTTPS** - No insecure links
6. **Payload is JSON** - Use proper structure
7. **Navigation creates new context** - Previous screen state persists
8. **Complete is final** - No more screens after complete

---

## Best Practices

1. **Validate server-side** - Never trust client validation
2. **Use navigate for progression** - Clear screen transitions
3. **Use data_exchange for validation** - Check email exists, etc.
4. **Use complete with payload** - Return all necessary data
5. **Handle errors gracefully** - Show retry option
6. **Clear button labels** - "Submit", "Next", "Cancel"
7. **Provide feedback** - Users know action completed
8. **Test all paths** - Navigate, data_exchange, complete
9. **Avoid back navigation** - WhatsApp handles it
10. **Keep payloads small** - Don't send unnecessary data

---

## Next Steps

- Learn **routing models** in `15-routing-model.md`
- Learn **server integration** in `16-data-endpoints.md`
- Learn **validation** in `17-validation-rules.md`
