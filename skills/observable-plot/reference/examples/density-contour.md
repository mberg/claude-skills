# Density and Contour Examples

Density estimation and contour plots visualize the distribution of data points in 2D space. Use `Plot.density()` for smooth density visualization and `Plot.contour()` for contour lines.

## Basic Density Plot

Create a 2D density heatmap:

```javascript
import * as Plot from "@observablehq/plot";

// Generate clustered data
const data = Array.from({length: 1000}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  color: {
    scheme: "YlOrRd",
    legend: true,
    label: "Density"
  },
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 10
    })
  ]
}).display();
```

## Contour Lines

Show density contours:

```javascript
const data = Array.from({length: 2000}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  marks: [
    Plot.contour(data, {
      x: "x",
      y: "y",
      stroke: "black",
      strokeWidth: 1,
      bandwidth: 10,
      thresholds: 10  // Number of contour levels
    })
  ]
}).display();
```

## Filled Contours

Combine filled areas with contour lines:

```javascript
const data = Array.from({length: 2000}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  color: {
    scheme: "viridis",
    legend: true
  },
  marks: [
    // Filled contours
    Plot.contour(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 10,
      thresholds: 20
    }),

    // Contour lines
    Plot.contour(data, {
      x: "x",
      y: "y",
      stroke: "white",
      strokeWidth: 0.5,
      bandwidth: 10,
      thresholds: 10
    })
  ]
}).display();
```

## Multiple Clusters

Visualize distinct clusters:

```javascript
// Generate three clusters
const cluster1 = Array.from({length: 400}, () => ({
  x: 30 + Math.random() * 15,
  y: 30 + Math.random() * 15
}));

const cluster2 = Array.from({length: 400}, () => ({
  x: 70 + Math.random() * 15,
  y: 70 + Math.random() * 15
}));

const cluster3 = Array.from({length: 400}, () => ({
  x: 50 + Math.random() * 10,
  y: 80 + Math.random() * 10
}));

const data = [...cluster1, ...cluster2, ...cluster3];

Plot.plot({
  color: {
    scheme: "turbo",
    legend: true
  },
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 8
    })
  ]
}).display();
```

## Density with Raw Points

Overlay density with original data:

```javascript
const data = Array.from({length: 500}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  color: {
    scheme: "Blues",
    legend: true
  },
  marks: [
    // Density background
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 10
    }),

    // Raw points
    Plot.dot(data, {
      x: "x",
      y: "y",
      r: 2,
      fill: "black",
      fillOpacity: 0.3
    })
  ]
}).display();
```

## Custom Bandwidth

Control smoothing with bandwidth parameter:

```javascript
const data = Array.from({length: 1000}, () => ({
  x: 50 + Math.random() * 40,
  y: 50 + Math.random() * 40
}));

// Narrow bandwidth (less smoothing)
Plot.plot({
  title: "Bandwidth: 5",
  color: {scheme: "YlOrRd"},
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 5
    })
  ]
}).display();

// Wide bandwidth (more smoothing)
Plot.plot({
  title: "Bandwidth: 20",
  color: {scheme: "YlOrRd"},
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 20
    })
  ]
}).display();
```

## Bivariate Normal Distribution

Visualize theoretical distributions:

```javascript
// Generate normally distributed data
const data = Array.from({length: 2000}, () => {
  const u1 = Math.random();
  const u2 = Math.random();
  const z0 = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  const z1 = Math.sqrt(-2 * Math.log(u1)) * Math.sin(2 * Math.PI * u2);

  return {
    x: 50 + z0 * 10,
    y: 50 + z1 * 10
  };
});

Plot.plot({
  color: {
    scheme: "Spectral",
    reverse: true,
    legend: true
  },
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 8
    }),
    Plot.contour(data, {
      x: "x",
      y: "y",
      stroke: "white",
      strokeWidth: 1,
      bandwidth: 8,
      thresholds: 5
    })
  ]
}).display();
```

## Contour Labels

Add labels to contour lines:

```javascript
const data = Array.from({length: 1500}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

Plot.plot({
  marks: [
    // Filled contours
    Plot.contour(data, {
      x: "x",
      y: "y",
      fill: "density",
      stroke: "black",
      strokeWidth: 0.5,
      bandwidth: 10,
      thresholds: 8
    })
  ],
  color: {
    scheme: "RdYlGn",
    reverse: true,
    legend: true
  }
}).display();
```

