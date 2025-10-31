# Mark Reference

Marks are visual elements that represent data. Observable Plot provides 30+ mark types organized by category.

## Point and Symbol Marks

### Plot.dot(data, options)

Draws circles at specified positions.

**Common channels**:
- `x`, `y`: Position (required)
- `r`: Radius (size)
- `fill`, `stroke`: Color
- `fillOpacity`, `strokeOpacity`: Transparency
- `symbol`: Shape (circle, square, diamond, triangle, star, etc.)

**Example**:
```javascript
Plot.dot(data, {x: "age", y: "height", r: 5, fill: "steelblue"})
```

### Plot.image(data, options)

Displays images at specified positions.

**Channels**: `x`, `y`, `src` (image URL), `width`, `height`

**Example**:
```javascript
Plot.image(data, {x: "lon", y: "lat", src: "imageUrl", width: 20})
```

### Plot.text(data, options)

Renders text labels.

**Channels**: `x`, `y`, `text`, `fontSize`, `fontWeight`, `fontFamily`, `rotate`, `textAnchor`

**Example**:
```javascript
Plot.text(data, {x: "x", y: "y", text: "label", fontSize: 12})
```

## Rectangular Marks

### Plot.barY(data, options) / Plot.barX(data, options)

Vertical or horizontal bars.

**Channels**:
- `barY`: `x` (category), `y` (value), `y1`, `y2` (range)
- `barX`: `y` (category), `x` (value), `x1`, `x2` (range)
- `fill`, `stroke`: Color
- `inset`, `insetTop`, `insetBottom`: Spacing

**Example**:
```javascript
Plot.barY(data, {x: "category", y: "value", fill: "steelblue"})
```

### Plot.cell(data, options)

Draws rectangular cells (heatmap tiles).

**Channels**: `x`, `y`, `fill`, `stroke`, `inset`

**Example**:
```javascript
Plot.cell(data, {x: "day", y: "hour", fill: "temperature"})
```

### Plot.rect(data, options)

Arbitrary rectangles with x1/x2 and y1/y2 bounds.

**Channels**: `x1`, `x2`, `y1`, `y2`, `fill`, `stroke`, `inset`

**Example**:
```javascript
Plot.rect(data, {x1: "start", x2: "end", y1: 0, y2: "value"})
```

## Line and Area Marks

### Plot.line(data, options)

Connects points with a line.

**Channels**: `x`, `y`, `z` (series), `stroke`, `strokeWidth`, `curve`, `marker`

**Curve options**: `"linear"`, `"step"`, `"step-after"`, `"step-before"`, `"basis"`, `"cardinal"`, `"catmull-rom"`, `"natural"`

**Example**:
```javascript
Plot.line(data, {x: "date", y: "value", stroke: "steelblue", curve: "basis"})
```

### Plot.lineY(data, options) / Plot.lineX(data, options)

Optimized for vertical (lineY) or horizontal (lineX) data.

**Example**:
```javascript
Plot.lineY(data, {x: "date", y: "value"})
```

### Plot.area(data, options)

Filled area under/between lines.

**Channels**: `x`, `y`, `y1`, `y2`, `fill`, `fillOpacity`, `curve`

**Example**:
```javascript
Plot.area(data, {x: "date", y: "value", fill: "steelblue", fillOpacity: 0.3})
```

### Plot.areaY(data, options) / Plot.areaX(data, options)

Optimized for vertical (areaY) or horizontal (areaX) areas.

**Example**:
```javascript
Plot.areaY(data, {x: "date", y: "value", fill: "steelblue"})
```

## Reference Marks

### Plot.ruleY(data, options) / Plot.ruleX(data, options)

Horizontal (ruleY) or vertical (ruleX) lines.

**Channels**: `y` or `x`, `stroke`, `strokeWidth`, `strokeDasharray`

**Example**:
```javascript
Plot.ruleY([0], {stroke: "black", strokeWidth: 2})
```

### Plot.tickY(data, options) / Plot.tickX(data, options)

Short tick marks along an axis.

**Channels**: `x`, `y` (position), `stroke`, `strokeWidth`

**Example**:
```javascript
Plot.tickX(data, {x: "value", stroke: "black"})
```

### Plot.gridY(options) / Plot.gridX(options)

Grid lines across the plot.

**Options**: `stroke`, `strokeOpacity`, `strokeDasharray`, `ticks`

**Example**:
```javascript
Plot.gridY({stroke: "lightgray", strokeOpacity: 0.5})
```

### Plot.frame(options)

Draws a frame around the plot area.

**Options**: `stroke`, `fill`, `strokeWidth`, `inset`

**Example**:
```javascript
Plot.frame({stroke: "black"})
```

## Geographic Marks

### Plot.geo(data, options)

Renders GeoJSON features (polygons, lines, points) on a geographic projection.

**Channels**: `fill`, `stroke`, `strokeWidth`, `fillOpacity`, `strokeOpacity`
**Special**: Requires `projection` option at plot level

**Example**:
```javascript
Plot.geo(geojson, {fill: "value", stroke: "white", tip: true})
```

**For comprehensive geographic visualization guide**, see [geographic.md](geographic.md) which covers:
- GeoJSON format and data loading
- All projection types and configuration
- Choropleth patterns and data joining
- Layering geographic marks
- Performance optimization for large datasets
- Common patterns (bubble maps, contours, heatmaps)

### Plot.sphere(options)

Renders the outline of the Earth (for globe projections).

**Example**:
```javascript
Plot.sphere({fill: "lightblue"})
```

### Plot.graticule(options)

Draws meridians and parallels.

**Options**: `stroke`, `strokeOpacity`

**Example**:
```javascript
Plot.graticule({stroke: "lightgray"})
```

