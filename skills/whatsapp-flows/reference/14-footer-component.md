# Footer Component

The primary action button component. Appears at bottom of screen.

---

## Basic Footer

```json
{
  "type": "Footer",
  "label": "Continue"
}
```

---

## Footer Properties

- `label` - Button text (required, max 30 chars)
- `on-click-action` - Action when clicked (required for non-terminal screens)
- `enabled` - Boolean, enable/disable button (default: true)

---

## Footer with Action

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

---

## Footer on Terminal Screens

Terminal screens must have Footer with complete action:

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
            "status": "success"
          }
        }
      }
    ]
  }
}
```

---

## Disabling Footer

Conditionally disable based on form state:

```json
{
  "type": "If",
  "condition": "${form.agree_to_terms}",
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

---

## Footer Rules

1. **One Footer per screen** - Max one
2. **Last component** - Must be final child in layout
3. **Terminal screens require Footer** - Mandatory for terminal
4. **Button in If/Switch** - Must appear in all branches
5. **Max 30 character label** - Truncated if longer
6. **Always clickable** - Users can always tap (unless disabled)

---

## Footer Best Practices

1. **Clear action label** - "Continue", "Submit", "Confirm"
2. **Use active verbs** - "Next" not "Proceed to Next"
3. **Avoid capitalization** - "Submit form" not "SUBMIT FORM"
4. **Single action per button** - Don't overload
5. **Provide feedback** - Show what happens on click
6. **Disable when invalid** - Use conditional logic
7. **Test on mobile** - Ensure tap target is large enough
8. **Consistent labels** - Use "Continue" throughout, not "Next"
9. **Optional vs required** - Make clear if step can be skipped
10. **Cancel options** - Provide way to go back (handled by WhatsApp)

---

## Next Steps

- Learn **routing models** in `15-routing-model.md`
- Learn **server integration** in `16-data-endpoints.md`
