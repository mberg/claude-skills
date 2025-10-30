# Routing Model: Server-Driven Flow Control (v4.0+)

Define allowed screen transitions for stateful flows with data endpoints.

---

## Routing Model Purpose

Specifies which screens can connect to which other screens. Used when:
- Flow exchanges data with server endpoint
- You want server to control valid transitions
- You need stateful flow with validation

---

## Routing Model Syntax

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": {
    "SCREEN_A": ["SCREEN_B", "ERROR"],
    "SCREEN_B": ["SCREEN_C", "ERROR"],
    "SCREEN_C": ["SUCCESS"]
  },
  "screens": [...]
}
```

- `routing_model` - Object mapping screen IDs to allowed next screens
- Each entry: `"SCREEN_ID": ["next_screen_1", "next_screen_2", ...]`
- Lists screens reachable from that screen

---

## Routing Rules

1. **Entry screen** - Screen with no inbound edges (typically SCREEN_A)
2. **Terminal screens** - `SUCCESS` and `ERROR` are reserved
3. **Forward only** - Routes go forward, back is automatic
4. **Max 10 branches** - Maximum 10 connections per screen
5. **No self-routes** - Can't route to same screen
6. **All paths end** - Every route leads to terminal

---

## Simple Routing Example

```json
{
  "routing_model": {
    "WELCOME": ["ENTER_EMAIL"],
    "ENTER_EMAIL": ["VERIFY_EMAIL", "ERROR"],
    "VERIFY_EMAIL": ["SUCCESS", "ERROR"],
    "ERROR": []
  }
}
```

Flow progression:
```
WELCOME → ENTER_EMAIL → VERIFY_EMAIL → SUCCESS (or ERROR)
                     → ERROR
```

---

## Complex Routing

Multiple paths based on business logic:

```json
{
  "routing_model": {
    "START": ["CHECK_ELIGIBILITY"],
    "CHECK_ELIGIBILITY": ["ELIGIBLE_PATH", "INELIGIBLE_PATH"],
    "ELIGIBLE_PATH": ["COLLECT_INFO"],
    "INELIGIBLE_PATH": ["EXPLAIN_INELIGIBLE"],
    "COLLECT_INFO": ["REVIEW", "ERROR"],
    "REVIEW": ["SUBMIT", "ERROR"],
    "SUBMIT": ["SUCCESS", "ERROR"],
    "EXPLAIN_INELIGIBLE": ["ERROR"],
    "ERROR": []
  }
}
```

---

## Reserved Screen IDs

- `SUCCESS` - Terminal success screen (must exist if used)
- `ERROR` - Terminal error screen (optional but recommended)

Both must be defined if referenced in routing_model.

---

## Routing Model Rules

1. **All screens referenced must exist** - No dangling references
2. **Entry screen must have inbound edges** - One screen starts flow
3. **Terminal screens have no outbound** - `SUCCESS` and `ERROR` end flow
4. **Routes match navigate actions** - Server validates transitions

---

## Example: E-Commerce Flow

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": {
    "PRODUCT_SELECTION": ["QUANTITY_INPUT", "ERROR"],
    "QUANTITY_INPUT": ["SHIPPING_ADDRESS", "ERROR"],
    "SHIPPING_ADDRESS": ["PAYMENT_INFO", "ERROR"],
    "PAYMENT_INFO": ["REVIEW_ORDER", "ERROR"],
    "REVIEW_ORDER": ["PROCESS_PAYMENT", "ERROR"],
    "PROCESS_PAYMENT": ["SUCCESS", "ERROR"],
    "ERROR": []
  },
  "screens": [
    {
      "id": "PRODUCT_SELECTION",
      "layout": { ... }
    },
    {
      "id": "QUANTITY_INPUT",
      "layout": { ... }
    },
    ...
    {
      "id": "SUCCESS",
      "terminal": true,
      "success": true,
      "layout": { ... }
    },
    {
      "id": "ERROR",
      "terminal": true,
      "success": false,
      "layout": { ... }
    }
  ]
}
```

---

