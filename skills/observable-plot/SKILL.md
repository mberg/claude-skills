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

**Launch from your working directory** (where you want plots to be created):

```bash
# From your project directory
uv run --directory ~/.claude/skills/observable-plot/scripts plot-viewer --plots-dir $(pwd)/plots
```

Or if you're already in the skills directory structure:

```bash
# Shorter version from within skills directory
uv run --directory observable-plot/scripts plot-viewer --plots-dir $(pwd)/plots
```

This launches a three-pane interface with history sidebar, live preview, and code editor on http://localhost:8765

**The viewer automatically detects if it's already running and just opens a new browser tab.**

**Options:**
- `--plots-dir PATH` - Specify plots directory (default: ./plots)
- `--port 8080` - Use a different port
- `--no-browser` - Don't auto-open browser
- `--create-example` - Create example plot file on startup

### Using with Claude

Claude can write visualization code to JSON files that automatically load in the viewer:

#### Writing Plot Files

**IMPORTANT**: Claude should check its current working directory and write plot files to `$(pwd)/plots/`.

**Workflow:**
1. User launches viewer from their working directory with `--plots-dir $(pwd)/plots`
2. Viewer displays the plots directory it's watching on startup
3. Claude checks its current directory and creates `plots/` subdirectory
4. Claude writes plot JSON files to `plots/filename.json`
5. Viewer automatically detects and displays new plots in the history sidebar

**For Claude:**
1. Check the current directory with `pwd`
2. Ensure the `plots` subdirectory exists with `mkdir -p plots`
3. Write plot files to `plots/filename.json`

The viewer will show which directory it's watching on startup, so you can verify Claude is writing to the correct location.

#### JSON File Format

Claude writes plot files to `$(pwd)/plots/` with this structure:

```json
{
  "name": "Sales Analysis",
  "description": "Monthly revenue by product category",
  "code": "const data = [...]; return Plot.plot({...})",
  "timestamp": "2025-10-31T12:34:56.789Z"
}
```

**Fields:**
- `name` - Descriptive name shown in history (required)
- `description` - Brief description shown in history sidebar (optional)
- `code` - JavaScript code that returns a Plot.plot() result (required)
- `timestamp` - ISO timestamp for tracking creation time (required)

#### File Naming Convention

Use descriptive filenames that make sense:
- `sales-by-category-2025.json`
- `temperature-trends-seattle.json`
- `penguins-body-mass-analysis.json`

Avoid generic names like `plot1.json` or `temp.json`.

#### Example Workflow

**Step 0: Launch the viewer from your working directory**

```bash
cd /Users/mberg/projects/myapp
uv run --directory ~/.claude/skills/observable-plot/scripts plot-viewer --plots-dir $(pwd)/plots
```

The viewer will print: `Watching plots directory: /Users/mberg/projects/myapp/plots`

**Step 1: Check current directory and ensure plots folder exists**

```bash
pwd
# Output: /Users/mberg/projects/myapp

mkdir -p plots
```

**Step 2: Write the plot file**

```bash
cat > plots/sales-analysis-2025.json << 'EOF'
{
  "name": "Sales Analysis",
  "description": "Monthly revenue by product category",
  "code": "const data = [\n  {month: 'Jan', revenue: 1000},\n  {month: 'Feb', revenue: 1200}\n];\n\nreturn Plot.plot({\n  marks: [\n    Plot.barY(data, {x: 'month', y: 'revenue'})\n  ]\n})",
  "timestamp": "2025-10-31T12:34:56.789Z"
}
EOF
```

**Step 3: Viewer automatically detects and loads the new plot**

The viewer polls every 5 seconds for new plots and will automatically:
- Add the plot to the history sidebar
- Load it as the current plot
- Display the visualization

**Step 4: User interaction**

Users can then:
- Switch between plots using the history sidebar
- Edit code in the editor and see live updates
- Save modified plots to new files

### Viewer Features

- **History Sidebar**: Browse all saved plots with names, descriptions, and timestamps
- **Live Preview**: Chart updates as you type (500ms debounce)
- **Monaco Editor**: Full-featured code editor with syntax highlighting
- **File Switching**: Click any plot in history to load it instantly
- **Auto-reload**: Detects new plots automatically (polls every 5 seconds)
- **Resizable Panes**: Drag divider to adjust layout
- **Error Display**: See error messages clearly when code fails
- **Keyboard Shortcut**: ⌘+Enter to manually run code
- **Persistent Storage**: All plots saved in `plots/` directory for future use

### Code Requirements

The `code` field must:
- Return a `Plot.plot()` result using `return`
- Have access to `Plot` and `d3` globals
- Be valid JavaScript (async/await supported)

**Example:**
```javascript
// Fetch and visualize data
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/penguins.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

return Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "flipper_length_mm",
      y: "body_mass_g",
      fill: "species",
      tip: true
    })
  ],
  color: { legend: true }
})
```

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
