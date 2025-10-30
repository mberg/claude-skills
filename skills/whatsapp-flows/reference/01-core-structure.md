# Core Flow JSON Structure

This is the fundamental structure every WhatsApp Flow must follow. Master this first, then learn specific components.

## Top-Level Flow Properties

Every Flow JSON has this structure:

```json
{
  "version": "7.1",
  "screens": [
    { "id": "SCREEN_1", "layout": { ... } },
    { "id": "SCREEN_2", "layout": { ... } }
  ]
}
```

### Required Properties

#### `version`
The Flow JSON schema version. Currently supported: `7.1`

```json
{ "version": "7.1" }
```

Newer versions introduce new components and features. Always verify component availability for your version.

#### `screens`
Array of screen definitions. Each screen represents a step in the flow.

```json
{
  "screens": [
    { "id": "SCREEN_1", ... },
    { "id": "SCREEN_2", ... }
  ]
}
```

Minimum: 1 screen (can be terminal). Maximum: Unlimited theoretically, but keep flows focused.

### Optional Top-Level Properties

#### `routing_model` *(Required when using Data Endpoint)*
Defines allowed screen transitions. Only needed if your flow exchanges data with a server endpoint.

```json
{
  "routing_model": {
    "SCREEN_1": ["SCREEN_2", "SCREEN_ERROR"],
    "SCREEN_2": ["SUCCESS"]
  }
}
```

See `15-routing-model.md` for detailed routing rules.

#### `data_api_version`
Specifies data endpoint API version. Required when using `routing_model`.

```json
{ "data_api_version": "3.0" }
```

Currently: `"3.0"`

---

## Screen Structure

Each screen is an object with layout and metadata:

```json
{
  "id": "WELCOME",
  "title": "Welcome to XYZ",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [ ... ]
  }
}
```

### Required Screen Properties

#### `id`
Unique identifier for this screen within the flow.

- Must be unique across all screens
- Alphanumeric and underscore only: `[a-zA-Z0-9_]`
- `SUCCESS` is reserved for terminal success screens
- Max length: 100 characters
- Used in routing, navigate actions, and global references

```json
{ "id": "USER_DETAILS" }
{ "id": "PAYMENT_PENDING" }
{ "id": "THANK_YOU" }
```

#### `layout`
Defines the visual layout and components on this screen.

```json
{
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      { "type": "TextHeading", "text": "Welcome" },
      { "type": "TextBody", "text": "Enter your details..." }
    ]
  }
}
```

### Optional Screen Properties

#### `terminal`
Boolean indicating this is an end state. Terminal screens:
- Must include a `Footer` component
- Only allowed action: `complete`
- May have `success: true/false` to indicate outcome

```json
{
  "id": "SUCCESS",
  "terminal": true,
  "success": true,
  "layout": { ... }
}
```

#### `success`
Used on terminal screens to indicate success (true) or failure (false) outcome.

```json
{ "id": "ORDER_CONFIRMED", "terminal": true, "success": true }
{ "id": "PAYMENT_FAILED", "terminal": true, "success": false }
```

#### `title`
Screen title shown in top navigation bar.

- Max 80 characters
- Optional, but recommended for clarity
- Shown to users as navigation context

```json
{ "title": "Shipping Address" }
```

#### `refresh_on_back`
Boolean (default: false). When true, triggers a `data_exchange` when user navigates back to this screen.

```json
{ "refresh_on_back": true }
```

Common use case: Refresh available products when returning from a detail screen.

#### `data`
Declares dynamic data structure for this screen using JSON Schema. Required if screen uses `${data.*}` variables.

```json
{
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
            "price": { "type": "number" }
          }
        },
        "__example__": [
          { "id": "001", "name": "Widget", "price": 9.99 }
        ]
      }
    }
  }
}
```

**Important**: Every dynamic field must have an `__example__` property for preview mode.

#### `sensitive` *(v5.1+)*
Array of field names that should be masked in responses.

```json
{
  "sensitive": ["password", "ssn", "credit_card"]
}
```

Marked fields will show as `••••••••` in response summaries. See `18-sensitive-data.md`.

---

## Layout Structure

Currently, only one layout type is supported:

### SingleColumnLayout

Vertical stack of components.

```json
{
  "type": "SingleColumnLayout",
  "children": [
    { "type": "TextHeading", "text": "Title" },
    { "type": "TextBody", "text": "Description" },
    { "type": "TextInput", "name": "email" },
    { "type": "Footer", "label": "Continue" }
  ]
}
```

**Properties:**
- `type`: Must be `"SingleColumnLayout"`
- `children`: Array of component objects (max 50 per screen)

**Component Order:**
- Components render top-to-bottom
- `Footer` must be last (for terminal screens)
- Text components typically come before inputs
- Input validation happens before actions

---

## Component Basics

All components share common properties:

### Universal Component Properties

```json
{
  "type": "TextInput",
  "name": "user_email",
  "label": "Email Address",
  "required": true
}
```

#### `type`
Component type. See specific component references for available types.

#### `name` *(usually required)*
Field identifier for form data. Used in `${form.field_name}` references.

#### `label` *(optional)*
Visible label for input components.

#### `required` *(optional)*
Boolean indicating if field must be filled before proceeding (default: false for most).

---

## Minimal Valid Flow

```json
{
  "version": "7.1",
  "screens": [
    {
      "id": "WELCOME",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextHeading",
            "text": "Welcome"
          },
          {
            "type": "Footer",
            "label": "Start"
          }
        ]
      }
    },
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
            "label": "Done"
          }
        ]
      }
    }
  ]
}
```

This is the simplest valid flow with two screens and no data collection.

---

## Common Patterns

### Multi-Step Form Flow

```json
{
  "version": "7.1",
  "screens": [
    {
      "id": "STEP_1_NAME",
      "title": "Your Name",
      "layout": { ... }
    },
    {
      "id": "STEP_2_EMAIL",
      "title": "Your Email",
      "layout": { ... }
    },
    {
      "id": "SUCCESS",
      "terminal": true,
      "success": true,
      "layout": { ... }
    }
  ]
}
```

### Flow With Optional Data Endpoint

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": {
    "SCREEN_1": ["SCREEN_2", "ERROR"],
    "SCREEN_2": ["SUCCESS"]
  },
  "screens": [ ... ]
}
```

When routing_model is present, the flow becomes stateful and can validate/process at the server.

---

## Next Steps

- Learn **data binding** in `02-data-model.md`
- Explore **components** in component-specific references
- Understand **actions** in `13-actions.md`
- Set up **routing** in `15-routing-model.md` when needed
