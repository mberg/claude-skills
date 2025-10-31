# Common Patterns Reference

Recipes for common visualization tasks using Observable Plot's declarative API. These patterns emphasize configuration over code.

## Data Aggregation

### Count by Category

```javascript
// Don't pre-aggregate - use groupX
Plot.barY(data, Plot.groupX({y: "count"}, {x: "category"}))
```

### Sum by Category

```javascript
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "value"}))
```

### Average by Category

```javascript
Plot.barY(data, Plot.groupX({y: "mean"}, {x: "category", y: "value"}))
```

### Multiple Aggregations

```javascript
Plot.dot(data, Plot.groupX(
  {
    y: "mean",      // Position
    r: "count",     // Size
    fill: "sum"     // Color
  },
  {x: "category", y: "value"}
))
```

## Histograms

### Basic Histogram

```javascript
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))
```

### Custom Bins

```javascript
Plot.rectY(data, Plot.binX(
  {y: "count"},
  {
    x: "value",
    thresholds: 20  // or [0, 10, 20, 30, ...]
  }
))
```

### Cumulative Distribution

```javascript
Plot.lineY(data, Plot.binX(
  {y: "count"},
  {x: "value", cumulative: true}
))
```

## Stacking

### Stacked Bars

```javascript
Plot.barY(data, Plot.stackY({
  x: "category",
  y: "value",
  fill: "subcategory"
}))
```

### Stacked Area

```javascript
Plot.areaY(data, Plot.stackY({
  x: "date",
  y: "value",
  fill: "series"
}))
```

### 100% Stacked

```javascript
Plot.areaY(data, Plot.stackY(Plot.normalizeY({
  x: "date",
  y: "value",
  fill: "series"
})))
```

## Time Series

### Basic Line Chart

```javascript
Plot.lineY(data, {
  x: "date",
  y: "value",
  stroke: "steelblue"
})
```

### Multiple Series

```javascript
Plot.lineY(data, {
  x: "date",
  y: "value",
  stroke: "series"  // Color by series
})
```

### Moving Average

```javascript
Plot.lineY(data, Plot.windowY(
  {k: 7},  // 7-period window
  {x: "date", y: "value"}
))
```

### With Confidence Band

```javascript
Plot.plot({
  marks: [
    // Confidence band
    Plot.areaY(data, {
      x: "date",
      y1: "lower",
      y2: "upper",
      fill: "steelblue",
      fillOpacity: 0.2
    }),

    // Mean line
    Plot.lineY(data, {
      x: "date",
      y: "mean",
      stroke: "steelblue"
    })
  ]
})
```

## Comparisons

### Side-by-Side Bars

```javascript
Plot.barY(data, Plot.dodgeX({
  x: "category",
  y: "value",
  fill: "subcategory"
}))
```

### Small Multiples

```javascript
Plot.plot({
  fx: {label: "Category"},
  marks: [
    Plot.dot(data, {
      fx: "category",
      x: "x",
      y: "y"
    })
  ]
})
```

### Before/After

```javascript
Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "category",
      y: "before",
      stroke: "lightgray"
    }),
    Plot.lineY(data, {
      x: "category",
      y: "after",
      stroke: "steelblue"
    })
  ]
})
```

## Distributions

### Box Plot

```javascript
Plot.boxY(data, {x: "category", y: "value"})
```

### Violin Plot (Density + Box)

```javascript
Plot.plot({
  marks: [
    Plot.density(data, {
      x: "category",
      y: "value",
      fill: "category"
    }),
    Plot.boxY(data, {
      x: "category",
      y: "value",
      stroke: "black"
    })
  ]
})
```

### Beeswarm

```javascript
Plot.dot(data, Plot.dodgeX("middle", {
  x: "category",
  y: "value",
  r: 3,
  fill: "steelblue"
}))
```

## Correlations

### Scatterplot with Regression

```javascript
Plot.plot({
  marks: [
    Plot.dot(data, {x: "x", y: "y"}),
    Plot.linearRegressionY(data, {x: "x", y: "y", stroke: "red"})
  ]
})
```

### Correlation Matrix

```javascript
const variables = ["var1", "var2", "var3"];

Plot.plot({
  fx: {domain: variables},
  fy: {domain: variables},
  marks: variables.flatMap(x =>
    variables.map(y =>
      Plot.dot(data, {fx: x, fy: y, x: x, y: y, r: 2})
    )
  )
})
```

### Hexbin for Dense Data

```javascript
Plot.dot(data, Plot.hexbin(
  {fill: "count"},
  {x: "x", y: "y", binWidth: 10}
))
```

## Rankings

### Sorted Bars

```javascript
Plot.barY(data, Plot.sortX({
  y: "descending"  // Sort by value
}, {
  x: "category",
  y: "value"
}))
```

### Top N

```javascript
const topN = data.sort((a, b) => b.value - a.value).slice(0, 10);

Plot.barY(topN, {x: "name", y: "value"})
```

### Lollipop Chart

```javascript
Plot.plot({
  marks: [
    Plot.ruleX(data, {x: "value", y: "category"}),
    Plot.dot(data, {x: "value", y: "category", r: 5})
  ]
})
```

