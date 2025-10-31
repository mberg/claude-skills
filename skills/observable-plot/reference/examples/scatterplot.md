# Scatterplot Examples

Scatterplots visualize relationships between two continuous variables using the `Plot.dot()` mark. This example demonstrates various encodings and styling options.

## Basic Scatterplot

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {x: 1, y: 2},
  {x: 2, y: 5},
  {x: 3, y: 3},
  {x: 4, y: 7},
  {x: 5, y: 4}
];

Plot.plot({
  marks: [
    Plot.dot(data, {x: "x", y: "y"})
  ]
}).display();
```

## Color Encoding

Map a categorical variable to color:

```javascript
const data = [
  {mpg: 18, weight: 3500, cylinders: 8},
  {mpg: 24, weight: 2800, cylinders: 4},
  {mpg: 20, weight: 3200, cylinders: 6},
  {mpg: 30, weight: 2200, cylinders: 4},
  {mpg: 15, weight: 4000, cylinders: 8},
  {mpg: 28, weight: 2400, cylinders: 4}
];

Plot.plot({
  color: {
    scheme: "category10",
    legend: true
  },
  marks: [
    Plot.dot(data, {
      x: "weight",
      y: "mpg",
      fill: "cylinders",  // Color by cylinders
      r: 5
    })
  ]
}).display();
```

## Size Encoding

Map a continuous variable to dot size:

```javascript
const data = [
  {gdp: 5000, lifeExpectancy: 68, population: 500000, country: "A"},
  {gdp: 15000, lifeExpectancy: 75, population: 2000000, country: "B"},
  {gdp: 30000, lifeExpectancy: 80, population: 10000000, country: "C"},
  {gdp: 8000, lifeExpectancy: 70, population: 1000000, country: "D"}
];

Plot.plot({
  r: {range: [2, 20]},  // Control size range
  color: {scheme: "blues"},
  marks: [
    Plot.dot(data, {
      x: "gdp",
      y: "lifeExpectancy",
      r: "population",    // Size by population
      fill: "population", // Also color by population
      fillOpacity: 0.7,
      tip: true           // Show tooltip
    })
  ]
}).display();
```

## Multiple Encodings

Combine color, size, and shape encodings:

```javascript
const data = [
  {price: 100, sales: 50, region: "North", season: "winter"},
  {price: 120, sales: 65, region: "South", season: "spring"},
  {price: 90, sales: 45, region: "East", season: "summer"},
  {price: 110, sales: 70, region: "West", season: "fall"},
  {price: 105, sales: 55, region: "North", season: "spring"},
  {price: 95, sales: 60, region: "South", season: "winter"}
];

Plot.plot({
  color: {
    legend: true,
    domain: ["North", "South", "East", "West"]
  },
  marks: [
    Plot.gridX(),
    Plot.gridY(),
    Plot.dot(data, {
      x: "price",
      y: "sales",
      fill: "region",
      r: 8,
      stroke: "black",
      strokeWidth: 1,
      fillOpacity: 0.8,
      tip: true
    })
  ]
}).display();
```

## With Regression Line

Layer a regression line with scatterplot dots:

```javascript
import * as Plot from "@observablehq/plot";

const data = [
  {x: 1, y: 2.3},
  {x: 2, y: 4.1},
  {x: 3, y: 5.8},
  {x: 4, y: 8.2},
  {x: 5, y: 9.7},
  {x: 6, y: 12.1}
];

Plot.plot({
  marks: [
    // Background grid
    Plot.gridX(),
    Plot.gridY(),

    // Scatterplot dots
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "steelblue",
      r: 5
    }),

    // Linear regression line
    Plot.linearRegressionY(data, {
      x: "x",
      y: "y",
      stroke: "red",
      strokeWidth: 2
    })
  ]
}).display();
```

## Logarithmic Scales

Use log scales for data spanning multiple orders of magnitude:

```javascript
const data = [
  {gdp: 500, population: 100000},
  {gdp: 5000, population: 1000000},
  {gdp: 50000, population: 10000000},
  {gdp: 25000, population: 5000000},
  {gdp: 1000, population: 500000}
];

Plot.plot({
  x: {type: "log"},
  y: {type: "log"},
  marks: [
    Plot.gridX({ticks: 10}),
    Plot.gridY({ticks: 10}),
    Plot.dot(data, {
      x: "gdp",
      y: "population",
      r: 6,
      fill: "steelblue"
    })
  ]
}).display();
```

## With Labels

Add text labels to points:

```javascript
const data = [
  {company: "Apple", revenue: 365, profit: 94},
  {company: "Google", revenue: 257, profit: 76},
  {company: "Microsoft", revenue: 168, profit: 61},
  {company: "Amazon", revenue: 386, profit: 21}
];

Plot.plot({
  marks: [
    Plot.gridX(),
    Plot.gridY(),

    // Dots
    Plot.dot(data, {
      x: "revenue",
      y: "profit",
      fill: "steelblue",
      r: 8
    }),

    // Labels
    Plot.text(data, {
      x: "revenue",
      y: "profit",
      text: "company",
      dy: -12,  // Offset above the dot
      fontSize: 10
    })
  ]
}).display();
```

## Key Patterns

### Encoding Channels
- `x`: Horizontal position (required)
- `y`: Vertical position (required)
- `fill`: Fill color
- `stroke`: Stroke color
- `r`: Radius (size)
- `fillOpacity`: Transparency
- `strokeWidth`: Outline thickness

### Common Options
- `tip: true`: Add interactive tooltips
- `r: number`: Fixed radius for all dots
- `r: "column"`: Variable radius from data
- `fill: "color"`: Fixed color
- `fill: "column"`: Color from data

### Scale Configuration
```javascript
Plot.plot({
  color: {
    scheme: "viridis",    // Color scheme
    legend: true,          // Show legend
    domain: [min, max]     // Explicit domain
  },
  r: {
    range: [2, 20]         // Size range
  }
})
```

### Layering
Order matters - later marks draw on top:
1. Background (grid, frame)
2. Reference lines (ruleY, ruleX)
3. Data marks (dot, bar, line)
4. Annotations (text, tip)

## Related Examples
- [interactive-tips.md](interactive-tips.md) - Advanced tooltip interactions
- [faceted-plot.md](faceted-plot.md) - Multiple scatterplots in small multiples
- [hexbin-heatmap.md](hexbin-heatmap.md) - For dense scatterplots with many points

## Reference
- [reference/marks.md](../marks.md) - Complete dot mark options
- [reference/scales.md](../scales.md) - Color schemes and scale types
