# Interactive Tips and Crosshair Examples

Observable Plot provides built-in interactivity through tooltips (tips) and crosshairs. These features are declarative and require no external JavaScript.

## Basic Tooltip

Add `tip: true` to show tooltips on hover:

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {name: "Alice", age: 25, score: 85},
  {name: "Bob", age: 30, score: 92},
  {name: "Carol", age: 28, score: 78},
  {name: "Dave", age: 35, score: 88}
];

Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "age",
      y: "score",
      fill: "steelblue",
      r: 6,
      tip: true  // Enable tooltips
    })
  ]
}).display();
```

## Custom Tooltip Channels

Control what appears in tooltips using `channels`:

```javascript
const data = [
  {x: 10, y: 20, category: "A", details: "Important data point"},
  {x: 15, y: 35, category: "B", details: "Another observation"},
  {x: 20, y: 25, category: "A", details: "Third point"}
];

Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "category",
      r: 8,
      tip: true,
      channels: {
        Category: "category",
        Details: "details",
        "X Value": "x",
        "Y Value": "y"
      }
    })
  ]
}).display();
```

## Tooltip with Calculated Values

Show computed values in tooltips:

```javascript
const data = [
  {product: "Laptop", price: 1200, quantity: 5},
  {product: "Phone", price: 800, quantity: 10},
  {product: "Tablet", price: 500, quantity: 7}
];

Plot.plot({
  marks: [
    Plot.barY(data, {
      x: "product",
      y: "quantity",
      fill: "steelblue",
      tip: true,
      channels: {
        Product: "product",
        Quantity: "quantity",
        Price: "price",
        Revenue: d => d.price * d.quantity
      }
    })
  ]
}).display();
```

## Crosshair

Show crosshair lines on hover:

```javascript
const data = Array.from({length: 50}, (_, i) => ({
  x: i,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "x",
      y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.crosshair(data, {
      x: "x",
      y: "y"
    })
  ]
}).display();
```

## Crosshair with Tooltip

Combine crosshair and tooltip:

```javascript
const data = [
  {date: new Date("2023-01-01"), value: 100},
  {date: new Date("2023-02-01"), value: 120},
  {date: new Date("2023-03-01"), value: 115},
  {date: new Date("2023-04-01"), value: 140},
  {date: new Date("2023-05-01"), value: 135}
];

Plot.plot({
  marks: [
    Plot.gridY(),
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.dot(data, {
      x: "date",
      y: "value",
      fill: "steelblue",
      r: 4
    }),
    Plot.crosshair(data, {
      x: "date",
      y: "value",
      tip: true
    })
  ]
}).display();
```

## Pointer Transform

Use pointer transform for nearest-point tooltips:

```javascript
const data = Array.from({length: 100}, (_, i) => ({
  x: i,
  y: 50 + Math.sin(i / 10) * 20 + Math.random() * 5
}));

Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "x",
      y: "y",
      stroke: "lightgray",
      strokeWidth: 1
    }),
    Plot.dot(data, Plot.pointer({
      x: "x",
      y: "y",
      fill: "red",
      r: 6,
      tip: true
    }))
  ]
}).display();
```

## Multiple Series with Tips

Show tooltips for multiple series:

```javascript
const data = [
  {month: "Jan", series: "A", value: 100},
  {month: "Jan", series: "B", value: 90},
  {month: "Feb", series: "A", value: 120},
  {month: "Feb", series: "B", value: 95},
  {month: "Mar", series: "A", value: 115},
  {month: "Mar", series: "B", value: 110}
];

Plot.plot({
  color: {legend: true},
  marks: [
    Plot.lineY(data, {
      x: "month",
      y: "value",
      stroke: "series",
      strokeWidth: 2,
      tip: true
    }),
    Plot.dot(data, {
      x: "month",
      y: "value",
      fill: "series",
      r: 4,
      tip: true,
      channels: {
        Series: "series",
        Month: "month",
        Value: "value"
      }
    })
  ]
}).display();
```

## Rule-based Tooltip

Show tooltip at a specific position:

```javascript
const data = [
  {category: "A", value: 100, threshold: 80},
  {category: "B", value: 120, threshold: 110},
  {category: "C", value: 90, threshold: 95}
];

