# Time Series Examples

Time series visualizations show data over time using line and area marks. Plot automatically handles temporal scales and date formatting.

## Basic Line Chart

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {date: new Date("2023-01-01"), value: 100},
  {date: new Date("2023-02-01"), value: 120},
  {date: new Date("2023-03-01"), value: 115},
  {date: new Date("2023-04-01"), value: 140},
  {date: new Date("2023-05-01"), value: 135},
  {date: new Date("2023-06-01"), value: 160}
];

Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## With Points

Combine line and dot marks:

```javascript
const data = [
  {date: new Date("2023-01-01"), temperature: 45},
  {date: new Date("2023-02-01"), temperature: 48},
  {date: new Date("2023-03-01"), temperature: 55},
  {date: new Date("2023-04-01"), temperature: 62},
  {date: new Date("2023-05-01"), temperature: 70}
];

Plot.plot({
  marks: [
    Plot.gridY(),
    Plot.ruleY([0]),

    // Line
    Plot.lineY(data, {
      x: "date",
      y: "temperature",
      stroke: "coral",
      strokeWidth: 2
    }),

    // Points
    Plot.dot(data, {
      x: "date",
      y: "temperature",
      fill: "coral",
      r: 4,
      tip: true
    })
  ]
}).display();
```

## Multiple Series

Show multiple time series with color encoding:

```javascript
const data = [
  {date: new Date("2023-01-01"), series: "A", value: 100},
  {date: new Date("2023-01-01"), series: "B", value: 90},
  {date: new Date("2023-02-01"), series: "A", value: 120},
  {date: new Date("2023-02-01"), series: "B", value: 95},
  {date: new Date("2023-03-01"), series: "A", value: 115},
  {date: new Date("2023-03-01"), series: "B", value: 110}
];

Plot.plot({
  color: {
    legend: true,
    scheme: "category10"
  },
  marks: [
    Plot.gridY(),
    Plot.ruleY([0]),
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "series",
      strokeWidth: 2,
      tip: true
    })
  ]
}).display();
```

## Area Chart

Fill the area under the line:

```javascript
const data = [
  {month: new Date("2023-01-01"), sales: 1000},
  {month: new Date("2023-02-01"), sales: 1200},
  {month: new Date("2023-03-01"), sales: 1100},
  {month: new Date("2023-04-01"), sales: 1400},
  {month: new Date("2023-05-01"), sales: 1300}
];

Plot.plot({
  marks: [
    Plot.areaY(data, {
      x: "month",
      y: "sales",
      fill: "steelblue",
      fillOpacity: 0.3
    }),
    Plot.lineY(data, {
      x: "month",
      y: "sales",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.ruleY([0])
  ]
}).display();
```

## Stacked Area Chart

Stack multiple series:

```javascript
const data = [
  {date: new Date("2023-01"), product: "A", revenue: 100},
  {date: new Date("2023-01"), product: "B", revenue: 150},
  {date: new Date("2023-01"), product: "C", revenue: 80},
  {date: new Date("2023-02"), product: "A", revenue: 120},
  {date: new Date("2023-02"), product: "B", revenue: 180},
  {date: new Date("2023-02"), product: "C", revenue: 90},
  {date: new Date("2023-03"), product: "A", revenue: 110},
  {date: new Date("2023-03"), product: "B", revenue: 200},
  {date: new Date("2023-03"), product: "C", revenue: 95}
];

Plot.plot({
  color: {
    legend: true,
    scheme: "tableau10"
  },
  marks: [
    Plot.areaY(data, Plot.stackY({
      x: "date",
      y: "revenue",
      fill: "product",
      tip: true
    })),
    Plot.ruleY([0])
  ]
}).display();
```

## Normalized Stacked Area

Show proportions over time:

```javascript
const data = [
  {year: new Date("2018"), source: "Solar", amount: 20},
  {year: new Date("2018"), source: "Wind", amount: 30},
  {year: new Date("2018"), source: "Coal", amount: 50},
  {year: new Date("2019"), source: "Solar", amount: 25},
  {year: new Date("2019"), source: "Wind", amount: 35},
  {year: new Date("2019"), source: "Coal", amount: 40},
  {year: new Date("2020"), source: "Solar", amount: 30},
  {year: new Date("2020"), source: "Wind", amount: 40},
  {year: new Date("2020"), source: "Coal", amount: 30}
];

Plot.plot({
  y: {percent: true, grid: true},
  color: {legend: true},
  marks: [
    Plot.areaY(data, Plot.stackY(Plot.normalizeY({
      x: "year",
      y: "amount",
      fill: "source"
    }))),
    Plot.ruleY([0, 1])
  ]
}).display();
```

## Moving Average

Use window transform for smoothing:

```javascript
const data = Array.from({length: 100}, (_, i) => ({
  day: i,
  value: 50 + Math.random() * 20 + Math.sin(i / 10) * 10
}));

Plot.plot({
  marks: [
    Plot.gridY(),

    // Raw data (faint)
    Plot.lineY(data, {
      x: "day",
      y: "value",
      stroke: "lightgray",
      strokeWidth: 1
    }),

    // 7-day moving average
    Plot.lineY(data, Plot.windowY(
      {k: 7, strict: true},  // 7-point window
      {
        x: "day",
        y: "value",
        stroke: "steelblue",
        strokeWidth: 2
      }
    ))
  ]
}).display();
```

## Confidence Bands

Show uncertainty with area bands:

