---
title: Observable Plot
description: Create data visualizations using Observable Plot's declarative grammar of graphics
version: 1.0.0
tags: [visualization, data, plot, chart, graphics, d3]
---

# Observable Plot

Observable Plot is a JavaScript library for exploratory data visualization. It uses a declarative grammar of graphics to create meaningful visualizations quickly by composing marks, scales, and transforms.

## What is Observable Plot?

Observable Plot helps you turn data into visualizations by mapping data columns to visual properties. Instead of specifying chart types, you compose visual elements (marks) with data transformations (transforms) and encodings (scales).

**Key principle**: Maximize configuration, minimize external JavaScript. Plot handles data processing, layout, axes, and legends through its declarative API.

## Five Core Concepts

### 1. Marks

Marks are visual elements that represent data. Plot provides 30+ mark types:

- **Point marks**: `dot`, `image`, `text`
- **Rectangular marks**: `barX`, `barY`, `cell`, `rect`
- **Line marks**: `line`, `lineX`, `lineY`, `area`, `areaX`, `areaY`
- **Reference marks**: `ruleX`, `ruleY`, `tickX`, `tickY`, `frame`, `grid`
- **Geographic marks**: `geo`, `sphere`, `graticule`
- **Relational marks**: `arrow`, `link`, `tree`, `vector`
- **Density marks**: `contour`, `density`, `hexgrid`, `raster`
- **Statistical marks**: `boxX`, `boxY`, `linearRegressionY`
- **Utility marks**: `axis`, `tip`

### 2. Scales

Scales map abstract data values to visual values (position, color, size, etc.). Plot automatically infers scales from your data and mark specifications.

**Scale types**:
- Continuous: `linear`, `log`, `sqrt`, `pow`, `time`, `utc`
- Discrete: `point`, `band`, `ordinal`
- Color: sequential, diverging, categorical, cyclical schemes

### 3. Transforms

Transforms process data within the Plot specification, eliminating the need for external data wrangling:

- **Aggregation**: `bin`, `hexbin`, `group`
- **Statistical**: `normalize`, `window` (moving averages)
- **Positional**: `stack`, `dodge`, `shift`
- **Filtering**: `filter`, `select`
- **Ordering**: `sort`

### 4. Layering

Compose complex visualizations by layering multiple marks. Each mark can have its own data, transforms, and encodings while sharing the same coordinate system.

### 5. Tidy Data

Plot works best with tidy data: arrays of objects where each object represents one observation with consistent properties.

```javascript
// Tidy data format
const data = [
  {name: "Alice", age: 25, score: 85},
  {name: "Bob", age: 30, score: 92},
  {name: "Carol", age: 28, score: 78}
];
```

## Quick Start

```javascript
import * as Plot from "@observablehq/plot";

// Simple scatterplot
const data = [
  {x: 1, y: 2, category: "A"},
  {x: 2, y: 5, category: "B"},
  {x: 3, y: 3, category: "A"},
  {x: 4, y: 7, category: "B"}
];

const plot = Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "category",
      r: 5
    })
  ]
});

document.body.appendChild(plot);
```

## Interactive Viewer

The Observable Plot skill includes an interactive live editor and viewer for developing visualizations:

### Starting the Viewer

```bash
cd skills/observable-plot/scripts
uv run plot-viewer
```

This launches a split-pane editor with live preview on http://localhost:8765

**Options:**
- `--port 8080` - Use a different port
- `--no-browser` - Don't auto-open browser
- `--create-example` - Create example temp file on startup

### Using with Claude

Claude can write visualization code that automatically loads in the viewer:

1. Claude writes code to `/tmp/observable-plot-code.js`
2. Open the viewer: `uv run plot-viewer`
3. Click "Load Temp File" to see the visualization
4. Edit code and see live updates as you type

