# Rich Content & Advanced Text

RichText component and advanced markdown features.

---

## RichText Component (v5.1+)

Large formatted text with full markdown support.

**Properties:**
- `text` - Rich text with markdown (max 4096 chars)

### Basic RichText

```json
{
  "type": "RichText",
  "text": "# Welcome\n\nThis is **bold** and this is *italic*."
}
```

### Full Markdown Support

RichText supports comprehensive markdown:

```json
{
  "type": "RichText",
  "text": "# Heading 1\n\n## Heading 2\n\n### Heading 3\n\n**Bold text**\n\n*Italic text*\n\n~~Strikethrough~~ (v6.0+)\n\n`Inline code`\n\n```json\nCode block\n```\n\n> Blockquote\n\n---\n\n- Bullet point\n- Another point\n\n1. Numbered\n2. List\n\n[Link text](https://example.com)\n\n| Header 1 | Header 2 |\n|----------|----------|\n| Cell 1   | Cell 2   |\n| Cell 3   | Cell 4   |"
}
```

### Markdown Syntax Reference

| Element | Markdown | Result |
|---------|----------|--------|
| Heading 1 | `# Text` | Large heading |
| Heading 2 | `## Text` | Medium heading |
| Heading 3 | `### Text` | Small heading |
| Bold | `**text**` | **bold** |
| Italic | `*text*` | *italic* |
| Strikethrough | `~~text~~` | ~~strikethrough~~ (v6.0+) |
| Code | `` `code` `` | `monospace` |
| Code Block | `` ```\ncode\n``` `` | Formatted block |
| Line Break | `\n` | New line |
| Horizontal Rule | `---` or `***` | Divider |
| Bullet List | `- item` | • item |
| Numbered List | `1. item` | 1. item |
| Blockquote | `> text` | Indented quote |
| Link | `[text](url)` | Link reference |
| Table | Standard markdown | Data table |

---

## RichText Examples

### FAQ Section

```json
{
  "type": "RichText",
  "text": "# Frequently Asked Questions\n\n## How do I track my order?\n\nYou can track your order using the tracking number sent to your email.\n\n## What is your return policy?\n\n- 30-day returns\n- Free shipping on returns\n- Must be in original condition\n\n## How do I contact support?\n\n**Email:** support@example.com\n**Phone:** 1-800-SUPPORT\n**Hours:** Mon-Fri 9am-5pm EST"
}
```

### Order Details with Table

```json
{
  "type": "RichText",
  "text": "# Order Confirmation\n\n## Items\n\n| Item | Qty | Price |\n|------|-----|-------|\n| Widget A | 2 | $10.00 |\n| Widget B | 1 | $15.00 |\n\n**Subtotal:** $35.00\n**Shipping:** $5.00\n**Tax:** $3.20\n**Total:** $43.20\n\n---\n\nEstimated Delivery: 3-5 business days"
}
```

### Price Comparison

```json
{
  "type": "RichText",
  "text": "# Plan Comparison\n\n## Basic Plan\n- Up to 10 projects\n- Email support\n- **$9.99/month**\n\n## Pro Plan\n- Unlimited projects\n- Priority support\n- Advanced analytics\n- **$29.99/month** ← *Best Value*\n\n## Enterprise\n- Custom features\n- Dedicated support\n- Contact sales\n- **Custom pricing**"
}
```

---

## RichText vs TextBody

| Feature | RichText | TextBody |
|---------|----------|----------|
| Max chars | 4096 | 4096 |
| Markdown | Full | v5.1+ basic |
| Headers | h1, h2, h3 | Not supported |
| Tables | Yes | No |
| Code blocks | Yes | No |
| Strikethrough | Yes (v6.0+) | No |
| Visibility | Large, prominent | Normal size |
| Standalone (v5.1-v6.2) | Must be only component | Can combine with Footer |
| Combine with Footer (v6.3+) | Yes | Yes |

Use **RichText** for:
- Complex layouts with headers
- Data tables
- FAQ sections
- Detailed product descriptions
- Pricing comparisons

Use **TextBody** for:
- Regular paragraphs
- Instructions
- Confirmation messages
- Descriptive text

---

## RichText with Dynamic Data

