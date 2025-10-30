# Navigation Components

Advanced components for navigation and selection with richer UI.

---

## NavigationList (v6.2+)

Rich navigation list for selecting from items with descriptions and detail.

**Properties:**
- `name` - Field identifier (required)
- `data-source` - List items (static or dynamic)
- `on-select-action` - Action when item selected (navigate or data_exchange)

### Basic NavigationList

```json
{
  "type": "NavigationList",
  "name": "selected_option",
  "data-source": {
    "type": "static",
    "values": [
      {
        "id": "option1",
        "title": "Option One",
        "description": "Description of option 1"
      },
      {
        "id": "option2",
        "title": "Option Two",
        "description": "Description of option 2"
      }
    ]
  },
  "on-select-action": {
    "action": "navigate",
    "next_screen": "NEXT_SCREEN"
  }
}
```

### NavigationList with Images

```json
{
  "type": "NavigationList",
  "name": "category",
  "data-source": {
    "type": "dynamic",
    "values": "${data.categories}"
  }
}
```

Server provides:
```json
{
  "categories": [
    {
      "id": "electronics",
      "title": "Electronics",
      "description": "Phones, laptops, accessories",
      "image": "https://example.com/electronics.jpg"
    },
    {
      "id": "clothing",
      "title": "Clothing",
      "description": "Apparel and accessories",
      "image": "https://example.com/clothing.jpg"
    }
  ]
}
```

Items display with thumbnail images.

### NavigationList Structure

Each item in `values` array:

```json
{
  "id": "unique_id",
  "title": "Display Title",
  "description": "Longer description text",
  "image": "https://example.com/image.jpg"  // optional
}
```

Properties:
- `id` - Unique identifier
- `title` - Display title (required)
- `description` - Subtitle/description text
- `image` - URL to thumbnail (optional)

### NavigationList Form Value

Selected item ID:

```json
${form.category}  // "electronics"
```

### NavigationList Constraints

- Minimum 1 item, maximum 20 items
- Cannot be on terminal screen
- Maximum 2 per screen
- Cannot combine with other major components on same screen
- Cannot trigger action before selection (must select, then action)

### NavigationList Use Cases

- Category/section selection
- Service tier comparison
- Multi-step form with clear options
- Product type selection
- Account tier choice

---

## ChipsSelector (v6.3+)

Multi-select chips component (buttons for easy selection).

**Properties:**
- `name` - Field identifier (required)
- `data-source` - Chip options (static or dynamic)
- `on-select-action` - Optional action on selection
- `on-unselect-action` - Optional action on deselection (v7.1+)

### Basic ChipsSelector

```json
{
  "type": "ChipsSelector",
  "name": "interests",
  "data-source": {
    "type": "static",
    "values": [
      "Sports",
      "Music",
      "Travel",
      "Food",
      "Technology"
    ]
  }
}
```

### ChipsSelector with Images

```json
{
  "type": "ChipsSelector",
  "name": "payment_method",
  "data-source": {
    "type": "dynamic",
    "values": "${data.payment_methods}"
  }
}
```

Server provides:
```json
{
  "payment_methods": [
    {
      "id": "credit_card",
      "title": "Credit Card",
      "image": "https://example.com/cc.jpg"
    },
    {
      "id": "paypal",
      "title": "PayPal",
      "image": "https://example.com/paypal.jpg"
    }
  ]
}
```

### ChipsSelector Form Value

Selected chips as array:

```json
${form.interests}  // ["Sports", "Music"]
```

### ChipsSelector Constraints

- Minimum 2 options, maximum 20 options
- Multiple selection allowed
- Chips display inline (wraps on small screens)
- v6.3+: `on-select-action` support
- v7.1+: `on-unselect-action` support

### ChipsSelector with Actions

Trigger action on selection:

```json
{
  "type": "ChipsSelector",
  "name": "filter",
  "data-source": {
    "type": "static",
    "values": ["All", "Available", "Sale"]
  },
  "on-select-action": {
    "action": "data_exchange",
    "payload": {
      "filter": "${form.filter}"
    }
  }
}
```

---

## EmbeddedLink

Clickable link within content (not a standalone button).

**Properties:**
- `text` - Link text (max 25 chars)
- `link` - URL or action
- `on-click-action` - Action when clicked (navigate, data_exchange, open_url)

### Basic EmbeddedLink

```json
{
  "type": "EmbeddedLink",
  "text": "Learn more",
  "on-click-action": {
    "action": "open_url",
    "url": "https://example.com/details"
  }
}
```

### EmbeddedLink in Text Context

EmbeddedLink used near text for clarity:

