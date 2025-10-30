# Data Endpoints: Server Integration

Integrate WhatsApp Flows with your backend for dynamic, stateful experiences.

---

## When to Use Data Endpoints

Use when:
- Need to validate user input (email exists, age valid, etc.)
- Fetch dynamic data (products, categories, prices)
- Store form submissions in database
- Implement business logic server-side
- Track flow completion

Don't use when:
- Simple static flows
- No backend integration needed
- No dynamic data required

---

## Enabling Data Endpoints

Set required properties:

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": { ... },
  "screens": [ ... ]
}
```

Two properties enable endpoints:
1. `data_api_version: "3.0"` - API version (currently required)
2. `routing_model` - Defines allowed transitions

---

## Server Endpoint URL

Configure when creating flow (not in Flow JSON):

```bash
POST /api/flows/create
{
  "name": "My Flow",
  "flow_json": { ... },
  "data_channel_uri": "https://your-server.com/whatsapp/flow"
}
```

Server endpoint URL configured via Facebook Developers API, not in JSON.

---

## Endpoint Request Format

When user submits form (data_exchange action):

```json
{
  "flow_id": "abc123",
  "flow_token": "token123",
  "data": {
    "screen": "CURRENT_SCREEN",
    "data": {
      "field1": "value1",
      "field2": "value2"
    }
  }
}
```

---

## Endpoint Response Format

Server responds with next screen and data:

```json
{
  "version": "3.0",
  "screen": "NEXT_SCREEN",
  "data": {
    "field1": "response1",
    "field2": "response2"
  },
  "errors": {
    "field1": "Error message for field1"
  }
}
```

### Response Properties

- `screen` - Next screen to navigate to (from routing_model)
- `data` - Dynamic data for screen (matches screen's data schema)
- `errors` - Field errors (optional, shows validation errors)

---

## Example: Email Validation Endpoint

### Flow Definition

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": {
    "ENTER_EMAIL": ["EMAIL_VALID", "ERROR"],
    "EMAIL_VALID": ["SUCCESS"],
    "ERROR": []
  },
  "screens": [
    {
      "id": "ENTER_EMAIL",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextInput",
            "name": "email",
            "input-type": "email",
            "label": "Email Address",
            "required": true
          },
          {
            "type": "Footer",
            "label": "Validate",
            "on-click-action": {
              "action": "data_exchange",
              "payload": {
                "email": "${form.email}"
              }
            }
          }
        ]
      }
    },
    {
      "id": "EMAIL_VALID",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextHeading",
            "text": "Email Verified"
          },
          {
            "type": "Footer",
            "label": "Continue"
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
            "label": "Done",
            "on-click-action": {
              "action": "complete",
              "payload": { "status": "success" }
            }
          }
        ]
      }
    },
    {
      "id": "ERROR",
      "terminal": true,
      "success": false,
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Email validation failed"
          },
          {
            "type": "Footer",
            "label": "Back"
          }
        ]
      }
    }
  ]
}
```

### Server Implementation (Python)

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/whatsapp/flow', methods=['POST'])
def handle_flow():
    data = request.json
    screen = data['data']['screen']
    form_data = data['data']['data']

    if screen == 'ENTER_EMAIL':
        email = form_data.get('email', '')

        # Validate email format
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            return jsonify({
                'version': '3.0',
                'screen': 'ERROR',
                'errors': {
                    'email': 'Invalid email format'
                }
            })

        # Check if email exists in database
        if email_exists_in_db(email):
            return jsonify({
                'version': '3.0',
                'screen': 'ERROR',
                'errors': {
                    'email': 'Email already registered'
                }
            })

        # Email valid, proceed
        return jsonify({
            'version': '3.0',
            'screen': 'EMAIL_VALID',
            'data': {}
        })

    return jsonify({'version': '3.0', 'screen': 'ERROR'})

def email_exists_in_db(email):
    # Check your database
    return False
```

---

## Example: Dynamic Product List

### Flow Definition

```json
{
  "version": "7.1",
  "data_api_version": "3.0",
  "routing_model": {
    "CATEGORY": ["PRODUCTS", "ERROR"],
    "PRODUCTS": ["SUCCESS", "ERROR"]
  },
  "screens": [
    {
      "id": "CATEGORY",
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
          }
        ]
      }
    },
    {
      "id": "PRODUCTS",
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
              { "id": "P1", "name": "Widget", "price": 9.99 }
            ]
          }
        }
      },
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "Dropdown",
            "name": "product",
            "label": "Select Product",
            "data-source": {
              "type": "dynamic",
              "values": "${data.products}"
            }
          },
          {
            "type": "Footer",
            "label": "Order"
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
            "text": "Order Placed!"
          },
          {
            "type": "Footer",
            "label": "Done"
          }
        ]
      }
    },
    {
      "id": "ERROR",
      "terminal": true,
      "success": false,
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Error occurred"
          },
          {
            "type": "Footer",
            "label": "Try Again"
          }
        ]
      }
    }
  ]
}
```

### Server Implementation

```python
@app.route('/whatsapp/flow', methods=['POST'])
def handle_flow():
    data = request.json
    screen = data['data']['screen']
    form_data = data['data']['data']

    if screen == 'CATEGORY':
        category = form_data.get('category')

        # Get products from database
        products = get_products_by_category(category)

        return jsonify({
            'version': '3.0',
            'screen': 'PRODUCTS',
            'data': {
                'products': products
            }
        })

    return jsonify({'version': '3.0', 'screen': 'ERROR'})

def get_products_by_category(category):
    # Query database
    return [
        {'id': 'P1', 'name': 'Widget A', 'price': 19.99},
        {'id': 'P2', 'name': 'Widget B', 'price': 29.99}
    ]
```

---

## Error Handling

Return errors for validation failures:

```json
{
  "version": "3.0",
  "screen": "SAME_SCREEN",
  "errors": {
    "email": "Email is already registered",
    "phone": "Invalid phone format"
  }
}
```

- Stay on same screen
- Show field errors to user
- User corrects and retries

---

## Data Security

1. **Validate all input** - Never trust client data
2. **Use HTTPS only** - Encrypt in transit
3. **Authenticate requests** - Verify flow_token
4. **Rate limit** - Prevent abuse
5. **Sanitize data** - Prevent injection attacks
6. **Secure sensitive data** - Don't expose passwords, SSNs
7. **Log submissions** - For audit trail
8. **GDPR compliance** - Handle user data properly
9. **Timeout requests** - Long responses cause UX issues
10. **Monitor errors** - Track failed requests

---

## Best Practices

1. **Fast responses** - Keep endpoint latency < 1 second
2. **Meaningful errors** - Tell users what's wrong
3. **Validate comprehensively** - Check everything server-side
4. **Handle edge cases** - NULL, empty, invalid values
5. **Test thoroughly** - All paths, error scenarios
6. **Monitor performance** - Track endpoint metrics
7. **Version your API** - Support multiple flow versions
8. **Document clearly** - Help developers understand flow
9. **Rollback capability** - Be able to revert flows
10. **Audit logging** - Track all submissions

---

## Refresh on Back (refresh_on_back)

Optional property triggers data_exchange when user navigates back:

```json
{
  "id": "PRODUCT_DETAILS",
  "refresh_on_back": true,
  "layout": { ... }
}
```

When user goes back to PRODUCT_DETAILS, automatically fetch latest data from server.

Use case: Show updated stock count when returning from details screen.

---

## Next Steps

- Learn **validation rules** in `17-validation-rules.md`
- Learn **version features** in `19-version-features.md`
- See **examples** in `examples/` directory
