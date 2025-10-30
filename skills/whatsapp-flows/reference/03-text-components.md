# Text Components

Text components display information to users. They are the primary way to communicate instructions, confirmations, and feedback within flows.

---

## TextHeading

Large heading text, typically at the top of a screen.

**Properties:**
- `text` - Heading text (max 80 chars)
- `font-weight` - Optional: `regular` (default) or `bold`

```json
{
  "type": "TextHeading",
  "text": "Welcome to Our Service"
}
```

**Best practices:**
- Use for screen titles and main messages
- Keep concise and clear
- One per screen typical, occasionally two
- No markdown support

---

## TextSubheading

Secondary heading, smaller than TextHeading.

**Properties:**
- `text` - Subheading text (max 80 chars)

```json
{
  "type": "TextSubheading",
  "text": "Step 1 of 3"
}
```

**Usage:**
- Progress indicators
- Section labels
- Secondary titles

---

## TextBody

Body text for descriptions, instructions, and explanations.

**Properties:**
- `text` - Body text (max 4096 chars)
- `font-weight` - Optional: `regular` or `bold`

```json
{
  "type": "TextBody",
  "text": "Please enter your email address so we can send you a confirmation."
}
```

**v5.1+ Markdown Support:**
Supports markdown formatting for richer text:

```json
{
  "type": "TextBody",
  "text": "**Bold text** and *italic text* are supported.\n\n• List items\n• Another item\n\n1. Numbered\n2. Lists"
}
```

Markdown features:
- Bold: `**text**`
- Italic: `*text*`
- Line breaks: `\n`
- Bullet lists: `• item`
- Numbered lists: `1. item`

**Character limits:**
- Before v5.1: 4096 chars, plain text only
- v5.1+: 4096 chars, markdown supported

---

## TextCaption

Small caption text for supplementary information.

**Properties:**
- `text` - Caption text (max 409 chars)

```json
{
  "type": "TextCaption",
  "text": "Your information is secure and will not be shared."
}
```

**v5.1+ Markdown Support:**
Same markdown as TextBody.

```json
{
  "type": "TextCaption",
  "text": "Read our **[privacy policy](https://example.com/privacy)**"
}
```

**Usage:**
- Disclaimers
- Privacy notices
- Helper text
- Small supporting information

---

## RichText (v5.1+)

Large formatted text component with full markdown support. Preferred over TextBody when you need rich formatting.

**Properties:**
- `text` - Rich text with markdown (max 4096 chars)

```json
{
  "type": "RichText",
  "text": "# Main Title\n\nThis is a paragraph with **bold** and *italic* text.\n\n## Section\n\nBullet points:\n• Item one\n• Item two\n\nNumbered list:\n1. First\n2. Second\n\nTables are supported:\n| Col 1 | Col 2 |\n|-------|-------|\n| Data  | Data  |"
}
```

**Markdown features:**
- Headers: `# H1`, `## H2`, `### H3`
- Bold: `**text**`
- Italic: `*text*`
- Code: `` `code` ``
- Line breaks: `\n`
- Horizontal rule: `---`
- Lists (bullet and numbered)
- Tables: Standard markdown table syntax
- Links: `[text](url)` *(not clickable, reference only)*
- Blockquotes: `> text`
- Strikethrough: `~~text~~` (v6.0+)

**RichText vs TextBody:**
- RichText: Larger, more visible, full markdown
- TextBody: Smaller, basic markdown, good for body copy

**Placement rules (v5.1-v6.2):**
- RichText must stand alone on screen
- Cannot combine with Footer or other components

**Placement rules (v6.3+):**
- RichText can combine with Footer
- Can use in conditional If/Switch blocks

---

## Text Component Combinations

Typical screen layout with text:

```json
{
  "type": "SingleColumnLayout",
  "children": [
    {
      "type": "TextHeading",
      "text": "Order Confirmation"
    },
    {
      "type": "TextSubheading",
      "text": "Order #12345"
    },
    {
      "type": "TextBody",
      "text": "Your order has been confirmed. Estimated delivery: 3-5 business days."
    },
    {
      "type": "TextCaption",
      "text": "You can track your order in your account."
    },
    {
      "type": "Footer",
      "label": "Done"
    }
  ]
}
```

---

## Dynamic Text

All text components support data binding:

```json
{
  "type": "TextBody",
  "text": "Thank you, ${form.first_name}!"
}
```

Or from server data:

```json
{
  "type": "TextBody",
  "text": "Your balance is ${data.account_balance}"
}
```

---

## Character Limits Summary

| Component | Limit | Markdown | Notes |
|-----------|-------|----------|-------|
| TextHeading | 80 | No | Bold weight optional |
| TextSubheading | 80 | No | - |
| TextBody | 4096 | v5.1+ | Large body text |
| TextCaption | 409 | v5.1+ | Small supplementary |
| RichText | 4096 | Yes | v5.1+, full markdown |

---

## Best Practices

1. **Use clear hierarchy** - Heading → Body → Caption
2. **Be concise** - Long text overwhelms on mobile
3. **Use markdown sparingly** - Don't over-format
4. **Test dynamic content** - Ensure `${variable}` values fit character limits
5. **Consider line breaks** - `\n` helps readability
6. **Use TextCaption for disclaimers** - Smaller, less intrusive
7. **Choose RichText for complex layouts** - Tables, multiple sections
8. **Keep lists short** - 5-7 items max
9. **Avoid nested markdown** - Some markdown features don't nest
10. **Test with examples** - Use `__example__` values to preview

---

## Next Steps

- Learn **input components** in `04-input-components.md`
- Learn **selection components** in `05-selection-components.md`
- See examples in `examples/` directory