**Example workflow:**
```javascript
// Claude writes this to /tmp/observable-plot-code.js
const data = [
  {category: "A", value: 10},
  {category: "B", value: 20},
  {category: "C", value: 15}
];

return Plot.plot({
  marks: [
    Plot.barY(data, {x: "category", y: "value"})
  ]
})
```

The code must return a `Plot.plot()` result using `return` and has access to `Plot` and `d3` globals. Click "Load Temp File" in the viewer to render it.

### Viewer Features

- **Live Preview**: Chart updates as you type (500ms debounce)
- **Monaco Editor**: Full-featured code editor with syntax highlighting
- **Built-in Examples**: Load sample charts with one click
- **Resizable Panes**: Drag divider to adjust layout
- **Error Display**: See error messages clearly when code fails
- **Keyboard Shortcut**: ⌘+Enter to manually run code

## Sample Datasets

Observable provides a collection of real-world datasets perfect for creating example visualizations. These include datasets for time series (stock prices, weather, temperature), categorical data (letters, athletes, cars), and geographic data (US counties, state capitals).

**See**: [reference/datasets.md](reference/datasets.md) for complete dataset catalog with direct URLs and usage examples.

### Using Sample Datasets Correctly

When creating visualizations with real data, **always use the curated datasets from `reference/datasets.md`**. Do not attempt to fetch arbitrary URLs or datasets from other sources.

**Before creating a visualization with external data, verify the data structure**:

```bash
curl -s "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/olympians.csv" | head -20
```

This shows you:
- The actual column names (critical for writing correct Plot code)
- Data types and formats
- Whether the data loads successfully
- Sample values to understand the data

**Proper pattern for CSV files**:

```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/olympians.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

return Plot.plot({
  marks: [
    Plot.dot(data, {x: "weight", y: "height", fill: "sex"})
  ]
});
```

**Key points**:
1. Use URLs from [reference/datasets.md](reference/datasets.md) - these are verified and reliable
2. **Always verify external data with `curl | head -20` before creating the plot**
3. For CSV files: `fetch(url).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType))`
4. For JSON files: `fetch(url).then(r => r.json())`
5. Always use `d3.autoType` to automatically infer numeric and date types
6. Check the dataset columns in datasets.md before writing your visualization code

**Example datasets with common use cases**:
- **olympians.csv** (Olympic athletes): Scatterplots, grouped analysis, distributions
- **penguins.csv** (Penguin measurements): Species comparison, statistical analysis
- **aapl.csv** (Apple stock): Time series, line charts, price trends
- **cars.csv** (Automobile data): Correlation analysis, grouped comparisons
- **diamonds.csv** (Diamond data): Price analysis, quality visualizations

## Common Tasks

### Creating Visualizations

- **Scatterplots**: Use `Plot.dot()` with x/y channels
- **Bar charts**: Use `Plot.barY()` or `Plot.barX()` with grouping/stacking
- **Line charts**: Use `Plot.line()` with x/y channels, optional `curve` option
- **Heatmaps**: Use `Plot.cell()` with fill encoding or `Plot.hexbin()` for hexagonal binning
- **Geographic maps**: Use `Plot.geo()` with GeoJSON data and projections
- **Small multiples**: Use `fx`/`fy` faceting options

### Data Transformations

See [reference/transforms.md](reference/transforms.md) for detailed transform documentation.

### Styling and Customization

See [reference/plot-options.md](reference/plot-options.md) for layout, margins, and dimensions.
See [reference/scales.md](reference/scales.md) for color schemes and scale configuration.

### Interactivity

See [reference/interactions.md](reference/interactions.md) for tips, crosshairs, and pointer interactions.

## Essential Constraints

### Browser Compatibility

Observable Plot requires modern JavaScript (ES2020+) and works in:
- Chrome/Edge 80+
- Firefox 75+
- Safari 13.1+
- Node.js 14+ (for server-side rendering)

### Data Format

- Prefers arrays of objects (tidy data)
- Supports typed arrays for numeric data
- GeoJSON for geographic features
- Dates as Date objects or ISO 8601 strings