Combine markdown with variables:

```json
{
  "type": "RichText",
  "text": "# Thank You, ${form.first_name}!\n\nYour order has been confirmed.\n\n## Order Summary\n\n**Order ID:** ${data.order_id}\n**Total:** ${data.currency} ${data.total_amount}\n**Estimated Delivery:** ${data.delivery_date}\n\nWe've sent a confirmation email to ${form.email}."
}
```

---

## Tables in RichText

Standard markdown table syntax:

```json
{
  "type": "RichText",
  "text": "| Product | Quantity | Price |\n|---------|----------|-------|\n| Item A  | 1        | $50   |\n| Item B  | 2        | $25   |\n| Item C  | 1        | $100  |\n\n**Total:** $200"
}
```

Limitations:
- Simple tables only
- No merged cells
- No cell formatting (bold, italic within cells)
- Alignment (`:---`, `:---:`) supported

---

## Lists in RichText

### Bullet Lists

```json
{
  "type": "RichText",
  "text": "## Features\n\n- Feature one\n- Feature two\n  - Sub-feature\n  - Another sub\n- Feature three"
}
```

### Numbered Lists

```json
{
  "type": "RichText",
  "text": "## Steps\n\n1. First step\n2. Second step\n   1. Sub-step\n   2. Another sub\n3. Third step"
}
```

### Mixed Lists

```json
{
  "type": "RichText",
  "text": "## Instructions\n\n1. Choose size\n   - Small\n   - Medium\n   - Large\n2. Select color\n3. Add to cart"
}
```

---

## Code in RichText

### Inline Code

```json
{
  "type": "RichText",
  "text": "Use the `API_KEY` environment variable to authenticate."
}
```

### Code Blocks

```json
{
  "type": "RichText",
  "text": "## Installation\n\nRun the following command:\n\n```bash\nnpm install my-package\n```"
}
```

---

## RichText Placement Rules

### v5.1 - v6.2
RichText must stand alone on screen:

```json
{
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "RichText",
        "text": "# Content"
      }
    ]
  }
}
```

**Cannot combine** with Footer or other components.

### v6.3+
RichText can combine with Footer:

```json
{
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "RichText",
        "text": "# Content"
      },
      {
        "type": "Footer",
        "label": "Continue"
      }
    ]
  }
}
```

Can also use in If/Switch conditional blocks.

---

## Markdown Escaping

Special markdown characters can be escaped with backslash:

```json
{
  "type": "RichText",
  "text": "Price is \\$50 (not $50 which would be strikethrough)\n\nThis is \\*not italic\\*"
}
```

---

## RichText Best Practices

1. **Use headers for structure** - Organize content logically
2. **Keep readable on mobile** - Short lines, clear hierarchy
3. **Use tables sparingly** - Best for 2-4 columns
4. **Format prices clearly** - Consistent currency format
5. **Escape special chars** - `$` can trigger unwanted formatting
6. **Test rendering** - Preview markdown before deploying
7. **Don't abuse formatting** - Bold/italic highlight, not everything
8. **Use blockquotes for emphasis** - Stands out visually
9. **Keep code blocks simple** - Short snippets only
10. **Combine with TextCaption** (v6.3+) - RichText + Caption for context

---

## Content Organization Patterns

### FAQ Screen

```json
{
  "type": "RichText",
  "text": "# Help Center\n\n## Account Questions\n\n### How do I reset my password?\nClick \"Forgot Password\" on login screen.\n\n### How do I change my email?\nGo to Settings > Account > Change Email.\n\n## Order Questions\n\n### Can I cancel my order?\nOnly if order hasn't shipped yet.\n\n### What's your return policy?\n30 days, full refund."
}
```

### Terms & Conditions

```json
{
  "type": "RichText",
  "text": "# Terms of Service\n\n## 1. Use License\n\nPermission is granted to temporarily download...\n\n## 2. Disclaimer\n\nThe materials are provided \"as is\"...\n\n## 3. Limitations\n\nIn no event shall our company be liable..."
}
```

---

## Next Steps

- Learn **navigation components** in `09-navigation-components.md`
- Learn **conditional logic** in `10-conditional-logic.md`
- Learn **actions** in `13-actions.md`