## Compositions

### Layered Visualization

```javascript
Plot.plot({
  marks: [
    // Background
    Plot.gridY(),
    Plot.ruleY([0]),

    // Data layer 1
    Plot.areaY(data, {x: "x", y: "y", fill: "lightblue"}),

    // Data layer 2
    Plot.lineY(data, {x: "x", y: "y", stroke: "blue"}),

    // Annotations
    Plot.text(labels, {x: "x", y: "y", text: "label"}),
    Plot.dot(points, {x: "x", y: "y", fill: "red"})
  ]
})
```

### Dual Axes (Not Recommended)

Observable Plot doesn't support dual y-axes by design. Instead, use:

**Faceting**:
```javascript
Plot.plot({
  fy: {label: "Metric"},
  marks: [
    Plot.lineY(data, {fy: "metric", x: "date", y: "value"})
  ]
})
```

**Normalized scales**:
```javascript
Plot.lineY(data, Plot.normalizeY("first", {
  x: "date",
  y: "value",
  stroke: "metric"
}))
```

## Highlighting

### Conditional Formatting

```javascript
Plot.barY(data, {
  x: "category",
  y: "value",
  fill: d => d.value > 50 ? "green" : "red"
})
```

### Highlighting Subset

```javascript
Plot.plot({
  marks: [
    // All data (gray)
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "lightgray",
      r: 3
    }),

    // Highlighted subset
    Plot.dot(data.filter(d => d.important), {
      x: "x",
      y: "y",
      fill: "red",
      r: 6
    })
  ]
})
```

### Reference Lines

```javascript
Plot.plot({
  marks: [
    Plot.barY(data, {x: "category", y: "value"}),

    // Threshold line
    Plot.ruleY([75], {
      stroke: "red",
      strokeDasharray: "4,4"
    }),

    // Average line
    Plot.ruleY([d3.mean(data, d => d.value)], {
      stroke: "blue"
    })
  ]
})
```

## Geographic

### Choropleth Map

```javascript
Plot.plot({
  projection: "albers-usa",
  color: {scheme: "blues", legend: true},
  marks: [
    Plot.geo(states, {
      fill: "value",
      stroke: "white",
      tip: true
    })
  ]
})
```

### Point Map

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {fill: "lightgray"}),
    Plot.dot(cities, {
      x: "longitude",
      y: "latitude",
      r: "population",
      fill: "red"
    })
  ]
})
```

### Hexbin Map

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {fill: "none", stroke: "gray"}),
    Plot.dot(events, Plot.hexbin(
      {fill: "count"},
      {x: "longitude", y: "latitude", binWidth: 30}
    ))
  ]
})
```

## Minimizing External JavaScript

### Use Transforms Instead of Pre-processing

**Don't**:
```javascript
const aggregated = d3.rollup(data, v => v.length, d => d.category);
Plot.barY(Array.from(aggregated), {x: d => d[0], y: d => d[1]})
```

**Do**:
```javascript
Plot.barY(data, Plot.groupX({y: "count"}, {x: "category"}))
```

### Use Channels for Dynamic Values

**Don't**:
```javascript
data.forEach(d => d.color = d.value > 50 ? "green" : "red");
Plot.dot(data, {x: "x", y: "y", fill: "color"})
```

**Do**:
```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  fill: d => d.value > 50 ? "green" : "red"
})
```

### Use Faceting Instead of Loops

**Don't**:
```javascript
categories.map(cat =>
  Plot.plot({
    title: cat,
    marks: [Plot.dot(data.filter(d => d.category === cat))]
  })
)
```

**Do**:
```javascript
Plot.plot({
  fx: {label: "Category"},
  marks: [
    Plot.dot(data, {fx: "category", x: "x", y: "y"})
  ]
})
```

## Color Strategies

### Sequential (One Direction)

```javascript
{color: {scheme: "blues"}}  // Light to dark
```

### Diverging (Two Directions)

```javascript
{color: {scheme: "rdbu", symmetric: true}}  // Red-white-blue
```

### Categorical (Distinct)

```javascript
{color: {scheme: "category10"}}  // Distinct colors
```

### Custom

```javascript
{color: {range: ["white", "yellow", "orange", "red"]}}
```

## Performance Patterns

### Large Point Datasets (>10k)

Use density or hexbin:
```javascript
Plot.density(data, {x: "x", y: "y", fill: "density"})
// or
Plot.dot(data, Plot.hexbin({fill: "count"}, {x: "x", y: "y"}))
```

### Many Categories (>20)

Use faceting instead of color:
```javascript
Plot.plot({
  fx: {label: "Category"},
  marks: [Plot.dot(data, {fx: "category", x: "x", y: "y"})]
})
```

### Complex Transforms

Chain transforms efficiently:
```javascript
Plot.barY(data, Plot.stackY(
  Plot.sort({y: "descending"},
    Plot.groupX({y: "sum"}, {x: "category", y: "value", fill: "type"})
  )
))
```

## Related Documentation
- [examples/](examples/) - Working examples
- [marks.md](marks.md) - Mark reference
- [transforms.md](transforms.md) - Transform reference
