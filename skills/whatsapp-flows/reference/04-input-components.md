# Input Components: TextInput & TextArea

Simple text input components for collecting user information.

---

## TextInput

Single-line text entry field.

**Properties:**
- `name` - Field identifier (required, used in `${form.name}`)
- `label` - Visible label (optional)
- `input-type` - Type of input (default: `text`)
- `placeholder` - Placeholder text when empty
- `required` - Boolean, must be filled (default: false)
- `init-value` - Initial value when screen loads
- `max-length` - Maximum characters (default: 80)
- `error-message` - Custom error text if validation fails
- `pattern` - Regex for validation (v6.2+)

### Input Types

```json
{
  "type": "TextInput",
  "name": "email",
  "input-type": "email",
  "label": "Email Address",
  "required": true
}
```

Available input types:
- `text` - Plain text (default)
- `number` - Numeric input only
- `email` - Email validation
- `password` - Masked text input
- `passcode` - Numeric, masked (e.g., PIN)
- `phone` - Phone number format
- `date` - Date picker (YYYY-MM-DD)

### Basic TextInput Examples

**Email collection:**
```json
{
  "type": "TextInput",
  "name": "email",
  "input-type": "email",
  "label": "Email",
  "required": true,
  "placeholder": "user@example.com"
}
```

**Phone number:**
```json
{
  "type": "TextInput",
  "name": "phone",
  "input-type": "phone",
  "label": "Phone Number",
  "required": true
}
```

**Password:**
```json
{
  "type": "TextInput",
  "name": "password",
  "input-type": "password",
  "label": "Password",
  "required": true,
  "error-message": "Password must be at least 8 characters"
}
```

### Validation

#### Built-in Validation

Input types have built-in validation:
- `email` - Validates email format
- `number` - Validates numeric format
- `phone` - Validates phone format
- `date` - Validates date format (YYYY-MM-DD)

#### Custom Validation with Pattern (v6.2+)

Use regex patterns for custom validation:

```json
{
  "type": "TextInput",
  "name": "username",
  "label": "Username",
  "pattern": "^[a-zA-Z0-9_]{3,20}$",
  "error-message": "Username must be 3-20 alphanumeric characters"
}
```

Common patterns:
- Alphanumeric only: `^[a-zA-Z0-9]+$`
- 3-20 chars: `.{3,20}`
- Uppercase and number: `(?=.*[A-Z])(?=.*[0-9])`
- No special chars: `^[^!@#$%^&*()_+=\-\[\]{};':"\\|,.<>\/?]+$`

#### Validation at Action

Validate before submission using nested expressions:

```json
{
  "type": "Footer",
  "label": "Continue",
  "on-click-action": {
    "action": "data_exchange",
    "payload": {
      "email": "${form.email}",
      "valid": "${`${form.email}`.includes('@')}"
    }
  }
}
```

### Initial Values

Set default values when screen loads:

```json
{
  "type": "TextInput",
  "name": "country",
  "label": "Country",
  "init-value": "United States"
}
```

Or from dynamic data:

```json
{
  "type": "TextInput",
  "name": "default_email",
  "label": "Email",
  "init-value": "${data.user_email}"
}
```

### Character Limits

- Default max length: 80 characters
- Can increase with `max-length` property
- Phone/email have format limits regardless of max-length

```json
{
  "type": "TextInput",
  "name": "notes",
  "label": "Notes",
  "max-length": 200
}
```

---

## TextArea

Multi-line text entry field.

**Properties:**
- `name` - Field identifier (required)
- `label` - Visible label (optional)
- `placeholder` - Placeholder text
- `required` - Boolean, must be filled (default: false)
- `init-value` - Initial value
- `max-length` - Maximum characters (default: 600)

### TextArea Examples

**Feedback collection:**
```json
{
  "type": "TextArea",
  "name": "feedback",
  "label": "How can we improve?",
  "placeholder": "Please tell us your thoughts...",
  "max-length": 500
}
```

**Long-form input:**
```json
{
  "type": "TextArea",
  "name": "description",
  "label": "Product Description",
  "required": true,
  "max-length": 1000
}
```

---

## Input with Dynamic Placeholder

Show different placeholders based on data:

```json
{
  "type": "TextInput",
  "name": "amount",
  "input-type": "number",
  "label": "Amount (${data.currency})",
  "placeholder": "e.g., ${data.min_amount} - ${data.max_amount}"
}
```

---

## Input with Error Handling

Set custom error messages for validation failures:

```json
{
  "type": "TextInput",
  "name": "age",
  "input-type": "number",
  "label": "Age",
  "error-message": "Please enter a valid age (18+)",
  "pattern": "^([1-9][0-9]|[1-9][0-9]{2,})$"
}
```

---

## Combining Inputs

Typical form with multiple inputs:

```json
{
  "type": "SingleColumnLayout",
  "children": [
    {
      "type": "TextHeading",
      "text": "Registration"
    },
    {
      "type": "TextInput",
      "name": "first_name",
      "label": "First Name",
      "required": true
    },
    {
      "type": "TextInput",
      "name": "last_name",
      "label": "Last Name",
      "required": true
    },
    {
      "type": "TextInput",
      "name": "email",
      "input-type": "email",
      "label": "Email",
      "required": true
    },
    {
      "type": "TextInput",
      "name": "password",
      "input-type": "password",
      "label": "Password",
      "required": true
    },
    {
      "type": "TextArea",
      "name": "about",
      "label": "About Yourself",
      "max-length": 200
    },
    {
      "type": "Footer",
      "label": "Create Account"
    }
  ]
}
```

---

## Validation Flow

When user submits form:

1. **Client-side validation** checks:
   - Required fields are filled
   - Format is correct (email, phone, etc.)
   - Pattern regex matches (if specified)
   - Max length not exceeded

2. **Action triggered** (navigate, data_exchange, etc.)

3. **Server validation** (if data_exchange):
   - Double-check values
   - Check for duplicates
   - Verify against business rules

---

## Best Practices

1. **Use appropriate input types** - `email` for emails, `phone` for phones
2. **Set required on critical fields** - Don't require nice-to-have data
3. **Provide clear labels** - "Email Address" not "Email"
4. **Use helpful placeholders** - Show format: "MM/DD/YYYY"
5. **Limit max-length** - TextArea up to 600, TextInput 80 default
6. **Add error messages** - Tell users why input failed
7. **Use patterns sparingly** - Only for complex validation
8. **Set init-values when appropriate** - Pre-fill known data
9. **Keep forms short** - 5-7 fields per screen max
10. **Validate server-side** - Never trust only client validation

---

## Common Patterns

### Email Verification Flow
```json
{
  "id": "ENTER_EMAIL",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Verify Your Email"
      },
      {
        "type": "TextInput",
        "name": "email",
        "input-type": "email",
        "required": true
      },
      {
        "type": "Footer",
        "label": "Send Code",
        "on-click-action": {
          "action": "data_exchange",
          "payload": { "email": "${form.email}" }
        }
      }
    ]
  }
}
```

### Password Change
```json
{
  "type": "TextInput",
  "name": "new_password",
  "input-type": "password",
  "label": "New Password",
  "error-message": "Password must be 8+ characters, with uppercase and number"
}
```

---

## Next Steps

- Learn **selection components** in `05-selection-components.md`
- Learn **date/time components** in `06-date-time-components.md`
- Learn **validation and actions** in `13-actions.md`