```javascript
const data = [
  {date: new Date("2023-01"), mean: 100, lower: 90, upper: 110},
  {date: new Date("2023-02"), mean: 120, lower: 105, upper: 135},
  {date: new Date("2023-03"), mean: 115, lower: 100, upper: 130},
  {date: new Date("2023-04"), mean: 140, lower: 120, upper: 160}
];

Plot.plot({
  marks: [
    Plot.gridY(),

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
      stroke: "steelblue",
      strokeWidth: 2
    }),

    Plot.ruleY([0])
  ]
}).display();
```

## Difference Chart

Highlight areas above/below a baseline:

```javascript
const data = [
  {month: new Date("2023-01"), actual: 100, target: 110},
  {month: new Date("2023-02"), actual: 125, target: 115},
  {month: new Date("2023-03"), actual: 108, target: 120},
  {month: new Date("2023-04"), actual: 145, target: 125}
];

Plot.plot({
  marks: [
    // Positive difference (above target)
    Plot.areaY(data, {
      x: "month",
      y1: "target",
      y2: "actual",
      fill: "green",
      fillOpacity: 0.3,
      filter: d => d.actual > d.target
    }),

    // Negative difference (below target)
    Plot.areaY(data, {
      x: "month",
      y1: "target",
      y2: "actual",
      fill: "red",
      fillOpacity: 0.3,
      filter: d => d.actual < d.target
    }),

    // Target line
    Plot.lineY(data, {
      x: "month",
      y: "target",
      stroke: "black",
      strokeDasharray: "4,4"
    }),

    // Actual line
    Plot.lineY(data, {
      x: "month",
      y: "actual",
      stroke: "steelblue",
      strokeWidth: 2
    })
  ]
}).display();
```

## Streamgraph

Centered stacked area chart:

```javascript
const data = [
  {year: 2018, category: "A", value: 30},
  {year: 2018, category: "B", value: 40},
  {year: 2018, category: "C", value: 35},
  {year: 2019, category: "A", value: 35},
  {year: 2019, category: "B", value: 45},
  {year: 2019, category: "C", value: 30},
  {year: 2020, category: "A", value: 40},
  {year: 2020, category: "B", value: 50},
  {year: 2020, category: "C", value: 25}
];

Plot.plot({
  color: {legend: true},
  marks: [
    Plot.areaY(data, Plot.stackY({
      offset: "center",  // Center the stack
      x: "year",
      y: "value",
      fill: "category"
    })),
    Plot.ruleY([0])
  ]
}).display();
```

## Date Parsing

Parse dates from strings:

```javascript
const data = [
  {date: "2023-01-15", value: 100},
  {date: "2023-02-15", value: 120},
  {date: "2023-03-15", value: 115}
];

Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: d => new Date(d.date),  // Parse string to Date
      y: "value",
      stroke: "steelblue",
      strokeWidth: 2
    })
  ]
}).display();
```

## Custom Time Scale

Configure temporal axis:

```javascript
const data = [
  {time: new Date("2023-01-01T00:00"), value: 10},
  {time: new Date("2023-01-01T06:00"), value: 15},
  {time: new Date("2023-01-01T12:00"), value: 20},
  {time: new Date("2023-01-01T18:00"), value: 12}
];

Plot.plot({
  x: {
    type: "utc",
    ticks: "6 hours",
    label: "Time of day"
  },
  marks: [
    Plot.lineY(data, {
      x: "time",
      y: "value",
      stroke: "steelblue",
      curve: "step"  // Step function
    })
  ]
}).display();
```

## Key Patterns

### Basic Line Chart
```javascript
Plot.lineY(data, {
  x: "date",  // Date column
  y: "value",
  stroke: "color",
  strokeWidth: 2
})
```

### Area Chart
```javascript
Plot.areaY(data, {
  x: "date",
  y: "value",
  fill: "steelblue",
  fillOpacity: 0.3
})
```

### Multiple Series
```javascript
// Color by category
Plot.lineY(data, {
  x: "date",
  y: "value",
  stroke: "category"
})
```

### Stacking
```javascript
// Stacked area
Plot.areaY(data, Plot.stackY({
  x: "date",
  y: "value",
  fill: "category"
}))

// Normalized (100%)
Plot.areaY(data, Plot.stackY(Plot.normalizeY({...})))
```

### Moving Average (Window Transform)
```javascript
Plot.lineY(data, Plot.windowY(
  {k: 7},  // Window size
  {x: "date", y: "value"}
))
```

### Curve Interpolation
```javascript
{
  curve: "linear",      // Straight lines (default)
  curve: "step",        // Step function
  curve: "step-after",  // Step after
  curve: "step-before", // Step before
  curve: "basis",       // Smooth B-spline
  curve: "cardinal",    // Cardinal spline
  curve: "catmull-rom", // Catmull-Rom spline
  curve: "natural"      // Natural cubic spline
}
```

### Date Formatting
Plot automatically formats dates. Customize with scale options:
```javascript
{
  x: {
    type: "utc",           // UTC time scale
    ticks: "month",        // Tick interval
    tickFormat: "%b %Y"    // Custom format
  }
}
```

## Related Examples
- [scatterplot.md](scatterplot.md) - Point-based temporal data
- [bar-chart.md](bar-chart.md) - Temporal bar charts
- [faceted-plot.md](faceted-plot.md) - Multiple time series in small multiples

## Reference
- [reference/marks.md](../marks.md) - Line and area mark options
- [reference/transforms.md](../transforms.md) - Window transform for moving averages
- [reference/scales.md](../scales.md) - Time scale configuration
