# Bar Chart Examples

Bar charts visualize categorical data using `Plot.barY()` (vertical bars) or `Plot.barX()` (horizontal bars). Plot handles grouping, stacking, and aggregation through transforms.

## Basic Vertical Bar Chart

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {category: "A", value: 28},
  {category: "B", value: 55},
  {category: "C", value: 43},
  {category: "D", value: 91}
];

Plot.plot({
  marks: [
    Plot.barY(data, {
      x: "category",
      y: "value",
      fill: "steelblue"
    }),
    Plot.ruleY([0])  // Baseline
  ]
}).display();
```

## Horizontal Bar Chart

Use `Plot.barX()` for horizontal orientation:

```javascript
const data = [
  {product: "Laptop", sales: 245},
  {product: "Phone", sales: 532},
  {product: "Tablet", sales: 189},
  {product: "Watch", sales: 324}
];

Plot.plot({
  marginLeft: 80,  // Space for labels
  marks: [
    Plot.barX(data, {
      y: "product",
      x: "sales",
      fill: "coral"
    }),
    Plot.ruleX([0])
  ]
}).display();
```

## Grouped Bar Chart

Use the `groupZ` transform to aggregate multiple observations:

```javascript
const data = [
  {month: "Jan", category: "A", value: 10},
  {month: "Jan", category: "A", value: 12},
  {month: "Jan", category: "B", value: 15},
  {month: "Feb", category: "A", value: 18},
  {month: "Feb", category: "B", value: 22},
  {month: "Feb", category: "B", value: 20}
];

Plot.plot({
  marks: [
    Plot.barY(data, Plot.groupZ(
      {y: "sum"},  // Aggregate function
      {
        x: "month",
        y: "value",
        fill: "category",
        tip: true
      }
    )),
    Plot.ruleY([0])
  ],
  color: {legend: true}
}).display();
```

## Stacked Bar Chart

Use the `stack` transform to stack bars:

```javascript
const data = [
  {quarter: "Q1", product: "Laptop", revenue: 100},
  {quarter: "Q1", product: "Phone", revenue: 150},
  {quarter: "Q1", product: "Tablet", revenue: 80},
  {quarter: "Q2", product: "Laptop", revenue: 120},
  {quarter: "Q2", product: "Phone", revenue: 180},
  {quarter: "Q2", product: "Tablet", revenue: 90},
  {quarter: "Q3", product: "Laptop", revenue: 110},
  {quarter: "Q3", product: "Phone", revenue: 200},
  {quarter: "Q3", product: "Tablet", revenue: 95}
];

Plot.plot({
  marks: [
    Plot.barY(data, Plot.stackY({
      x: "quarter",
      y: "revenue",
      fill: "product",
      tip: true
    })),
    Plot.ruleY([0])
  ],
  color: {
    legend: true,
    scheme: "category10"
  }
}).display();
```

## Normalized Stacked Bar Chart

Show proportions instead of absolute values:

```javascript
const data = [
  {year: "2020", source: "Solar", amount: 20},
  {year: "2020", source: "Wind", amount: 30},
  {year: "2020", source: "Coal", amount: 50},
  {year: "2021", source: "Solar", amount: 30},
  {year: "2021", source: "Wind", amount: 40},
  {year: "2021", source: "Coal", amount: 30},
  {year: "2022", source: "Solar", amount: 45},
  {year: "2022", source: "Wind", amount: 50},
  {year: "2022", source: "Coal", amount: 5}
];

Plot.plot({
  y: {
    grid: true,
    percent: true  // Show as percentages
  },
  marks: [
    Plot.barY(data, Plot.stackY(Plot.normalizeY({
      x: "year",
      y: "amount",
      fill: "source",
      tip: true
    }))),
    Plot.ruleY([0])
  ],
  color: {legend: true}
}).display();
```

## Diverging Bar Chart

Show positive and negative values:

```javascript
const data = [
  {category: "Marketing", change: 15},
  {category: "Sales", change: -8},
  {category: "Engineering", change: 22},
  {category: "Support", change: -5},
  {category: "Product", change: 12}
];

Plot.plot({
  marks: [
    Plot.barY(data, {
      x: "category",
      y: "change",
      fill: d => d.change > 0 ? "green" : "red",
      tip: true
    }),
    Plot.ruleY([0], {stroke: "black", strokeWidth: 2})
  ]
}).display();
```

## Histogram (Binned Data)

Use the `bin` transform to create histograms from continuous data:

```javascript
// Raw continuous data
const heights = [
  162, 170, 168, 175, 180, 165, 172, 178, 169, 174,
  171, 166, 173, 177, 164, 176, 182, 167, 179, 168
];

