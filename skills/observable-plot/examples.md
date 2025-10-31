# Observable Plot Examples

This file provides a basic getting-started example. For more specialized examples, see the individual files in the `examples/` directory below.

## Basic Scatterplot Example

This example demonstrates the fundamental pattern for creating a Plot visualization: define your data, specify marks with channel encodings, and render the plot.

```javascript
import * as Plot from "@observablehq/plot";

// Sample data: array of objects (tidy data format)
const data = [
  {temperature: 15, sales: 30, season: "winter"},
  {temperature: 20, sales: 45, season: "spring"},
  {temperature: 25, sales: 60, season: "spring"},
  {temperature: 30, sales: 85, season: "summer"},
  {temperature: 32, sales: 90, season: "summer"},
  {temperature: 18, sales: 35, season: "fall"},
  {temperature: 22, sales: 50, season: "fall"},
  {temperature: 12, sales: 25, season: "winter"}
];

// Create the plot
const plot = Plot.plot({
  // Plot-level options
  width: 640,
  height: 400,
  marginLeft: 60,

  // Configure the color scale
  color: {
    legend: true,
    scheme: "tableau10"
  },

  // Add marks (visual elements)
  marks: [
    // Grid for easier reading
    Plot.gridX(),
    Plot.gridY(),

    // Horizontal rule at y=0
    Plot.ruleY([0]),

    // Scatterplot dots
    Plot.dot(data, {
      x: "temperature",
      y: "sales",
      fill: "season",    // Color by season
      r: 6,              // Radius of dots
      tip: true          // Show tooltip on hover
    })
  ]
});

// Add to document
document.body.appendChild(plot);
```

**Key concepts demonstrated**:
- Tidy data format (array of objects)
- Channel encodings (x, y, fill)
- Multiple marks (grid, rule, dot)
- Automatic scales and axes
- Built-in interactivity (tip: true)

## All Examples

Browse examples by visualization type:

### Basic Visualizations
- [Scatterplot](reference/examples/scatterplot.md) - Scatterplots with various encodings (size, color, shape)
- [Bar Chart](reference/examples/bar-chart.md) - Vertical and horizontal bars with grouping and stacking
- [Time Series](reference/examples/time-series.md) - Line charts for temporal data with moving averages

### Categorical & Comparative
- [Diverging Stacked Bars](reference/examples/diverging-stacked-bars.md) - Likert scales, sentiment analysis, survey responses
- [Population Pyramid](reference/examples/population-pyramid.md) - Age and gender demographic distributions
- [Waffle Charts](reference/examples/waffle-charts.md) - Unit-based visualizations for proportions
- [Heatmaps](reference/examples/heatmaps.md) - Matrix visualizations with color encoding

### Statistical & Density
- [Hexbin Heatmap](reference/examples/hexbin-heatmap.md) - Hexagonal binning for dense scatterplots
- [Density Contour](reference/examples/density-contour.md) - Density estimation and contour plots

### Network & Relational
- [Network Diagrams](reference/examples/network-diagrams.md) - Arrows, links, trees, and flow visualizations
- [Vector Fields](reference/examples/vector-fields.md) - Directional data and wind maps

### Geographic Visualizations
- [Choropleth Map](reference/examples/choropleth-map.md) - Filled geographic regions with data encoding

### Advanced Compositions
- [Faceted Plot](reference/examples/faceted-plot.md) - Small multiples using fx/fy faceting
- [Interactive Tips](reference/examples/interactive-tips.md) - Interactive tooltips and crosshairs

## Example Categories

### By Mark Type
- **Dot marks**: [Scatterplot](reference/examples/scatterplot.md), [Hexbin Heatmap](reference/examples/hexbin-heatmap.md)
- **Bar marks**: [Bar Chart](reference/examples/bar-chart.md), [Diverging Stacked Bars](reference/examples/diverging-stacked-bars.md), [Population Pyramid](reference/examples/population-pyramid.md)
- **Line marks**: [Time Series](reference/examples/time-series.md)
- **Area marks**: [Time Series](reference/examples/time-series.md)
- **Cell marks**: [Waffle Charts](reference/examples/waffle-charts.md), [Heatmaps](reference/examples/heatmaps.md)
- **Geo marks**: [Choropleth Map](reference/examples/choropleth-map.md)
- **Arrow/Link marks**: [Network Diagrams](reference/examples/network-diagrams.md)
- **Vector marks**: [Vector Fields](reference/examples/vector-fields.md)

### By Transform
- **Bin transform**: [Hexbin Heatmap](reference/examples/hexbin-heatmap.md), [Bar Chart](reference/examples/bar-chart.md)
- **Group transform**: [Bar Chart](reference/examples/bar-chart.md)
- **Stack transform**: [Bar Chart](reference/examples/bar-chart.md), [Diverging Stacked Bars](reference/examples/diverging-stacked-bars.md)
- **Window transform**: [Time Series](reference/examples/time-series.md)
- **Hexbin transform**: [Hexbin Heatmap](reference/examples/hexbin-heatmap.md)

### By Feature
- **Faceting**: [Faceted Plot](reference/examples/faceted-plot.md)
- **Interactivity**: [Interactive Tips](reference/examples/interactive-tips.md)
- **Multiple layers**: Most examples demonstrate layering
- **Color scales**: [Scatterplot](reference/examples/scatterplot.md), [Heatmaps](reference/examples/heatmaps.md), [Choropleth Map](reference/examples/choropleth-map.md)
- **Projections**: [Choropleth Map](reference/examples/choropleth-map.md), [Vector Fields](reference/examples/vector-fields.md)
- **Diverging patterns**: [Diverging Stacked Bars](reference/examples/diverging-stacked-bars.md), [Population Pyramid](reference/examples/population-pyramid.md)

## Creating Your Own Visualizations

Start with these steps:

1. **Prepare tidy data**: Array of objects with consistent properties
2. **Choose marks**: Select visual elements (dot, bar, line, etc.)
3. **Map channels**: Assign data properties to visual channels (x, y, fill, etc.)
4. **Add transforms**: Use Plot transforms for aggregation/calculation
5. **Layer marks**: Combine multiple marks for rich visualizations
6. **Configure scales**: Adjust domains, ranges, and color schemes as needed

For detailed API documentation, see the [reference/](reference/) directory.
