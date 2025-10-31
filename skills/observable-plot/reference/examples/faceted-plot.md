# Faceted Plot Examples

Faceting creates small multiples by splitting data across multiple subplots. Use `fx` (horizontal facets) and `fy` (vertical facets) to partition data by categorical variables.

## Horizontal Faceting

Use `fx` to create columns:

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {region: "North", month: "Jan", sales: 100},
  {region: "North", month: "Feb", sales: 120},
  {region: "North", month: "Mar", sales: 110},
  {region: "South", month: "Jan", sales: 90},
  {region: "South", month: "Feb", sales: 95},
  {region: "South", month: "Mar", sales: 105},
  {region: "East", month: "Jan", sales: 85},
  {region: "East", month: "Feb", sales: 100},
  {region: "East", month: "Mar", sales: 95}
];

Plot.plot({
  fx: {label: "Region"},
  marks: [
    Plot.barY(data, {
      fx: "region",
      x: "month",
      y: "sales",
      fill: "steelblue"
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## Vertical Faceting

Use `fy` to create rows:

```javascript
const data = [
  {year: 2020, quarter: "Q1", revenue: 100},
  {year: 2020, quarter: "Q2", revenue: 120},
  {year: 2020, quarter: "Q3", revenue: 115},
  {year: 2020, quarter: "Q4", revenue: 140},
  {year: 2021, quarter: "Q1", revenue: 130},
  {year: 2021, quarter: "Q2", revenue: 145},
  {year: 2021, quarter: "Q3", revenue: 135},
  {year: 2021, quarter: "Q4", revenue: 160}
];

Plot.plot({
  fy: {label: "Year"},
  marks: [
    Plot.lineY(data, {
      fy: "year",
      x: "quarter",
      y: "revenue",
      stroke: "coral",
      strokeWidth: 2,
      marker: "dot"
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## Grid Layout (fx + fy)

Combine horizontal and vertical faceting:

```javascript
const data = [
  {product: "A", region: "North", quarter: "Q1", sales: 100},
  {product: "A", region: "North", quarter: "Q2", sales: 120},
  {product: "A", region: "South", quarter: "Q1", sales: 90},
  {product: "A", region: "South", quarter: "Q2", sales: 95},
  {product: "B", region: "North", quarter: "Q1", sales: 80},
  {product: "B", region: "North", quarter: "Q2", sales: 110},
  {product: "B", region: "South", quarter: "Q1", sales: 75},
  {product: "B", region: "South", quarter: "Q2", sales: 85}
];

Plot.plot({
  fx: {label: "Region"},
  fy: {label: "Product"},
  marks: [
    Plot.barY(data, {
      fx: "region",
      fy: "product",
      x: "quarter",
      y: "sales",
      fill: "steelblue"
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## Faceted Scatterplots

Create multiple scatterplots by category:

```javascript
const data = Array.from({length: 200}, () => ({
  species: ["setosa", "versicolor", "virginica"][Math.floor(Math.random() * 3)],
  sepalLength: 4 + Math.random() * 4,
  sepalWidth: 2 + Math.random() * 2,
  petalLength: 1 + Math.random() * 6,
  petalWidth: 0.1 + Math.random() * 2.5
}));

Plot.plot({
  fx: {label: "Species"},
  color: {legend: true},
  marks: [
    Plot.frame(),
    Plot.dot(data, {
      fx: "species",
      x: "sepalLength",
      y: "sepalWidth",
      fill: "species",
      r: 3
    })
  ]
}).display();
```

## Shared vs Independent Scales

Control scale sharing across facets:

```javascript
const data = [
  {category: "A", x: 1, y: 10},
  {category: "A", x: 2, y: 20},
  {category: "B", x: 1, y: 100},
  {category: "B", x: 2, y: 200}
];

// Shared scales (default)
Plot.plot({
  fx: {label: "Category"},
  marks: [
    Plot.dot(data, {
      fx: "category",
      x: "x",
      y: "y"
    })
  ]
}).display();

// Independent y-scales
Plot.plot({
  fx: {label: "Category"},
  y: {domain: undefined},  // Let each facet determine its own scale
  marks: [
    Plot.dot(data, {
      fx: "category",
      x: "x",
      y: "y"
    })
  ]
}).display();
```

## Faceted Time Series

Multiple time series in small multiples:

```javascript
const data = Array.from({length: 120}, (_, i) => ({
  metric: ["CPU", "Memory", "Disk"][Math.floor(i / 40)],
  time: new Date(2023, 0, 1 + (i % 40)),
  value: 50 + Math.random() * 30
}));

Plot.plot({
  fy: {label: "Metric"},
  marks: [
    Plot.gridY(),
    Plot.lineY(data, {
      fy: "metric",
      x: "time",
      y: "value",
      stroke: "steelblue",
      strokeWidth: 1.5
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## Mixed Faceted and Non-Faceted Marks

Layer faceted and non-faceted marks:

```javascript
const data = [
  {group: "A", x: 1, y: 10},
  {group: "A", x: 2, y: 20},
  {group: "B", x: 1, y: 15},
  {group: "B", x: 2, y: 25}
];

const overallMean = 17.5;

Plot.plot({
  fx: {label: "Group"},
  marks: [
    // Faceted dots
    Plot.dot(data, {
      fx: "group",
      x: "x",
      y: "y",
      fill: "steelblue"
    }),

    // Non-faceted reference line (appears in all facets)
    Plot.ruleY([overallMean], {
      stroke: "red",
      strokeDasharray: "4,4"
    })
  ]
}).display();
```

## Custom Facet Order

Control facet ordering:

```javascript
const data = [
  {size: "Small", value: 10},
  {size: "Medium", value: 20},
  {size: "Large", value: 30},
  {size: "Small", value: 12},
  {size: "Medium", value: 22},
  {size: "Large", value: 28}
];

Plot.plot({
  fx: {
    label: "Size",
    domain: ["Small", "Medium", "Large"]  // Explicit order
  },
  marks: [
    Plot.barY(data, Plot.groupX(
      {y: "mean"},
      {
        fx: "size",
        x: () => "Average",
        y: "value",
        fill: "steelblue"
      }
    ))
  ]
}).display();
```

## Faceted Histograms

Compare distributions across categories:

```javascript
const data = Array.from({length: 300}, () => ({
  condition: ["Control", "Treatment A", "Treatment B"][Math.floor(Math.random() * 3)],
  measurement: 50 + Math.random() * 30
}));

Plot.plot({
  fx: {label: "Condition"},
  marks: [
    Plot.rectY(data, Plot.binX(
      {y: "count"},
      {
        fx: "condition",
        x: "measurement",
        fill: "steelblue",
        thresholds: 20
      }
    )),
    Plot.ruleY([0])
  ]
}).display();
```

## Faceted Maps

Geographic data in small multiples:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

const data = [
  {year: 2010, state: "California", value: 37.3},
  {year: 2010, state: "Texas", value: 25.1},
  {year: 2020, state: "California", value: 39.5},
  {year: 2020, state: "Texas", value: 29.0}
  // ... more data
];

Plot.plot({
  projection: "albers-usa",
  fx: {label: "Year"},
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.geo(states, {
      fx: d => 2010,  // Assign facet dynamically
      fill: d => data.find(x => x.year === 2010 && x.state === d.properties.name)?.value,
      stroke: "white"
    }),
    Plot.geo(states, {
      fx: d => 2020,
      fill: d => data.find(x => x.year === 2020 && x.state === d.properties.name)?.value,
      stroke: "white"
    })
  ]
}).display();
```

## Trellis Plot

Classic trellis display with conditioning:

```javascript
const data = Array.from({length: 400}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100,
  groupA: ["Low", "High"][Math.floor(Math.random() * 2)],
  groupB: ["Type 1", "Type 2"][Math.floor(Math.random() * 2)]
}));

Plot.plot({
  fx: {label: "Group A"},
  fy: {label: "Group B"},
  marks: [
    Plot.frame(),
    Plot.dot(data, {
      fx: "groupA",
      fy: "groupB",
      x: "x",
      y: "y",
      r: 2,
      fill: "steelblue",
      fillOpacity: 0.5
    })
  ]
}).display();
```

## Key Patterns

### Basic Faceting
```javascript
// Horizontal facets (columns)
{fx: "category"}

// Vertical facets (rows)
{fy: "category"}

// Grid layout
{fx: "categoryX", fy: "categoryY"}
```

### Facet Configuration
```javascript
Plot.plot({
  fx: {
    label: "Custom Label",
    domain: ["A", "B", "C"],  // Explicit order
    padding: 0.1,              // Space between facets
    axis: "top"                // Axis position
  }
})
```

### Scale Sharing
```javascript
// Shared scales across facets (default)
Plot.plot({...})

// Independent scales per facet
Plot.plot({
  y: {domain: undefined}  // Each facet uses its own domain
})
```

### Facet Labels
```javascript
// Simple label
{fx: {label: "Category"}}

// Custom formatting
{fx: {
  label: "Region",
  tickFormat: d => d.toUpperCase()
}}
```

### Mixed Marks
```javascript
Plot.plot({
  marks: [
    // Faceted mark
    Plot.dot(data, {fx: "category", ...}),

    // Non-faceted mark (appears in all facets)
    Plot.ruleY([0])
  ]
})
```

### When to Use Faceting
- Compare patterns across categories
- Show how relationships vary by group
- Display temporal evolution across entities
- Avoid overlapping marks in single plot
- Each facet shows same variables with different subsets

### Faceting vs Color Encoding
- **Faceting**: Better for many categories (>5), makes individual patterns clearer
- **Color**: Better for few categories (<5), easier comparison, more compact

## Related Examples
- [scatterplot.md](scatterplot.md) - Basic plots that can be faceted
- [bar-chart.md](bar-chart.md) - Bar charts with faceting
- [time-series.md](time-series.md) - Time series with faceting
- [choropleth-map.md](choropleth-map.md) - Geographic small multiples

## Reference
- [reference/faceting.md](../faceting.md) - Complete faceting options
- [reference/plot-options.md](../plot-options.md) - Layout configuration
- [reference/geographic.md](../geographic.md) - Geographic projections and data for faceted maps
