# Faceting Reference

Faceting creates small multiples by partitioning data across multiple subplots. Use `fx` for horizontal facets (columns) and `fy` for vertical facets (rows).

## Basic Faceting

### Horizontal Facets (fx)

Creates columns of subplots:

```javascript
Plot.plot({
  fx: {label: "Category"},
  marks: [
    Plot.dot(data, {
      fx: "category",  // Partition by this column
      x: "x",
      y: "y"
    })
  ]
})
```

### Vertical Facets (fy)

Creates rows of subplots:

```javascript
Plot.plot({
  fy: {label: "Year"},
  marks: [
    Plot.lineY(data, {
      fy: "year",
      x: "month",
      y: "value"
    })
  ]
})
```

### Grid Layout (fx + fy)

Creates a 2D grid:

```javascript
Plot.plot({
  fx: {label: "Region"},
  fy: {label: "Product"},
  marks: [
    Plot.barY(data, {
      fx: "region",
      fy: "product",
      x: "quarter",
      y: "sales"
    })
  ]
})
```

## Facet Configuration

### Plot-Level Options

Configure facets at the plot level:

```javascript
Plot.plot({
  fx: {
    label: "Custom Label",
    domain: ["A", "B", "C"],  // Explicit order
    padding: 0.1,              // Space between facets (0-1)
    axis: "top",               // Axis position
    tickRotate: 45             // Rotate labels
  },
  fy: {
    label: "Another Dimension",
    reverse: true              // Reverse order
  },
  marks: [...]
})
```

### Domain

Control facet categories and order:

```javascript
{
  fx: {
    domain: ["Small", "Medium", "Large"]  // Explicit order
  }
}
```

Auto-inferred from data if not specified:
```javascript
{fx: {}}  // Domain auto-computed
```

### Padding

Space between facets (0 to 1):

```javascript
{
  fx: {padding: 0.1},  // 10% padding
  fy: {padding: 0.05}  // 5% padding
}
```

### Axis Position

Where to show facet labels:

```javascript
{
  fx: {axis: "top"},    // top (default), bottom, both, null
  fy: {axis: "right"}   // right (default), left, both, null
}
```

### Label

Custom facet dimension label:

```javascript
{
  fx: {label: "Region"},
  fy: {label: "Product Line"}
}
```

## Scale Sharing

### Shared Scales (Default)

All facets share the same x and y scales:

```javascript
Plot.plot({
  fx: {label: "Category"},
  marks: [Plot.dot(data, {fx: "category", x: "x", y: "y"})]
})
// All facets have same x and y ranges
```

### Independent Scales

Each facet has its own scale domain:

```javascript
Plot.plot({
  fx: {label: "Category"},
  y: {domain: undefined},  // Each facet gets its own y domain
  marks: [Plot.dot(data, {fx: "category", x: "x", y: "y"})]
})
```

Fixed domains work across all facets:
```javascript
{
  y: {domain: [0, 100]}  // Same domain for all facets
}
```

## Mixed Marks

### Faceted and Non-Faceted Marks

Combine faceted marks with non-faceted reference marks:

```javascript
Plot.plot({
  fx: {label: "Group"},
  marks: [
    // Faceted data
    Plot.dot(data, {
      fx: "group",
      x: "x",
      y: "y"
    }),

    // Non-faceted reference line (appears in all facets)
    Plot.ruleY([50], {
      stroke: "red",
      strokeDasharray: "4,4"
    })
  ]
})
```

### Different Facets for Different Marks

```javascript
Plot.plot({
  fx: {label: "Category"},
  fy: {label: "Region"},
  marks: [
    // Faceted by both fx and fy
    Plot.dot(dataA, {
      fx: "category",
      fy: "region",
      x: "x",
      y: "y"
    }),

    // Faceted only by fx
    Plot.lineY(dataB, {
      fx: "category",
      x: "month",
      y: "value"
    })
  ]
})
```

## Facet Filtering

