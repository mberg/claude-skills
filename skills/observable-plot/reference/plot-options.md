# Plot Options Reference

Configure plot-level settings including dimensions, margins, styling, and layout.

## Dimensions

### Width and Height

```javascript
Plot.plot({
  width: 640,   // Plot width in pixels
  height: 400,  // Plot height in pixels
  marks: [...]
})
```

**Auto-sizing**:
```javascript
{width: undefined}  // Use container width
{height: undefined}  // Use container height
```

### Aspect Ratio

Maintain aspect ratio:

```javascript
{
  width: 640,
  aspectRatio: 16/9  // Height determined by aspect ratio
}
```

## Margins

Space around the plot area:

```javascript
Plot.plot({
  marginTop: 20,
  marginRight: 30,
  marginBottom: 40,
  marginLeft: 50,
  marks: [...]
})
```

**Shorthand**:
```javascript
{margin: 40}  // All margins
{marginLeft: 60, marginRight: 60}  // Specific sides
```

**Auto margins** (default):
```javascript
{marginLeft: undefined}  // Auto-compute based on axis labels
```

## Padding and Insets

### Plot Padding

Space between plot frame and marks:

```javascript
{
  padding: 0.1  // 10% padding on all sides
}
```

### Insets

Space between plot edges and marks (in pixels):

```javascript
{
  inset: 10,           // All sides
  insetTop: 10,
  insetRight: 10,
  insetBottom: 10,
  insetLeft: 10
}
```

## Style

### Colors

```javascript
{
  style: {
    background: "white",
    color: "black",
    fontSize: 12,
    fontFamily: "sans-serif"
  }
}
```

### Grid

```javascript
{
  grid: true,     // Show x and y grids
  gridColor: "lightgray",
  gridOpacity: 0.5
}
```

Individual grid control:
```javascript
{
  x: {grid: true},
  y: {grid: true}
}
```

## Axes

### Axis Configuration

```javascript
{
  x: {
    label: "X Axis Label",
    ticks: 10,
    tickFormat: ".2f",
    axis: "bottom"  // or "top", "both", null
  },
  y: {
    label: "Y Axis Label →",
    ticks: 5,
    axis: "left"  // or "right", "both", null
  }
}
```

### Hide Axes

```javascript
{
  x: {axis: null},
  y: {axis: null}
}
```

### Axis Placement

```javascript
{
  x: {axis: "top"},     // Top instead of bottom
  y: {axis: "right"}    // Right instead of left
}
```

## Titles and Captions

### Title

```javascript
{
  title: "Plot Title",
  subtitle: "Additional context"
}
```

### Caption

```javascript
{
  caption: "Source: Data source information"
}
```

## Marks Array

The main content - ordered list of visual marks:

```javascript
{
  marks: [
    Plot.gridY(),
    Plot.ruleY([0]),
    Plot.barY(data, {x: "category", y: "value"}),
    Plot.text(labels, {x: "x", y: "y", text: "label"})
  ]
}
```

Order matters - later marks draw on top.

## Faceting

### Facet Configuration

```javascript
{
  fx: {
    label: "Horizontal Facets",
    domain: ["A", "B", "C"],
    padding: 0.1
  },
  fy: {
    label: "Vertical Facets",
    domain: ["X", "Y"],
    padding: 0.05
  },
  marks: [...]
}
```

See [faceting.md](faceting.md) for details.

## Projections

### Geographic Projection

```javascript
{
  projection: "albers-usa",
  marks: [Plot.geo(geojson)]
}
```

**With options**:
```javascript
{
  projection: {
    type: "orthographic",
    rotate: [-100, -30]
  },
  marks: [...]
}
```

See [projections.md](projections.md) for details.

## Color Configuration

### Global Color Scale

```javascript
{
  color: {
    scheme: "viridis",
    legend: true,
    label: "Color Scale Label",
    domain: [0, 100],
    range: ["white", "red"]
  },
  marks: [...]
}
```

See [scales.md](scales.md) for details.

## Layout

### Document Integration

```javascript
const plot = Plot.plot({...});
document.body.appendChild(plot);
```

**With display()**:
```javascript
Plot.plot({...}).display();
```

### Responsive Sizing

```javascript
{
  width: window.innerWidth * 0.8,
  height: window.innerHeight * 0.6
}
```

## Accessibility

### ARIA Labels

```javascript
{
  ariaLabel: "Bar chart showing sales by region",
  ariaDescription: "Chart displays quarterly sales data across four regions"
}
```

### Role

```javascript
{
  role: "img",
  ariaLabel: "Visualization description"
}
```

## Custom Styling

### CSS Classes

```javascript
{
  className: "custom-plot",
  style: {
    background: "#f9f9f9",
    borderRadius: "8px",
    padding: "20px"
  }
}
```

### Inline Styles

```javascript
{
  style: {
    fontSize: "14px",
    fontFamily: "Georgia, serif",
    color: "#333"
  }
}
```

## Common Configurations

### Minimal Plot

```javascript
Plot.plot({
  marks: [
    Plot.dot(data, {x: "x", y: "y"})
  ]
})
```

### Fully Configured Plot

```javascript
Plot.plot({
  // Dimensions
  width: 800,
  height: 500,

  // Margins
  marginTop: 30,
  marginRight: 40,
  marginBottom: 50,
  marginLeft: 60,

  // Title and caption
  title: "Sales Performance",
  subtitle: "Q1 2023",
  caption: "Source: Internal sales data",

  // Axes
  x: {
    label: "Month",
    grid: true
  },
  y: {
    label: "Revenue ($)",
    tickFormat: "$~s"
  },

  // Color scale
  color: {
    scheme: "category10",
    legend: true,
    label: "Product Line"
  },

  // Style
  style: {
    background: "white",
    fontSize: 12
  },

  // Marks
  marks: [
    Plot.gridY(),
    Plot.ruleY([0]),
    Plot.lineY(data, {
      x: "month",
      y: "revenue",
      stroke: "product"
    })
  ]
})
```

### Dashboard Grid

```javascript
Plot.plot({
  fx: {label: "Region"},
  fy: {label: "Quarter"},
  width: 1200,
  height: 800,
  marginLeft: 60,
  color: {scheme: "blues", legend: true},
  marks: [
    Plot.cell(data, {
      fx: "region",
      fy: "quarter",
      x: "month",
      y: "product",
      fill: "revenue"
    })
  ]
})
```

## Plot Methods

### plot.scale(name)

Access computed scales:

```javascript
const plot = Plot.plot({...});
const colorScale = plot.scale("color");
```

### plot.legend(name, options)

Extract legend as separate element:

```javascript
const plot = Plot.plot({...});
const legend = plot.legend("color");
document.body.appendChild(legend);
```

## Performance Options

### Large Datasets

```javascript
{
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      r: 1,  // Small points for performance
      opacity: 0.1  // Transparency for density
    })
  ]
}
```

Consider aggregation for >10k points:
```javascript
{
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      bandwidth: 20
    })
  ]
}
```

## Default Values

When options are omitted, Plot uses sensible defaults:

- **width**: 640
- **height**: Auto based on aspect ratio or 400
- **margins**: Auto-computed based on axes
- **style**: System defaults
- **Scales**: Auto-inferred from data

## Related Documentation
- [scales.md](scales.md) - Scale configuration
- [faceting.md](faceting.md) - Facet configuration
- [projections.md](projections.md) - Geographic projections
- [marks.md](marks.md) - Mark options