## Relational Marks

### Plot.arrow(data, options)

Draws arrows between points.

**Channels**: `x1`, `y1`, `x2`, `y2`, `stroke`, `strokeWidth`, `headLength`, `headAngle`

**Example**:
```javascript
Plot.arrow(data, {x1: "startX", y1: "startY", x2: "endX", y2: "endY"})
```

### Plot.link(data, options)

Connects pairs of points with lines.

**Channels**: `x1`, `y1`, `x2`, `y2`, `stroke`, `strokeWidth`, `curve`

**Example**:
```javascript
Plot.link(data, {x1: "sourceX", y1: "sourceY", x2: "targetX", y2: "targetY"})
```

### Plot.tree(data, options)

Hierarchical tree layout.

**Channels**: Typically works with hierarchical data structures

**Example**:
```javascript
Plot.tree(hierarchy, Plot.treeLink())
```

### Plot.vector(data, options)

Draws direction vectors (arrows with fixed origin).

**Channels**: `x`, `y`, `length`, `rotate`, `stroke`

**Example**:
```javascript
Plot.vector(data, {x: "x", y: "y", length: "magnitude", rotate: "angle"})
```

## Density Marks

### Plot.density(data, options)

2D kernel density estimation.

**Channels**: `x`, `y`, `fill` (density), `stroke`
**Options**: `bandwidth`, `thresholds`

**Example**:
```javascript
Plot.density(data, {x: "x", y: "y", fill: "density", bandwidth: 10})
```

### Plot.contour(data, options)

Contour lines or filled contours from density.

**Channels**: `x`, `y`, `fill` or `stroke`
**Options**: `bandwidth`, `thresholds`, `value`

**Example**:
```javascript
Plot.contour(data, {x: "x", y: "y", stroke: "black", thresholds: 10})
```

### Plot.hexgrid(data, options)

Hexagonal grid for spatial binning.

**Channels**: `x`, `y`, `fill`, `stroke`
**Options**: `binWidth`

**Example**:
```javascript
Plot.hexgrid(data, Plot.hexbin({fill: "count"}, {x: "x", y: "y"}))
```

### Plot.raster(data, options)

Renders raster images or heatmaps from gridded data.

**Channels**: `x`, `y`, `fill`
**Options**: `width`, `height`, `interpolate`

**Example**:
```javascript
Plot.raster(grid, {fill: "value", interpolate: "nearest"})
```

## Statistical Marks

### Plot.boxY(data, options) / Plot.boxX(data, options)

Box and whisker plots.

**Channels**: `x` (category), `y` (values) for boxY
**Options**: Automatically computes quartiles, min, max

**Example**:
```javascript
Plot.boxY(data, {x: "category", y: "value"})
```

### Plot.linearRegressionY(data, options)

Linear regression line.

**Channels**: `x`, `y`, `stroke`, `strokeWidth`
**Options**: `ci` (confidence interval)

**Example**:
```javascript
Plot.linearRegressionY(data, {x: "x", y: "y", stroke: "red"})
```

## Utility Marks

### Plot.axisX(options) / Plot.axisY(options)

Custom axis configuration.

**Options**: `anchor`, `label`, `ticks`, `tickFormat`, `tickSize`

**Example**:
```javascript
Plot.axisY({anchor: "right", label: "Custom Y Axis"})
```

### Plot.tip(data, options)

Interactive tooltips.

**Channels**: `x`, `y`, and any channels to display
**Options**: `format`, `anchor`

**Example**:
```javascript
Plot.tip(data, {x: "x", y: "y", title: d => `Value: ${d.value}`})
```

### Plot.crosshair(data, options)

Crosshair interaction.

**Channels**: `x`, `y`

**Example**:
```javascript
Plot.crosshair(data, {x: "date", y: "value"})
```

## Common Mark Options

All marks support these common options:

### Position Channels
- `x`, `y`: Primary position
- `x1`, `x2`, `y1`, `y2`: Position ranges
- `fx`, `fy`: Faceting

### Style Channels
- `fill`, `stroke`: Color
- `fillOpacity`, `strokeOpacity`: Transparency (0-1)
- `strokeWidth`: Line width
- `strokeDasharray`: Dash pattern (e.g., "4,4")

### Data Options
- `filter`: Filter data before rendering
- `sort`: Sort data
- `reverse`: Reverse data order
- `transform`: Apply data transform

### Interaction
- `tip`: Enable tooltips (boolean or options)
- `title`: Tooltip content
- `href`: Make marks clickable links
- `ariaLabel`, `ariaDescription`: Accessibility

### Mark-Specific
- `r`: Radius (dot, image)
- `symbol`: Shape (dot)
- `curve`: Interpolation (line, area)
- `inset`: Spacing (bar, cell, rect)
- `marker`: Line endpoint markers ("dot", "arrow")
- `bandwidth`: Smoothing (density, contour)

## Mark Composition

Layer multiple marks for complex visualizations:

```javascript
Plot.plot({
  marks: [
    // Background
    Plot.gridY(),
    Plot.ruleY([0]),

    // Data
    Plot.areaY(data, {x: "date", y: "value", fill: "lightblue"}),
    Plot.lineY(data, {x: "date", y: "value", stroke: "blue"}),

    // Annotations
    Plot.text(labels, {x: "date", y: "value", text: "label"}),
    Plot.dot(points, {x: "date", y: "value", fill: "red"})
  ]
})
```

Order matters - later marks draw on top of earlier marks.

## Related Documentation
- [transforms.md](transforms.md) - Data transformations
- [scales.md](scales.md) - Color and scale configuration
- [plot-options.md](plot-options.md) - Plot-level options
- [common-patterns.md](common-patterns.md) - Common mark patterns