### Performance Considerations

- Large datasets (>100k points): Consider `Plot.density()` or `Plot.hexbin()`
- Many categories: Limit color/shape encodings to ~10 categories
- Geographic data: Use appropriate projections and simplify geometries
- Faceting: Limit to reasonable grid sizes (e.g., 3×3 or 4×4)

## Configuration Patterns

Plot emphasizes declarative configuration. Here's the general pattern:

```javascript
Plot.plot({
  // Plot-level options
  width: 640,
  height: 400,
  marginLeft: 50,

  // Color scale configuration
  color: {
    scheme: "viridis",
    legend: true
  },

  // Marks array (order determines layering)
  marks: [
    // Background/reference marks
    Plot.gridY(),
    Plot.ruleY([0]),

    // Data marks with transforms
    Plot.barY(data, Plot.groupX({y: "sum"}, {
      x: "category",
      y: "value",
      fill: "subcategory"
    })),

    // Annotation marks
    Plot.text(labels, {x: "x", y: "y", text: "label"})
  ]
})
```

## Examples

For a basic getting-started example and links to all examples, see [reference/examples.md](reference/examples.md).

Browse examples by category:
- Basic charts (scatterplots, bars, lines)
- Statistical visualizations (density, contours, regression)
- Geographic visualizations (choropleths, projection maps)
- Interactive visualizations (tips, crosshairs)
- Advanced compositions (facets, layers)

## Reference Documentation

Comprehensive reference documentation is available for progressive loading:

- [TABLE_OF_CONTENTS.md](TABLE_OF_CONTENTS.md) - Browse by topic
- [reference/marks.md](reference/marks.md) - All 30 mark types with options
- [reference/transforms.md](reference/transforms.md) - Data transformation patterns
- [reference/scales.md](reference/scales.md) - Scale types and color schemes
- [reference/projections.md](reference/projections.md) - Geographic projections
- [reference/faceting.md](reference/faceting.md) - Small multiples patterns
- [reference/interactions.md](reference/interactions.md) - Interactivity patterns
- [reference/plot-options.md](reference/plot-options.md) - Layout and dimensions
- [reference/common-patterns.md](reference/common-patterns.md) - Recipes for declarative configs

## Design Principles

When helping users create visualizations with Observable Plot:

1. **Prefer declarative over imperative**: Use Plot's built-in transforms instead of pre-processing data externally
2. **Compose don't configure**: Layer simple marks rather than creating complex configurations
3. **Trust the defaults**: Plot makes sensible choices for scales, axes, and legends
4. **Think in channels**: Map data properties to visual channels (x, y, fill, stroke, r, etc.)
5. **Use transforms for aggregation**: Let Plot handle binning, grouping, and stacking
6. **Leverage faceting**: Use fx/fy for small multiples instead of manual iteration
7. **Keep data tidy**: Structure data as arrays of objects with consistent properties

## Learning Resources

- Official documentation: https://observablehq.com/plot/
- Gallery of examples: https://observablehq.com/@observablehq/plot-gallery
- API reference: https://github.com/observablehq/plot
- Getting started guide: https://observablehq.com/plot/getting-started

## Common Pitfalls

1. **Pre-processing data externally**: Use Plot transforms instead (bin, group, stack)
2. **Imperative styling**: Use mark options as data channels (fill: "category" not fill: "#ff0000")
3. **Wrong mark orientation**: Use `barY` for vertical bars, `barX` for horizontal bars
4. **Missing scales**: Explicitly configure scales when defaults don't match your data
5. **Overplotting**: Use `Plot.hexbin()`, `Plot.density()`, or opacity for large datasets
6. **Static legends**: Let Plot generate legends from scale configurations
7. **Manual faceting**: Use fx/fy options instead of creating multiple plots

## Version Information

This skill is based on Observable Plot v0.6.x API. The library is actively maintained and follows semantic versioning.
