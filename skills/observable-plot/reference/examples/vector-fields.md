# Vector Field Examples

Vector fields visualize magnitude and direction at points in space. Observable Plot provides the `Plot.vector()` mark for directional data and `Plot.arrow()` for flow visualization.

## Basic Vector Field

Simple directional vectors:

```javascript
import * as Plot from "@observablehq/plot";

// Generate grid of vectors
const vectors = [];
for (let x = 0; x <= 100; x += 10) {
  for (let y = 0; y <= 100; y += 10) {
    const angle = Math.atan2(y - 50, x - 50);
    const magnitude = Math.sqrt((x - 50) ** 2 + (y - 50) ** 2) / 10;
    vectors.push({x, y, angle, magnitude});
  }
}

Plot.plot({
  marks: [
    Plot.vector(vectors, {
      x: "x",
      y: "y",
      length: "magnitude",
      rotate: d => (d.angle * 180) / Math.PI,
      stroke: "steelblue",
      strokeWidth: 2
    })
  ]
}).display();
```

## Wind Map

Visualize wind direction and speed:

```javascript
// Sample wind data (direction in degrees, speed in mph)
const windData = [
  {lon: -122, lat: 37, direction: 45, speed: 15},
  {lon: -121, lat: 37, direction: 90, speed: 20},
  {lon: -120, lat: 37, direction: 135, speed: 10},
  {lon: -122, lat: 38, direction: 180, speed: 25},
  {lon: -121, lat: 38, direction: 225, speed: 12},
  {lon: -120, lat: 38, direction: 270, speed: 18}
];

Plot.plot({
  projection: {
    type: "mercator",
    domain: {
      type: "MultiPoint",
      coordinates: windData.map(d => [d.lon, d.lat])
    }
  },
  marks: [
    // Background map (if available)
    // Plot.geo(states, {fill: "lightgray"}),

    // Wind vectors
    Plot.vector(windData, {
      x: "lon",
      y: "lat",
      length: d => d.speed / 2,  // Scale for visibility
      rotate: "direction",
      stroke: d => d.speed,
      strokeWidth: 2,
      tip: true,
      channels: {
        Speed: d => `${d.speed} mph`,
        Direction: d => `${d.direction}°`
      }
    })
  ],
  color: {
    scheme: "YlOrRd",
    legend: true,
    label: "Wind Speed (mph)"
  }
}).display();
```

## Gradient Field

Visualize gradients or slopes:

```javascript
// Compute gradient of a function
const gradientField = [];
for (let x = 0; x <= 100; x += 5) {
  for (let y = 0; y <= 100; y += 5) {
    // Example: gradient of z = x^2 + y^2
    const dx = 2 * (x - 50);
    const dy = 2 * (y - 50);
    const magnitude = Math.sqrt(dx ** 2 + dy ** 2);
    const angle = Math.atan2(dy, dx);

    gradientField.push({
      x,
      y,
      angle: (angle * 180) / Math.PI,
      magnitude: magnitude / 10
    });
  }
}

Plot.plot({
  color: {scheme: "viridis", legend: true},
  marks: [
    Plot.vector(gradientField, {
      x: "x",
      y: "y",
      length: "magnitude",
      rotate: "angle",
      stroke: "magnitude",
      anchor: "start"  // Arrow starts at (x,y)
    })
  ]
}).display();
```

## Flow Field

Animated-style flow visualization:

```javascript
// Generate circular flow
const flowData = [];
for (let x = 10; x <= 90; x += 8) {
  for (let y = 10; y <= 90; y += 8) {
    const dx = -(y - 50);  // Rotational flow
    const dy = x - 50;
    const magnitude = Math.sqrt(dx ** 2 + dy ** 2);
    const angle = Math.atan2(dy, dx);

    flowData.push({
      x,
      y,
      angle: (angle * 180) / Math.PI,
      magnitude: Math.min(magnitude / 5, 10)
    });
  }
}

Plot.plot({
  marks: [
    Plot.vector(flowData, {
      x: "x",
      y: "y",
      length: "magnitude",
      rotate: "angle",
      stroke: "steelblue",
      strokeWidth: 1.5,
      strokeOpacity: 0.6
    })
  ]
}).display();
```

## Velocity Field with Magnitude

Color-code vectors by magnitude:

