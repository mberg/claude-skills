# Nested Expressions (v6.0+)

Advanced calculations and string operations within Flow JSON using backtick syntax.

---

## Expression Syntax

Nested expressions are wrapped in backticks and evaluate at runtime:

```json
${`expression here`}
```

**Examples:**
```json
${`${form.age} >= 18`}
${`${form.quantity} * ${data.unit_price}`}
${`${form.first_name} + ' ' + ${form.last_name}`}
```

---

## Supported Operations

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `${`${form.country} == 'USA'`}` |
| `!=` | Not equal | `${`${form.status} != 'pending'`}` |
| `<` | Less than | `${`${form.age} < 18`}` |
| `<=` | Less than or equal | `${`${form.age} <= 65`}` |
| `>` | Greater than | `${`${form.age} > 18`}` |
| `>=` | Greater than or equal | `${`${form.balance} >= 100`}` |

### Logical Operators

```json
${`${form.age} >= 18 && ${form.has_license} == true`}
${`${form.country} == 'USA' || ${form.country} == 'Canada'`}
${`!(${form.is_blocked})`}
```

| Operator | Meaning | Example |
|----------|---------|---------|
| `&&` | AND | Both conditions true |
| `\|\|` | OR | Either condition true |
| `!` | NOT | Inverts boolean |

### Math Operators

```json
${`${form.quantity} * ${data.unit_price}`}
${`${form.subtotal} + ${data.tax}`}
${`${data.total} - ${form.discount}`}
${`${form.distance} / ${data.speed}`}
${`${form.number} % 2`}
```

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `${`10 + 5`}` → 15 |
| `-` | Subtraction | `${`20 - 8`}` → 12 |
| `*` | Multiplication | `${`4 * 5`}` → 20 |
| `/` | Division | `${`100 / 4`}` → 25 |
| `%` | Modulo (remainder) | `${`10 % 3`}` → 1 |

### String Concatenation

```json
${`${form.first_name} + ' ' + ${form.last_name}`}
${`'Total: $' + ${data.amount}`}
${`'Order #' + ${data.order_id}`}
```

Use `+` operator for string concatenation (not `.concat()`).

---

## Common Use Cases

### Price Calculation

```json
{
  "type": "TextBody",
  "text": "Total: $${`${form.quantity} * ${data.price}`}"
}
```

Or with tax:

```json
{
  "type": "TextBody",
  "text": "Total (with tax): $${`(${form.quantity} * ${data.price} * 1.08).toFixed(2)`}"
}
```

**Note**: `toFixed()` not always supported; use server-side calculation for precision.

### Age Verification

```json
{
  "type": "If",
  "condition": "${`${form.age} >= 18`}",
  "then": [...]
}
```

### Discount Eligibility

```json
{
  "type": "If",
  "condition": "${`${form.purchase_total} > 100 && ${form.is_member} == true`}",
  "then": [
    {
      "type": "TextBody",
      "text": "You qualify for a $${`${form.purchase_total} * 0.15`} discount!"
    }
  ]
}
```

### Inventory Check

```json
{
  "type": "If",
  "condition": "${`${data.stock_count} > 0`}",
  "then": [
    {
      "type": "TextBody",
      "text": "${data.stock_count} items in stock"
    }
  ],
  "else": [
    {
      "type": "TextBody",
      "text": "Out of stock"
    }
  ]
}
```

### Dynamic URL Building

```json
{
  "type": "EmbeddedLink",
  "text": "View Details",
  "on-click-action": {
    "action": "open_url",
    "url": "https://example.com/product/${form.product_id}"
  }
}
```

---

## Expression Limitations

### What Works

✓ Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
✓ Logical: `&&`, `||`, `!`
✓ Math: `+`, `-`, `*`, `/`, `%`
✓ String concatenation: `+`
✓ Field references: `${form.x}`, `${data.y}`

### What Doesn't Work

✗ Method calls: `.length`, `.toUpperCase()` (mostly)
✗ Array operations: `[0]`, `.map()`, `.filter()`
✗ Object access: `.property`, `['key']`
✗ Regular expressions
✗ Custom functions
✗ Complex conditionals (keep simple)

**Exception**: Limited string methods like `toFixed()` on numbers.

---

## Expression Examples

### Quantity × Price

```json
{
  "id": "CART_TOTAL",
  "data": {
    "type": "object",
    "properties": {
      "unit_price": { "type": "number", "__example__": 29.99 }
    }
  },
  "layout": {
    "type": "SingleColumnLayout",
    "children": [
      {
        "type": "TextInput",
        "name": "quantity",
        "input-type": "number",
        "label": "Quantity",
        "init-value": "1"
      },
      {
        "type": "TextBody",
        "text": "Price per item: $${data.unit_price}"
      },
      {
        "type": "TextBody",
        "text": "Subtotal: $${`${form.quantity} * ${data.unit_price}`}"
      }
    ]
  }
}
```

### Multi-Condition Check

```json
{
  "condition": "${`${form.age} >= 18 && ${form.has_account} == true && ${form.country} == 'USA'`}"
}
```

### String Formatting

```json
{
  "type": "TextBody",
  "text": "${`${form.first_name.toUpperCase()} ${form.last_name}`}"
}
```

**Note**: Some string methods work, others don't. Test carefully.

---

## Order of Operations

Standard mathematical order applies:

```json
${`2 + 3 * 4`}  // 14 (not 20)
${`(2 + 3) * 4`} // 20
```

Use parentheses for clarity:

```json
${`(${form.price} + ${data.tax}) * ${form.quantity}`}
```

---

## Type Coercion

Expressions handle type conversion automatically:

```json
${`"5" + 3`}  // "53" (string concatenation)
${`5 + 3`}    // 8 (math)
${`"5" * 3`}  // 15 (coerced to number)
${form.quantity} > 10  // number comparison
```

---

## Debugging Expressions

### Common Errors

**Syntax error: Missing backticks**
```json
// Wrong:
${form.age >= 18}

// Right:
${`${form.age} >= 18`}
```

**Syntax error: Field name typos**
```json
// Wrong:
${`${form.firstName} >= 18`}  // field is first_name

// Right:
${`${form.first_name} >= 18`}
```

**Type mismatch in comparison**
```json
// Form values are strings:
${`${form.age} >= 18`}  // May not work as expected

// Better to validate server-side
```

### Testing Tips

1. Test expressions in data_exchange payloads first
2. Use simple values in `__example__` to verify logic
3. Don't use complex nested expressions (keep ≤2 operations)
4. Always validate business logic server-side
5. Consider readability over cleverness

---

## Best Practices

1. **Keep expressions simple** - One or two operations max
2. **Use meaningful field names** - `total_price` not `t`
3. **Validate server-side** - Never trust client calculations
4. **Use strings for concatenation** - Clear intent
5. **Parenthesize complex expressions** - For clarity
6. **Avoid nested field access** - Stick to `${form.x}` and `${data.y}`
7. **Test edge cases** - Zero, negative, null values
8. **Document complex logic** - Why this calculation?
9. **Use expressions for display** - Not critical business logic
10. **Round monetary values** - Avoid floating point errors

---

## Monetary Calculations Warning

Be careful with floating-point precision:

```json
// Potential precision issue:
${`${form.price} * 1.08`}  // Might have precision errors

// Better: Calculate server-side
```

For critical calculations (pricing, payments), always compute server-side, not in expressions.

---

## Next Steps

- Learn **actions** in `13-actions.md`
- Learn **routing** in `15-routing-model.md`
- Learn **validation** in `17-validation-rules.md`