## Routing with Conditional Logic

Server determines next screen based on data:

```json
{
  "routing_model": {
    "LOGIN": ["EXISTING_USER", "NEW_USER"],
    "EXISTING_USER": ["VERIFY_PASSWORD"],
    "NEW_USER": ["CREATE_PASSWORD"],
    "VERIFY_PASSWORD": ["SUCCESS", "ERROR"],
    "CREATE_PASSWORD": ["SUCCESS", "ERROR"]
  }
}
```

Server checks user in database, sends navigate to appropriate screen.

---

## Data Endpoint Integration

Routing requires server endpoint:

```json
{
  "data_api_version": "3.0",
  "routing_model": { ... }
}
```

When user submits (data_exchange action), server:
1. Receives payload
2. Validates data
3. Decides next screen
4. Returns response with navigate instruction

Server sends:
```json
{
  "next_screen": "NEXT_SCREEN_ID",
  "data": { ... }
}
```

---

## Validation Endpoints

Route to different screens based on validation:

```json
{
  "routing_model": {
    "COLLECT_EMAIL": ["VERIFY_EMAIL", "ERROR"],
    "VERIFY_EMAIL": ["SUCCESS", "RETRY_EMAIL"]
  }
}
```

- COLLECT_EMAIL → user enters email
- Server validates (exists, format, etc.)
- Route to VERIFY_EMAIL if valid
- Route to ERROR if invalid

---

## Multi-Outcome Flows

Different outcomes based on business logic:

```json
{
  "routing_model": {
    "LOAN_APPLICATION": ["INCOME_VERIFICATION", "ERROR"],
    "INCOME_VERIFICATION": ["APPROVED", "DENIED"],
    "APPROVED": ["SUCCESS"],
    "DENIED": ["EXPLAIN_DENIAL"]
  }
}
```

---

## When to Use Routing Model

### Use When:
- Flow integrates with data endpoint
- Server needs to control flow progression
- Multiple possible paths based on validation
- Complex business logic on server side
- Need stateful flow

### Don't Use When:
- Simple client-side flows (no endpoint)
- Fixed progression (no conditional routing)
- No server integration needed
- User always follows same path

---

## Without Routing Model

Simple flows don't need routing_model:

```json
{
  "version": "7.1",
  "screens": [
    {
      "id": "SCREEN_1",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "Footer",
            "label": "Next",
            "on-click-action": {
              "action": "navigate",
              "next_screen": "SCREEN_2"
            }
          }
        ]
      }
    },
    {
      "id": "SCREEN_2",
      "layout": { ... }
    }
  ]
}
```

No routing_model needed - navigation is hardcoded.

---

## Routing Model Best Practices

1. **Define all screens first** - Know complete flow before routing
2. **Map every transition** - Don't leave gaps
3. **Always have ERROR terminal** - Fallback for failures
4. **Validate server-side** - Routing doesn't validate, server does
5. **Clear screen names** - Routing reads better: `VERIFY_EMAIL` not `V_E`
6. **Document flow** - Draw diagram of routing paths
7. **Test all paths** - Ensure server routes correctly
8. **Limit branches** - Max 10 per screen, keep under 5 for simplicity
9. **Use meaningful next screens** - `APPROVED` better than `SCREEN_4`
10. **Server validation critical** - Never trust client-side routing

---

## Debugging Routing Issues

### Missing Routing
Error: Screen referenced in navigate but not in routing_model
- Add screen to routing_model
- Ensure screen exists

### Invalid Transition
Error: User tried navigate not in routing_model
- Server rejects invalid transitions
- Add valid path to routing_model

### Undefined Screen
Error: Routing_model references non-existent screen
- Create the screen in screens array
- Check spelling of screen ID

### No Entry Point
Error: All screens have inbound edges (circular)
- Identify entry screen (no inbound edges)
- Ensure at least one screen starts flow

---

## Next Steps

- Learn **data endpoints** in `16-data-endpoints.md`
- Learn **validation** in `17-validation-rules.md`
- See **examples** in `examples/` directory