### Subset of Facets

Show only specific facets:

```javascript
Plot.plot({
  fx: {
    domain: ["A", "B", "C"]  // Only these facets
  },
  marks: [
    Plot.dot(data, {
      fx: "category",
      x: "x",
      y: "y",
      filter: d => ["A", "B", "C"].includes(d.category)
    })
  ]
})
```

### Computed Facets

Derive facet values from data:

```javascript
Plot.plot({
  fx: {label: "Range"},
  marks: [
    Plot.dot(data, {
      fx: d => d.value < 50 ? "Low" : "High",
      x: "x",
      y: "y"
    })
  ]
})
```

## Facet Ordering

### Alphabetical (Default)

```javascript
{fx: {}}  // Alphabetical order
```

### Explicit Order

```javascript
{
  fx: {
    domain: ["Q1", "Q2", "Q3", "Q4"]  // Custom order
  }
}
```

### Reverse Order

```javascript
{
  fx: {reverse: true}
}
```

### Sort by Value

Use data transforms:

```javascript
Plot.plot({
  fx: {
    domain: d3.groupSort(data, g => -d3.sum(g, d => d.value), d => d.category)
  },
  marks: [...]
})
```

## Layout Options

### Margins

Control space around each facet:

```javascript
Plot.plot({
  marginTop: 30,
  marginRight: 20,
  marginBottom: 40,
  marginLeft: 50,
  marks: [...]
})
```

### Facet Dimensions

Control overall plot size (facets scale accordingly):

```javascript
Plot.plot({
  width: 960,
  height: 640,
  fx: {label: "Category"},
  marks: [...]
})
```

## Common Patterns

### Temporal Facets

```javascript
Plot.plot({
  fy: {label: "Year"},
  marks: [
    Plot.lineY(data, {
      fy: d => new Date(d.date).getFullYear(),
      x: d => new Date(d.date).getMonth(),
      y: "value"
    })
  ]
})
```

### Comparison Across Groups

```javascript
Plot.plot({
  fx: {label: "Treatment"},
  marks: [
    Plot.rectY(data, Plot.binX(
      {y: "count"},
      {
        fx: "treatment",
        x: "outcome",
        fill: "steelblue"
      }
    ))
  ]
})
```

### Geographic Facets

```javascript
Plot.plot({
  projection: "albers-usa",
  fx: {label: "Year"},
  color: {scheme: "blues", legend: true},
  marks: [
    Plot.geo(states, {
      fx: "year",
      fill: "value"
    })
  ]
})
```

### Scatter Plot Matrix

Show all pairwise relationships:

```javascript
const variables = ["var1", "var2", "var3"];

Plot.plot({
  fx: {domain: variables},
  fy: {domain: variables},
  marks: variables.flatMap(x =>
    variables.map(y =>
      Plot.dot(data, {
        fx: x,
        fy: y,
        x: x,
        y: y,
        r: 2
      })
    )
  )
})
```

## Faceting vs Color Encoding

### When to Use Faceting
- Many categories (>5)
- Overlapping patterns in single plot
- Want to emphasize individual patterns
- Comparing distributions

### When to Use Color
- Few categories (<5)
- Patterns don't overlap heavily
- Want compact visualization
- Comparing trends

### Combining Both

```javascript
Plot.plot({
  fx: {label: "Region"},
  color: {legend: true},
  marks: [
    Plot.lineY(data, {
      fx: "region",
      x: "date",
      y: "value",
      stroke: "product"  // Color within each facet
    })
  ]
})
```

## Accessibility

Add descriptive labels for screen readers:

```javascript
Plot.plot({
  fx: {label: "Geographic Region"},
  fy: {label: "Year"},
  ariaLabel: "Sales data by region and year",
  marks: [...]
})
```

## Related Documentation
- [examples/faceted-plot.md](examples/faceted-plot.md) - Faceting examples
- [plot-options.md](plot-options.md) - Plot-level configuration
