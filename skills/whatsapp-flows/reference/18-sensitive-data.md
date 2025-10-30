# Sensitive Data Handling (v5.1+)

Mark and protect sensitive information in WhatsApp Flows.

---

## Sensitive Field Declaration

Declare sensitive fields at screen level:

```json
{
  "id": "PASSWORD_ENTRY",
  "sensitive": ["password", "confirm_password"],
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextInput",
        "name": "password",
        "input-type": "password",
        "label": "Password"
      },
      {
        "type": "TextInput",
        "name": "confirm_password",
        "input-type": "password",
        "label": "Confirm Password"
      }
    ]
  }
}
```

---

## Sensitive Array Property

```json
{
  "sensitive": ["password", "ssn", "credit_card"]
}
```

- Array of field names that are sensitive
- Field names must match component `name` properties
- Applies to entire screen
- Case-sensitive

---

## Auto-Masked Fields

Some fields automatically masked regardless of `sensitive` array:

- `input-type: "password"` - Always masked
- `input-type: "passcode"` - Always masked
- PhotoPicker uploads - Hidden in responses
- DocumentPicker uploads - Hidden in responses

---

## Masking Behavior

When field marked sensitive:

```json
// In response summary:
{
  "password": "••••••••",
  "name": "John Doe",
  "ssn": "•••••••89"
}
```

Masked fields show as dots in:
- Flow completion response
- Server data_exchange responses
- User-facing confirmations

---

## What Gets Masked

| Data Type | Behavior |
|-----------|----------|
| Text fields | Show as `•••••••` |
| Password fields | Auto-masked |
| Passcode fields | Auto-masked |
| Media uploads | Hidden entirely |
| Other fields | Not masked |

---

## Sensitive Data Best Practices

1. **Mark all sensitive fields** - Passwords, SSNs, card numbers
2. **Use appropriate input types** - `password`, `passcode`
3. **Validate server-side** - Process sensitive data securely
4. **Don't send unnecessary data** - Only collect what you need
5. **Encrypt at rest** - Database encryption for sensitive data
6. **GDPR compliance** - Handle personal data properly
7. **Data retention** - Delete sensitive data after use
8. **Access control** - Limit who can view responses
9. **Audit logging** - Track access to sensitive data
10. **HTTPS only** - All communication encrypted

---

## Example: Secure Payment Form

```json
{
  "id": "PAYMENT_INFO",
  "sensitive": ["card_number", "cvv", "cardholder_name"],
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextInput",
        "name": "cardholder_name",
        "label": "Cardholder Name",
        "required": true
      },
      {
        "type": "TextInput",
        "name": "card_number",
        "label": "Card Number",
        "required": true,
        "max-length": 19
      },
      {
        "type": "TextInput",
        "name": "cvv",
        "input-type": "password",
        "label": "CVV",
        "required": true,
        "max-length": 4
      },
      {
        "type": "DatePicker",
        "name": "expiry",
        "label": "Expiry Date"
      },
      {
        "type": "Footer",
        "label": "Pay Securely"
      }
    ]
  }
}
```

Response summary:
```json
{
  "cardholder_name": "••••••••••",
  "card_number": "••••••••••••",
  "cvv": "•••",
  "expiry": "12/2025"  // Not marked sensitive
}
```

---

## Data Flow with Sensitive Fields

1. **User enters data** - Displayed normally on device
2. **Marked sensitive** - Flagged in screen definition
3. **Sent to server** - Raw data sent (encrypted via HTTPS)
4. **Server processes** - Business logic handles sensitive data
5. **Response returned** - Responses mask sensitive fields
6. **Completion summary** - Masked in responses to user

---

## Server-Side Handling

Servers should:

```python
# Receive sensitive data (raw, via HTTPS)
@app.route('/whatsapp/flow', methods=['POST'])
def handle_flow():
    data = request.json
    sensitive_field = data['data']['data']['password']  # Raw value

    # Process securely (hash, encrypt, validate)
    hashed = hash_password(sensitive_field)

    # Don't echo sensitive data back
    return jsonify({
        'version': '3.0',
        'screen': 'NEXT_SCREEN',
        'data': {
            # Don't include sensitive field in response
            'status': 'success'
        }
    })
```

Never echo sensitive data back in response.

---

## Common Sensitive Fields

- Passwords
- Social Security Numbers (SSN)
- Credit card numbers
- CVV codes
- PIN codes
- OTP codes
- API keys
- Authentication tokens
- Medical information
- Financial account details

---

## Next Steps

- Learn **version features** in `19-version-features.md`
- Learn **validation rules** in `17-validation-rules.md`
