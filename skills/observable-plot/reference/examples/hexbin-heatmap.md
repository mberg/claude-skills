# Hexbin Heatmap Examples

Hexbin heatmaps visualize the density of points in a 2D space using hexagonal binning. This is ideal for large datasets where individual points would create overplotting.

## Basic Hexbin

Use `Plot.dot()` with the `hexbin` transform:

```javascript
import * as Plot from "@observablehq/plot";

// Generate sample data with many points
const data = Array.from({length: 1000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100
}));

Plot.plot({
  marks: [
    Plot.dot(data, Plot.hexbin(
      {r: "count"},  // Radius encodes count
      {
        x: "x",
        y: "y",
        fill: "steelblue"
      }
    ))
  ]
}).display();
```

## Color-Encoded Density

Use color instead of size to show density:

```javascript
const data = Array.from({length: 2000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100
}));

Plot.plot({
  color: {
    scheme: "YlOrRd",  // Sequential color scheme
    legend: true,
    label: "Count"
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},  // Color encodes count
      {
        x: "x",
        y: "y",
        r: 8,  // Fixed radius
        stroke: "white",
        strokeWidth: 0.5
      }
    ))
  ]
}).display();
```

## Clustered Data

Visualize clusters in the data:

```javascript
// Generate clustered data
const cluster1 = Array.from({length: 500}, () => ({
  x: 30 + Math.random() * 20,
  y: 30 + Math.random() * 20
}));

const cluster2 = Array.from({length: 500}, () => ({
  x: 70 + Math.random() * 20,
  y: 70 + Math.random() * 20
}));

const data = [...cluster1, ...cluster2];

Plot.plot({
  color: {
    scheme: "turbo",
    legend: true
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "x",
        y: "y",
        r: 10,
        stroke: "white"
      }
    ))
  ]
}).display();
```

## Custom Bin Size

Control hexagon size with the `binWidth` option:

```javascript
const data = Array.from({length: 1500}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100
}));

Plot.plot({
  color: {
    scheme: "viridis",
    legend: true
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "x",
        y: "y",
        binWidth: 5,  // Smaller bins = more detail
        r: 5
      }
    ))
  ]
}).display();
```

## Aggregating Values

Aggregate a third variable within each hexbin:

```javascript
const data = Array.from({length: 1000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100,
  value: Math.random() * 50
}));

Plot.plot({
  color: {
    scheme: "RdYlBu",
    legend: true,
    label: "Mean Value"
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "mean"},  // Average of 'value' in each bin
      {
        x: "x",
        y: "y",
        z: "value",  // Variable to aggregate
        r: 8,
        stroke: "white"
      }
    ))
  ]
}).display();
```

## Hexbin with Multiple Aggregations

Show both count (size) and mean (color):

```javascript
const data = Array.from({length: 1000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100,
  temperature: 15 + Math.random() * 20
}));

Plot.plot({
  color: {
    scheme: "RdBu",
    reverse: true,
    legend: true,
    label: "Mean Temperature"
  },
  r: {
    range: [2, 20],
    label: "Count"
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {
        fill: "mean",   // Color by mean temperature
        r: "count"      // Size by count
      },
      {
        x: "x",
        y: "y",
        z: "temperature",
        stroke: "black",
        strokeWidth: 0.5,
        fillOpacity: 0.8,
        tip: true
      }
    ))
  ]
}).display();
```

## Using Plot.hexgrid Mark

Use `Plot.hexgrid()` for a pure heatmap style:

```javascript
const data = Array.from({length: 2000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100
}));

Plot.plot({
  color: {
    scheme: "plasma",
    legend: true,
    label: "Density"
  },
  marks: [
    Plot.hexgrid(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "x",
        y: "y",
        binWidth: 8
      }
    ))
  ]
}).display();
```

## Logarithmic Color Scale

Use log scale for highly skewed density distributions:

```javascript
// Generate power-law distributed data
const data = Array.from({length: 5000}, () => {
  const r = Math.pow(Math.random(), 2) * 50;
  const theta = Math.random() * 2 * Math.PI;
  return {
    x: 50 + r * Math.cos(theta),
    y: 50 + r * Math.sin(theta)
  };
});

Plot.plot({
  color: {
    type: "log",  // Logarithmic color scale
    scheme: "YlGnBu",
    legend: true
  },
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "x",
        y: "y",
        r: 6,
        stroke: "white",
        strokeWidth: 0.5
      }
    ))
  ]
}).display();
```

## Comparison: Before and After Hexbin

Show the difference between raw points and hexbin:

```javascript
const data = Array.from({length: 3000}, () => ({
  x: Math.random() * 100,
  y: Math.random() * 100
}));

// Raw scatterplot (overplotted)
Plot.plot({
  title: "Raw Scatterplot",
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      r: 2,
      fill: "steelblue",
      fillOpacity: 0.3
    })
  ]
}).display();

// Hexbin heatmap (clear density)
Plot.plot({
  title: "Hexbin Heatmap",
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "x",
        y: "y",
        r: 8
      }
    ))
  ]
}).display();
```

## Geographic Hexbin

Combine hexbin with geographic data:

```javascript
// Sample lat/lon data
const data = Array.from({length: 1000}, () => ({
  longitude: -122 + Math.random() * 2,
  latitude: 37 + Math.random() * 2,
  value: Math.random() * 100
}));

Plot.plot({
  projection: {
    type: "mercator",
    domain: {type: "MultiPoint", coordinates: data.map(d => [d.longitude, d.latitude])}
  },
  color: {
    scheme: "YlOrRd",
    legend: true
  },
  marks: [
    Plot.geo({type: "Sphere"}),  // Background
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {
        x: "longitude",
        y: "latitude",
        binWidth: 20,
        r: 8
      }
    ))
  ]
}).display();
```

## Key Patterns

### Basic Hexbin Transform
```javascript
Plot.dot(data, Plot.hexbin(
  {fill: "count"},  // or {r: "count"}
  {
    x: "xColumn",
    y: "yColumn"
  }
))
```

### Aggregation Options
- `"count"`: Number of points in bin
- `"sum"`: Sum of values
- `"mean"`: Average of values
- `"median"`: Median of values
- `"min"` / `"max"`: Minimum/maximum values

### Bin Size Control
```javascript
{
  binWidth: 10,  // Controls hexagon size (larger = fewer, bigger bins)
  r: 5          // Visual radius (for dot mark)
}
```

### Color Schemes for Density
- Sequential: `"YlOrRd"`, `"YlGnBu"`, `"viridis"`, `"plasma"`, `"turbo"`
- Use `type: "log"` for skewed distributions
- Set `legend: true` to show scale

### When to Use Hexbin
- Dataset has >1000 points and overplotting occurs
- Need to show density patterns
- Points are roughly uniformly distributed spatially
- Want to aggregate values spatially

### Hexbin vs Other Approaches
- **Hexbin**: Best for moderate datasets (1k-100k points), shows exact bin boundaries
- **Density contours**: Better for smooth density visualization
- **2D histogram (cell)**: Simpler but less visually appealing (rectangular bins)
- **Scatterplot with opacity**: Works for smaller datasets (<1000 points)

## Related Examples
- [scatterplot.md](scatterplot.md) - Raw point visualization
- [density-contour.md](density-contour.md) - Smooth density estimation
- [choropleth-map.md](choropleth-map.md) - Geographic hexbin heatmaps on maps

## Reference
- [reference/marks.md](../marks.md) - Dot and hexgrid mark options
- [reference/transforms.md](../transforms.md) - Hexbin transform details
- [reference/scales.md](../scales.md) - Color schemes for heatmaps
- [reference/geographic.md](../geographic.md) - Geographic visualization with projections and hexbin on maps