## Density Comparison (Faceted)

Compare densities across categories:

```javascript
const dataA = Array.from({length: 500}, () => ({
  group: "A",
  x: 40 + Math.random() * 20,
  y: 40 + Math.random() * 20
}));

const dataB = Array.from({length: 500}, () => ({
  group: "B",
  x: 60 + Math.random() * 20,
  y: 60 + Math.random() * 20
}));

const data = [...dataA, ...dataB];

Plot.plot({
  fx: {label: "Group"},
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.density(data, {
      fx: "group",
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 8
    })
  ]
}).display();
```

## Marginal Density

Combine 2D density with 1D marginals:

```javascript
const data = Array.from({length: 1000}, () => ({
  x: 50 + Math.random() * 30,
  y: 50 + Math.random() * 30
}));

// Main 2D density
Plot.plot({
  width: 640,
  height: 640,
  color: {scheme: "viridis"},
  marks: [
    Plot.density(data, {
      x: "x",
      y: "y",
      fill: "density",
      bandwidth: 10
    })
  ]
}).display();

// Marginal X density
Plot.plot({
  width: 640,
  height: 100,
  marks: [
    Plot.areaY(data, Plot.binX(
      {y: "count"},
      {
        x: "x",
        fill: "steelblue",
        thresholds: 30
      }
    ))
  ]
}).display();

// Marginal Y density
Plot.plot({
  width: 100,
  height: 640,
  marks: [
    Plot.areaX(data, Plot.binY(
      {x: "count"},
      {
        y: "y",
        fill: "steelblue",
        thresholds: 30
      }
    ))
  ]
}).display();
```

## Function-Based Contours

Contours from mathematical functions:

```javascript
// Generate grid of points
const points = [];
for (let x = 0; x <= 100; x += 1) {
  for (let y = 0; y <= 100; y += 1) {
    const value = Math.sin(x / 10) * Math.cos(y / 10);
    points.push({x, y, value});
  }
}

Plot.plot({
  color: {
    scheme: "RdBu",
    symmetric: true,
    legend: true
  },
  marks: [
    Plot.contour(points, {
      x: "x",
      y: "y",
      value: "value",
      fill: "value",
      stroke: "black",
      strokeWidth: 0.5,
      thresholds: 20
    })
  ]
}).display();
```

## Key Patterns

### Basic Density
```javascript
Plot.density(data, {
  x: "x",
  y: "y",
  fill: "density",     // Color by density
  bandwidth: 10        // Smoothing parameter
})
```

### Contour Lines
```javascript
Plot.contour(data, {
  x: "x",
  y: "y",
  stroke: "black",
  thresholds: 10       // Number of levels
})
```

### Filled Contours
```javascript
Plot.contour(data, {
  x: "x",
  y: "y",
  fill: "density",
  thresholds: 20
})
```

### Bandwidth Selection
- **Small bandwidth** (5-10): Less smoothing, shows more detail, may show noise
- **Medium bandwidth** (10-20): Balanced smoothing
- **Large bandwidth** (20-40): High smoothing, shows broad patterns only

### Threshold Selection
- **Few thresholds** (5-10): Clear distinct levels
- **Many thresholds** (20-50): Smooth gradations

### Color Schemes
- **Sequential**: `"YlOrRd"`, `"viridis"`, `"plasma"` (one direction)
- **Diverging**: `"RdBu"`, `"RdYlGn"` (two directions, use with `symmetric: true`)
- **Cyclical**: `"rainbow"`, `"sinebow"` (periodic data)

### When to Use
- **Density**: Show smooth distribution of points, good for large datasets
- **Contours**: Emphasize specific density levels, easier to read values
- **Hexbin**: Alternative for discrete binning instead of smooth density
- **Points**: Show actual data when dataset is small (<1000 points)

## Related Examples
- [hexbin-heatmap.md](hexbin-heatmap.md) - Discrete binning alternative
- [scatterplot.md](scatterplot.md) - Raw point visualization

## Reference
- [reference/marks.md](../marks.md) - Density and contour mark options
- [reference/scales.md](../scales.md) - Color schemes for density plots