```json
{
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextBody",
        "text": "By continuing, you agree to our"
      },
      {
        "type": "EmbeddedLink",
        "text": "Terms of Service",
        "on-click-action": {
          "action": "open_url",
          "url": "https://example.com/terms"
        }
      },
      {
        "type": "TextBody",
        "text": "and"
      },
      {
        "type": "EmbeddedLink",
        "text": "Privacy Policy",
        "on-click-action": {
          "action": "open_url",
          "url": "https://example.com/privacy"
        }
      }
    ]
  }
}
```

### EmbeddedLink Actions

```json
{
  "type": "EmbeddedLink",
  "text": "Continue",
  "on-click-action": {
    "action": "navigate",
    "next_screen": "NEXT_STEP"
  }
}
```

Or with data exchange:

```json
{
  "type": "EmbeddedLink",
  "text": "View details",
  "on-click-action": {
    "action": "data_exchange",
    "payload": { "view_type": "details" }
  }
}
```

### EmbeddedLink Constraints

- Maximum 2 per screen
- Text max 25 characters
- Cannot be primary action (use Footer for primary)
- Good for secondary actions and links

---

## Comparing Navigation Components

| Component | Selection | Limit | Use Case |
|-----------|-----------|-------|----------|
| NavigationList | Single | 20 items | Rich items with descriptions/images |
| ChipsSelector | Multiple | 20 options | Tag-like selection, filtering |
| EmbeddedLink | N/A | 2 per screen | Secondary links, terms/privacy |
| Dropdown | Single | 200 items | Long lists, space-constrained |
| RadioButtons | Single | 20 options | Simple required choice |

---

## NavigationList vs Dropdown vs RadioButtons

Choose based on:

- **NavigationList**: Complex items with descriptions/images, small lists
- **Dropdown**: Long lists (50+ items), space-constrained, simple options
- **RadioButtons**: Simple choices, 5-7 options, standard UI

Example decision:
```
"Which service tier?"
→ NavigationList (3 tiers with features)

"Select a product"
→ Dropdown (100+ products)

"Which color?"
→ RadioButtons or ChipsSelector (5-6 colors)
```

---

## ChipsSelector vs CheckboxGroup

| Feature | ChipsSelector | CheckboxGroup |
|---------|---------------|---------------|
| Appearance | Button-like chips | Checkboxes |
| Max items | 20 | 20 |
| Mobile UX | Better (button targets) | Standard |
| Images supported | Yes (v6.3+) | No |
| Min items | 2 | 1 |
| Version | v6.3+ | v4.0+ |
| Use case | Tags, filters | Checkboxes |

---

## Best Practices

### NavigationList
1. **Use for distinct choices** - Service tiers, account types
2. **Include descriptive text** - Help users make informed choice
3. **Add images when helpful** - Category icons, product photos
4. **Limit to 10 items** - More becomes overwhelming
5. **One per screen** when possible - NavigationList is prominent

### ChipsSelector
1. **Good for filters** - Multiple selections, visual feedback
2. **Use for 5-15 items** - Beyond that, consider list
3. **Show selected state clearly** - Chips should highlight when selected
4. **Group related chips** - Related interests together
5. **Quick interactions** - Trigger actions on selection

### EmbeddedLink
1. **Use sparingly** - 1-2 per screen max
2. **Clear link text** - "Read terms" not "Click here"
3. **Secondary actions** - Not primary user flow
4. **Consistent styling** - Look like links (typically blue)
5. **Open URLs in new context** - Not primary navigation

---

## Navigation Patterns

### Service Tier Selection

```json
{
  "id": "CHOOSE_PLAN",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Choose Your Plan"
      },
      {
        "type": "NavigationList",
        "name": "selected_plan",
        "data-source": {
          "type": "dynamic",
          "values": "${data.plans}"
        },
        "on-select-action": {
          "action": "navigate",
          "next_screen": "PLAN_DETAILS"
        }
      }
    ]
  }
}
```

### Filtering with ChipsSelector

```json
{
  "id": "FILTER_RESULTS",
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextHeading",
        "text": "Filter Results"
      },
      {
        "type": "ChipsSelector",
        "name": "categories",
        "data-source": {
          "type": "static",
          "values": ["Electronics", "Books", "Clothing", "Food"]
        },
        "on-select-action": {
          "action": "data_exchange",
          "payload": { "filter": "${form.categories}" }
        }
      }
    ]
  }
}
```

---

## Next Steps

- Learn **conditional logic** in `10-conditional-logic.md`
- Learn **nested expressions** in `11-nested-expressions.md`
- Learn **actions** in `13-actions.md`