Plot.plot({
  marks: [
    Plot.barY(data, {
      x: "category",
      y: "value",
      fill: "steelblue",
      tip: true
    }),
    Plot.ruleY(data, {
      x: "category",
      y: "threshold",
      stroke: "red",
      strokeWidth: 2,
      strokeDasharray: "4,4",
      tip: true,
      channels: {
        Category: "category",
        Threshold: "threshold"
      }
    })
  ]
}).display();
```

## Text Tips

Use text mark for custom annotations:

```javascript
const data = [
  {x: 10, y: 20, label: "Point A", note: "First observation"},
  {x: 20, y: 35, label: "Point B", note: "Outlier detected"},
  {x: 30, y: 25, label: "Point C", note: "Normal value"}
];

Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "steelblue",
      r: 8,
      tip: true,
      channels: {
        Label: "label",
        Note: "note"
      }
    }),
    Plot.text(data, {
      x: "x",
      y: "y",
      text: "label",
      dy: -15,
      fontSize: 10,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Geographic Tips

Tooltips on maps:

```javascript
const cities = [
  {name: "New York", lon: -74.0, lat: 40.7, population: 8.3},
  {name: "Los Angeles", lon: -118.2, lat: 34.0, population: 3.9},
  {name: "Chicago", lon: -87.6, lat: 41.9, population: 2.7}
];

Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo({type: "Sphere"}, {fill: "lightblue"}),
    Plot.dot(cities, {
      x: "lon",
      y: "lat",
      r: d => Math.sqrt(d.population) * 3,
      fill: "steelblue",
      stroke: "white",
      strokeWidth: 2,
      tip: true,
      channels: {
        City: "name",
        Population: d => `${d.population}M`
      }
    })
  ]
}).display();
```

## Tooltip Formatting

Format tooltip values:

```javascript
const data = [
  {product: "A", revenue: 1234567, growth: 0.156},
  {product: "B", revenue: 9876543, growth: -0.023},
  {product: "C", revenue: 5432109, growth: 0.089}
];

Plot.plot({
  marks: [
    Plot.barY(data, {
      x: "product",
      y: "revenue",
      fill: "steelblue",
      tip: true,
      channels: {
        Product: "product",
        Revenue: d => `$${(d.revenue / 1000000).toFixed(2)}M`,
        Growth: d => `${(d.growth * 100).toFixed(1)}%`
      }
    })
  ]
}).display();
```

## Conditional Tips

Show tips only for certain data:

```javascript
const data = [
  {x: 1, y: 10, important: true},
  {x: 2, y: 20, important: false},
  {x: 3, y: 15, important: true},
  {x: 4, y: 25, important: false}
];

Plot.plot({
  marks: [
    // All points
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "lightgray",
      r: 4
    }),

    // Important points with tips
    Plot.dot(data.filter(d => d.important), {
      x: "x",
      y: "y",
      fill: "red",
      r: 6,
      tip: true,
      channels: {
        X: "x",
        Y: "y",
        Important: "important"
      }
    })
  ]
}).display();
```

## Key Patterns

### Basic Tooltip
```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  tip: true  // Show all encoded channels
})
```

### Custom Channels
```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  tip: true,
  channels: {
    "Display Name": "dataColumn",
    "Computed": d => d.a + d.b
  }
})
```

### Crosshair
```javascript
Plot.crosshair(data, {
  x: "x",
  y: "y",
  tip: true  // Optional tooltip with crosshair
})
```

### Pointer Transform
```javascript
// Highlight nearest point
Plot.dot(data, Plot.pointer({
  x: "x",
  y: "y",
  fill: "red",
  tip: true
}))
```

### Tip Options
```javascript
{
  tip: true,              // Enable tooltip
  tip: {
    format: {
      x: ".2f",          // Format x values
      y: ".0%"           // Format y as percentage
    }
  }
}
```

### When to Use
- **tip: true**: Show data values on hover
- **crosshair**: Track position across plot
- **pointer**: Highlight nearest point
- **channels**: Custom tooltip content

## Related Examples
- [scatterplot.md](scatterplot.md) - Tooltips on scatterplots
- [bar-chart.md](bar-chart.md) - Tooltips on bar charts
- [choropleth-map.md](choropleth-map.md) - Geographic tooltips

## Reference
- [reference/interactions.md](../interactions.md) - Complete interaction options
- [reference/marks.md](../marks.md) - Tip mark documentation
- [reference/geographic.md](../geographic.md) - Geographic interaction and tooltips on maps