```javascript
const velocityField = [];
for (let x = 0; x <= 100; x += 10) {
  for (let y = 0; y <= 100; y += 10) {
    // Example velocity field
    const vx = Math.sin(x / 10) * Math.cos(y / 10);
    const vy = Math.cos(x / 10) * Math.sin(y / 10);
    const magnitude = Math.sqrt(vx ** 2 + vy ** 2);
    const angle = Math.atan2(vy, vx);

    velocityField.push({
      x,
      y,
      angle: (angle * 180) / Math.PI,
      magnitude: magnitude * 10
    });
  }
}

Plot.plot({
  color: {
    scheme: "turbo",
    legend: true,
    label: "Magnitude"
  },
  marks: [
    Plot.vector(velocityField, {
      x: "x",
      y: "y",
      length: d => Math.min(d.magnitude, 15),
      rotate: "angle",
      stroke: "magnitude",
      strokeWidth: 2
    })
  ]
}).display();
```

## Arrow-Based Flow

Use arrows instead of vectors for clearer direction:

```javascript
const flowPoints = [];
for (let x = 20; x <= 80; x += 20) {
  for (let y = 20; y <= 80; y += 20) {
    const dx = Math.sin(y / 10);
    const dy = Math.cos(x / 10);
    const magnitude = Math.sqrt(dx ** 2 + dy ** 2) * 15;

    flowPoints.push({
      x1: x,
      y1: y,
      x2: x + dx * magnitude,
      y2: y + dy * magnitude
    });
  }
}

Plot.plot({
  marks: [
    Plot.arrow(flowPoints, {
      x1: "x1",
      y1: "y1",
      x2: "x2",
      y2: "y2",
      stroke: "steelblue",
      strokeWidth: 2,
      headLength: 8,
      headAngle: 45
    })
  ]
}).display();
```

## Spike Map (Geographic)

Show directional data on a map:

```javascript
const earthquakeData = [
  {lon: -122.5, lat: 37.8, magnitude: 4.5, direction: 45},
  {lon: -121.5, lat: 37.5, magnitude: 3.2, direction: 90},
  {lon: -120.5, lat: 38.0, magnitude: 5.1, direction: 180},
  {lon: -122.0, lat: 38.5, magnitude: 3.8, direction: 270}
];

Plot.plot({
  projection: "mercator",
  marks: [
    // Base map (if available)
    // Plot.geo(region, {fill: "lightgray"}),

    // Spike vectors
    Plot.vector(earthquakeData, {
      x: "lon",
      y: "lat",
      length: d => d.magnitude * 2,
      rotate: "direction",
      stroke: "red",
      strokeWidth: 3,
      tip: true,
      channels: {
        Magnitude: "magnitude",
        Direction: d => `${d.direction}°`
      }
    })
  ]
}).display();
```

## Barb Plot (Meteorological)

Weather barbs showing wind direction:

```javascript
const weatherStations = [
  {x: 20, y: 20, windSpeed: 25, windDir: 45},
  {x: 50, y: 30, windSpeed: 15, windDir: 135},
  {x: 80, y: 25, windSpeed: 30, windDir: 225},
  {x: 35, y: 60, windSpeed: 20, windDir: 315},
  {x: 65, y: 70, windSpeed: 10, windDir: 90}
];

Plot.plot({
  marks: [
    // Wind direction vectors
    Plot.vector(weatherStations, {
      x: "x",
      y: "y",
      length: d => d.windSpeed / 3,
      rotate: "windDir",
      stroke: "steelblue",
      strokeWidth: 2
    }),

    // Station markers
    Plot.dot(weatherStations, {
      x: "x",
      y: "y",
      r: 5,
      fill: "white",
      stroke: "steelblue",
      strokeWidth: 2,
      tip: true,
      channels: {
        "Wind Speed": d => `${d.windSpeed} mph`,
        "Wind Direction": d => `${d.windDir}°`
      }
    })
  ]
}).display();
```

## Streamlines (Simulated)

Continuous flow lines through field:

```javascript
// Generate streamline points (simplified)
const streamlines = [];

for (let startY = 10; startY < 100; startY += 15) {
  const line = [];
  let x = 5, y = startY;

  for (let i = 0; i < 50; i++) {
    // Simple flow field
    const vx = 2;
    const vy = Math.sin(x / 10) * 3;

    line.push({x, y, line: startY});
    x += vx;
    y += vy;

    if (x > 100 || y < 0 || y > 100) break;
  }

  streamlines.push(...line);
}

Plot.plot({
  marks: [
    Plot.line(streamlines, {
      x: "x",
      y: "y",
      z: "line",
      stroke: "steelblue",
      strokeWidth: 1,
      strokeOpacity: 0.6
    })
  ]
}).display();
```

