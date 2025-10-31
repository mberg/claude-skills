# Geographic Projection Reference

Projections transform spherical coordinates (longitude, latitude) to planar coordinates (x, y) for mapping. Use projections with `Plot.geo()` marks.

## Usage

Specify projection at the plot level:

```javascript
Plot.plot({
  projection: "albers-usa",  // or projection config object
  marks: [
    Plot.geo(geojson, {fill: "value"})
  ]
})
```

## Projection Types

### Conic Projections

**albers** - Albers equal-area conic
- Equal-area (preserves relative sizes)
- Good for mid-latitude regions
- Standard parallels: 29.5°N, 45.5°N

```javascript
{projection: "albers"}
{projection: {type: "albers", parallels: [30, 40]}}
```

**albers-usa** - Composite Albers for US
- Includes Alaska and Hawaii insets
- Optimized for United States
- Most common for US choropleth maps

```javascript
{projection: "albers-usa"}
```

**conic-conformal** - Lambert conformal conic
- Conformal (preserves angles/shapes)
- Good for mid-latitude regions

```javascript
{projection: "conic-conformal"}
{projection: {type: "conic-conformal", parallels: [33, 45]}}
```

**conic-equal-area** - Albers conic equal-area
```javascript
{projection: "conic-equal-area"}
```

**conic-equidistant** - Conic equidistant
- Preserves distances along meridians
```javascript
{projection: "conic-equidistant"}
```

### Cylindrical Projections

**mercator** - Mercator
- Conformal (preserves shapes locally)
- Used by web maps (Google Maps, etc.)
- Distorts sizes near poles

```javascript
{projection: "mercator"}
```

**transverse-mercator** - Transverse Mercator
- Rotated Mercator
- Good for north-south regions

```javascript
{projection: "transverse-mercator"}
```

**equirectangular** - Plate carrée
- Simplest projection (linear lat/lon)
- Neither conformal nor equal-area

```javascript
{projection: "equirectangular"}
```

### Azimuthal Projections

**azimuthal-equal-area** - Lambert azimuthal equal-area
- Equal-area
- Good for polar regions

```javascript
{projection: "azimuthal-equal-area"}
```

**azimuthal-equidistant** - Azimuthal equidistant
- Preserves distances from center point

```javascript
{projection: "azimuthal-equidistant"}
```

**stereographic** - Stereographic
- Conformal azimuthal
- Good for polar regions

```javascript
{projection: "stereographic"}
```

**orthographic** - Orthographic (globe view)
- Perspective projection (as if viewing from space)
- Shows one hemisphere

```javascript
{projection: "orthographic"}
{projection: {type: "orthographic", rotate: [100, -30]}}
```

**gnomonic** - Gnomonic
- All great circles are straight lines

```javascript
{projection: "gnomonic"}
```

### Compromise Projections

**equal-earth** - Equal Earth
- Equal-area
- Visually pleasing for world maps
- Similar to Robinson

```javascript
{projection: "equal-earth"}
```

**natural-earth** - Natural Earth
- Compromise (neither conformal nor equal-area)
- Visually pleasing

```javascript
{projection: "natural-earth"}
```

**robinson** - Robinson
- Compromise projection
- Common for world maps

```javascript
{projection: "robinson"}
```

## Projection Configuration

### Basic Options

**type** - Projection name
```javascript
{projection: {type: "mercator"}}
```

**domain** - Auto-fit to GeoJSON bounds
```javascript
{projection: {type: "mercator", domain: geojson}}
```

**rotate** - Rotation [λ, φ, γ] in degrees
```javascript
{projection: {
  type: "orthographic",
  rotate: [-100, -30, 0]  // [longitude, latitude, roll]
}}
```

**parallels** - Standard parallels (conic projections)
```javascript
{projection: {
  type: "albers",
  parallels: [30, 40]
}}
```

**precision** - Adaptive resampling precision
```javascript
{projection: {precision: 0.5}}
```

### Clipping

**clip** - Clip to sphere or rectangle
```javascript
{projection: {clip: true}}       // Clip to sphere
{projection: {clip: "sphere"}}   // Clip to sphere
{projection: {clip: "frame"}}    // Clip to frame
```

### Inset Options (albers-usa)

The `albers-usa` projection automatically positions Alaska and Hawaii as insets.

```javascript
{projection: "albers-usa"}  // Default configuration
```

## Common Use Cases

### US Choropleth Map
```javascript
Plot.plot({
  projection: "albers-usa",
  color: {scheme: "blues", legend: true},
  marks: [
    Plot.geo(states, {fill: "value", stroke: "white"})
  ]
})
```

### World Map
```javascript
Plot.plot({
  projection: "equal-earth",
  marks: [
    Plot.sphere({fill: "#e0f3ff"}),  // Ocean
    Plot.geo(countries, {fill: "lightgray", stroke: "white"})
  ]
})
```

### Globe View
```javascript
Plot.plot({
  projection: {
    type: "orthographic",
    rotate: [-100, -30]
  },
  marks: [
    Plot.sphere({fill: "#e0f3ff"}),
    Plot.graticule({stroke: "lightgray"}),
    Plot.geo(countries, {fill: "lightgray", stroke: "white"})
  ]
})
```

### Regional Map
```javascript
Plot.plot({
  projection: {
    type: "mercator",
    domain: regionGeoJSON  // Auto-fit to region bounds
  },
  marks: [
    Plot.geo(regionGeoJSON, {fill: "value"})
  ]
})
```

### Polar Region
```javascript
Plot.plot({
  projection: {
    type: "azimuthal-equal-area",
    rotate: [0, -90]  // Center on South Pole
  },
  marks: [
    Plot.geo(antarctica, {fill: "white", stroke: "gray"})
  ]
})
```

## Projection Properties

### Preserves Shapes (Conformal)
- `mercator`
- `stereographic`
- `conic-conformal`

### Preserves Areas (Equal-area)
- `albers`
- `albers-usa`
- `azimuthal-equal-area`
- `conic-equal-area`
- `equal-earth`

### Preserves Distances
- `azimuthal-equidistant`
- `equirectangular` (along meridians)

### Compromise (Visual Appeal)
- `natural-earth`
- `robinson`

## Auto-fitting

Use `domain` to automatically fit projection to data bounds:

```javascript
Plot.plot({
  projection: {
    type: "mercator",
    domain: geojson  // Fit to GeoJSON extent
  },
  marks: [Plot.geo(geojson)]
})
```

## Combining with Other Marks

Layer geographic and non-geographic marks:

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    // Geographic background
    Plot.geo(states, {fill: "lightgray"}),

    // Point data with lon/lat
    Plot.dot(cities, {
      x: "longitude",
      y: "latitude",
      r: "population",
      fill: "red"
    }),

    // Text labels
    Plot.text(cities, {
      x: "longitude",
      y: "latitude",
      text: "name",
      dy: -12
    })
  ]
})
```

## Related Documentation
- [examples/choropleth-map.md](examples/choropleth-map.md) - Geographic visualization examples
- [marks.md](marks.md) - Geo mark documentation