const data = heights.map(h => ({height: h}));

Plot.plot({
  marks: [
    Plot.rectY(data, Plot.binX(
      {y: "count"},  // Count observations in each bin
      {
        x: "height",
        fill: "steelblue",
        tip: true
      }
    )),
    Plot.ruleY([0])
  ]
}).display();
```

## Custom Bin Configuration

Control bin thresholds and intervals:

```javascript
const data = [
  {score: 65}, {score: 72}, {score: 88}, {score: 91},
  {score: 55}, {score: 78}, {score: 84}, {score: 95},
  {score: 68}, {score: 74}, {score: 81}, {score: 89}
];

Plot.plot({
  marks: [
    Plot.rectY(data, Plot.binX(
      {y: "count"},
      {
        x: "score",
        thresholds: [0, 60, 70, 80, 90, 100],  // Grade ranges
        fill: "steelblue",
        tip: true
      }
    )),
    Plot.ruleY([0])
  ]
}).display();
```

## Grouped and Stacked

Combine grouping and stacking:

```javascript
const data = [
  {region: "North", quarter: "Q1", type: "Online", sales: 50},
  {region: "North", quarter: "Q1", type: "Store", sales: 70},
  {region: "North", quarter: "Q2", type: "Online", sales: 60},
  {region: "North", quarter: "Q2", type: "Store", sales: 75},
  {region: "South", quarter: "Q1", type: "Online", sales: 45},
  {region: "South", quarter: "Q1", type: "Store", sales: 65},
  {region: "South", quarter: "Q2", type: "Online", sales: 55},
  {region: "South", quarter: "Q2", type: "Store", sales: 70}
];

Plot.plot({
  fx: {label: "Region"},
  marks: [
    Plot.barY(data, Plot.stackY({
      x: "quarter",
      y: "sales",
      fill: "type",
      tip: true
    })),
    Plot.ruleY([0])
  ],
  color: {legend: true}
}).display();
```

## Bar Chart with Error Bars

Layer error bars on top of bars:

```javascript
const data = [
  {category: "A", mean: 25, std: 5},
  {category: "B", mean: 40, std: 8},
  {category: "C", mean: 35, std: 6}
];

Plot.plot({
  marks: [
    // Bars
    Plot.barY(data, {
      x: "category",
      y: "mean",
      fill: "lightblue"
    }),

    // Error bars
    Plot.ruleY(data, {
      x: "category",
      y1: d => d.mean - d.std,
      y2: d => d.mean + d.std,
      stroke: "black",
      strokeWidth: 2
    }),

    Plot.ruleY([0])
  ]
}).display();
```

## Key Patterns

### Orientation
- `Plot.barY()`: Vertical bars (x = category, y = value)
- `Plot.barX()`: Horizontal bars (y = category, x = value)

### Aggregation Transforms
```javascript
// Sum values by category
Plot.barY(data, Plot.groupZ({y: "sum"}, {x: "category", y: "value"}))

// Count observations
Plot.barY(data, Plot.groupX({y: "count"}, {x: "category"}))

// Average values
Plot.barY(data, Plot.groupZ({y: "mean"}, {x: "category", y: "value"}))
```

### Stacking
```javascript
// Stack bars
Plot.barY(data, Plot.stackY({x: "x", y: "y", fill: "category"}))

// Normalized stacking (100%)
Plot.barY(data, Plot.stackY(Plot.normalizeY({...})))
```

### Binning (Histograms)
```javascript
// Auto binning
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// Custom thresholds
Plot.rectY(data, Plot.binX({y: "count"}, {
  x: "value",
  thresholds: [0, 10, 20, 30, 40, 50]
}))
```

### Color Encoding
```javascript
// Fixed color
{fill: "steelblue"}

// Color by category
{fill: "category"}

// Conditional color
{fill: d => d.value > 0 ? "green" : "red"}
```

## Related Examples
- [faceted-plot.md](faceted-plot.md) - Bar charts in small multiples
- [time-series.md](time-series.md) - Temporal bar charts

## Reference
- [reference/marks.md](../marks.md) - Complete bar mark options
- [reference/transforms.md](../transforms.md) - Grouping, stacking, binning transforms