## Quiver Plot

Scientific vector visualization:

```javascript
// Electric field around charges
const field = [];
const charges = [
  {x: 30, y: 50, charge: 1},
  {x: 70, y: 50, charge: -1}
];

for (let x = 10; x <= 90; x += 8) {
  for (let y = 10; y <= 90; y += 8) {
    let Ex = 0, Ey = 0;

    // Calculate field from each charge
    charges.forEach(charge => {
      const dx = x - charge.x;
      const dy = y - charge.y;
      const r2 = dx ** 2 + dy ** 2;
      const r = Math.sqrt(r2);

      if (r > 3) {  // Avoid singularity
        Ex += charge.charge * dx / (r2 * r);
        Ey += charge.charge * dy / (r2 * r);
      }
    });

    const magnitude = Math.sqrt(Ex ** 2 + Ey ** 2);
    const angle = Math.atan2(Ey, Ex);

    field.push({
      x,
      y,
      angle: (angle * 180) / Math.PI,
      magnitude: Math.min(magnitude * 20, 10)
    });
  }
}

Plot.plot({
  color: {scheme: "RdBu", legend: true},
  marks: [
    // Field vectors
    Plot.vector(field, {
      x: "x",
      y: "y",
      length: "magnitude",
      rotate: "angle",
      stroke: "magnitude",
      strokeWidth: 1.5
    }),

    // Charge markers
    Plot.dot(charges, {
      x: "x",
      y: "y",
      r: 8,
      fill: d => d.charge > 0 ? "red" : "blue",
      stroke: "white",
      strokeWidth: 2
    })
  ]
}).display();
```

## Key Patterns

### Vector Mark
```javascript
Plot.vector(data, {
  x: "x",
  y: "y",
  length: "magnitude",    // Vector length
  rotate: "angle",        // Direction in degrees
  stroke: "color",
  anchor: "middle"        // "start", "middle", "end"
})
```

### Arrow Mark for Flow
```javascript
Plot.arrow(data, {
  x1: "startX",
  y1: "startY",
  x2: "endX",
  y2: "endY",
  stroke: "color",
  headLength: 8,          // Arrow head size
  strokeWidth: 2
})
```

### Angle Conventions
- Degrees: Use directly in `rotate` channel
- Radians: Convert with `rotate: d => (d.angleRad * 180) / Math.PI`
- Meteorological (from direction): Use directly
- Mathematical (counterclockwise from east): Standard

### Length Scaling
```javascript
// Constant length
{length: 10}

// Data-driven
{length: "magnitude"}

// Scaled for visibility
{length: d => Math.sqrt(d.magnitude) * scale}

// Clamped
{length: d => Math.min(d.magnitude * scale, maxLength)}
```

### Color Encoding
```javascript
// By magnitude
{
  stroke: "magnitude",
  color: {scheme: "viridis", legend: true}
}

// By direction
{
  stroke: d => (d.angle + 360) % 360,
  color: {type: "cyclical", scheme: "rainbow"}
}
```

### Anchor Points
- `"start"`: Vector starts at (x, y)
- `"middle"`: Vector centered at (x, y) [default]
- `"end"`: Vector ends at (x, y)

## Common Use Cases

### Weather Visualization
- Wind speed/direction
- Ocean currents
- Atmospheric pressure gradients

### Physics Simulations
- Electric/magnetic fields
- Fluid dynamics
- Force fields

### Geographic Data
- Migration patterns
- Trade flows
- Movement tracking

## Performance Tips

For large vector fields (>1000 vectors):
1. Reduce grid resolution
2. Use opacity to handle overlap
3. Consider density-based filtering
4. Use smaller arrow heads/widths

## Related Examples
- [network-diagrams.md](network-diagrams.md) - Arrow marks for connections
- [choropleth-map.md](choropleth-map.md) - Geographic base layers

## Reference
- [reference/marks.md](../marks.md) - Vector and arrow mark options
- [reference/geographic.md](../geographic.md) - Geographic projections for wind maps and vector fields on maps
