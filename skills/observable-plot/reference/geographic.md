# Geographic Visualization Reference

Comprehensive guide to creating geographic visualizations with Observable Plot's `Plot.geo()` mark and geographic projections.

## Plot.geo() Mark

The `Plot.geo()` mark renders GeoJSON features (polygons, lines, points) on a geographic projection.

### Basic Syntax

```javascript
Plot.geo(geojson, options)
```

### Common Channels

**Position** (automatic with projection):
- Features are positioned via geographic coordinates

**Styling**:
- `fill` - Fill color (can be channel for data encoding)
- `stroke` - Border color
- `strokeWidth` - Border width
- `fillOpacity` - Fill transparency (0-1)
- `strokeOpacity` - Border transparency

**Data Encoding**:
- `fill: "columnName"` - Color by data value
- `stroke: d => d.properties.value > 50 ? "red" : "blue"` - Conditional styling

**Interaction**:
- `tip: true` - Show tooltips
- `channels: {...}` - Custom tooltip content

### Full Option Set

```javascript
Plot.geo(geojson, {
  // Styling
  fill: "#ccc",                    // Fixed color or channel
  stroke: "black",                 // Border color
  strokeWidth: 1,                  // Border width
  strokeOpacity: 1,                // Border transparency
  fillOpacity: 0.8,                // Fill transparency
  strokeDasharray: "4,4",          // Dashed border

  // Interaction
  tip: true,                       // Tooltip on hover
  tip: {
    format: {value: "$.2f"},       // Custom formats
    anchor: "top"                  // Position
  },

  // Data
  channels: {
    Name: d => d.properties.name,
    Value: "value",
    Custom: d => custom(d)
  },

  // Filtering/Sorting
  filter: d => d.properties.active,
  sort: "properties.value",

  // Rendering
  clip: true,                      // Clip to map bounds
  href: d => `/details/${d.id}`    // Make clickable
})
```

## GeoJSON Format

GeoJSON is the standard format for geographic data.

### FeatureCollection (Polygons/Regions)

```javascript
{
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {
        name: "State Name",
        value: 42,
        color: "red"
      },
      geometry: {
        type: "Polygon",
        coordinates: [[[[lng, lat], [lng, lat], ...]]]  // Rings
      }
    },
    // ... more features
  ]
}
```

### MultiPolygon (Regions with Holes)

```javascript
{
  type: "Feature",
  geometry: {
    type: "MultiPolygon",
    coordinates: [
      [[[lng, lat], ...]],  // Outer ring
      [[[lng, lat], ...]]   // Hole/island
    ]
  }
}
```

### LineString (Boundaries, Routes)

```javascript
{
  type: "Feature",
  geometry: {
    type: "LineString",
    coordinates: [[lng, lat], [lng, lat], ...]
  }
}
```

### Point (Locations)

```javascript
{
  type: "Feature",
  geometry: {
    type: "Point",
    coordinates: [lng, lat]  // Note: [longitude, latitude]
  }
}
```

### Important Notes
- **Coordinate order**: [longitude, latitude] (not latitude, longitude!)
- **Coordinate range**: Longitude [-180, 180], Latitude [-90, 90]
- **Rings**: Counterclockwise for outer rings, clockwise for holes
- **MultiPolygon**: Each polygon can have multiple rings

## Projections

Map projections transform spherical coordinates to 2D plane coordinates.

### Essential Projections

**albers-usa** - United States (includes Alaska, Hawaii insets)
```javascript
{projection: "albers-usa"}
```
Best for: US choropleths, regional US analysis

**mercator** - Web standard (like Google Maps)
```javascript
{projection: "mercator"}
```
Best for: Web maps, interactive maps, familiar to users
Caveat: Distorts sizes near poles

**equal-earth** - Equal-area world map
```javascript
{projection: "equal-earth"}
```
Best for: World maps, comparing countries/continents

**orthographic** - Globe view
```javascript
{projection: {type: "orthographic", rotate: [lng, lat]}}
```
Best for: 3D globe effect, focal point emphasis

**transverse-mercator** - For north-south regions
```javascript
{projection: "transverse-mercator"}
```
Best for: Countries, regions with N-S orientation

### Projection Configuration

```javascript
{
  projection: {
    type: "mercator",
    domain: geojson,           // Auto-fit to bounds
    rotate: [-100, 0],         // [longitude, latitude]
    scale: 1000,               // Zoom level
    translate: [width/2, height/2]  // Center position
  }
}
```

**Auto-fit Example**:
```javascript
const bounds = geojson;  // Your GeoJSON
Plot.plot({
  projection: {
    type: "mercator",
    domain: bounds
  },
  marks: [Plot.geo(geojson)]
})
```

### When to Use Each

| Projection | Best For | Preserve |
|-----------|----------|----------|
| mercator | Web maps, interactive | Angles (conformal) |
| albers-usa | US regional data | Area |
| equal-earth | World maps | Area |
| orthographic | Globe visualization | - |
| azimuthal-equal-area | Polar regions | Area |
| conic-conformal | Mid-latitude regions | Angles |

## Loading GeoJSON Data

### From URL

```javascript
const geojson = await fetch("url/to/geojson.json")
  .then(r => r.json());

Plot.plot({
  projection: "mercator",
  marks: [Plot.geo(geojson)]
})
```

### From TopoJSON (Compressed Format)

TopoJSON is more compact than GeoJSON (30-80% smaller).

```javascript
// Need to convert TopoJSON to GeoJSON first
const topology = await fetch("url/to/topology.json")
  .then(r => r.json());

// Using topojson-client library
const geojson = topojson.feature(topology, topology.objects.states);

Plot.plot({
  marks: [Plot.geo(geojson)]
})
```

### Common Data Sources

**Natural Earth** (free, good quality):
- https://www.naturalearthdata.com/
- Different resolutions: 10m, 50m, 110m

**OpenStreetMap** (free, detailed):
- Through Overpass API or other services

**Census Data** (US specific):
- US Census Bureau

**World Bank** (country boundaries):
- Various datasets available

## Layering Geographic Marks

### Complete Map Composition

```javascript
Plot.plot({
  projection: "mercator",
  marks: [
    // 1. Ocean/background
    Plot.sphere({fill: "#e0f3ff"}),

    // 2. Graticule (grid lines)
    Plot.graticule({stroke: "lightgray", strokeOpacity: 0.5}),

    // 3. Base regions (background color)
    Plot.geo(states, {fill: "#f5f5f5", stroke: "white"}),

    // 4. Data visualization (choropleth)
    Plot.geo(states, {
      fill: "value",
      stroke: "white",
      tip: true
    }),

    // 5. Point data overlay
    Plot.dot(cities, {
      x: "longitude",
      y: "latitude",
      r: d => Math.sqrt(d.population) / 100,
      fill: "red"
    }),

    // 6. Labels
    Plot.text(cities, {
      x: "longitude",
      y: "latitude",
      text: "name",
      dy: -8
    })
  ],
  color: {scheme: "Blues", legend: true}
})
```

**Layer Order**:
1. Ocean/background (if needed)
2. Graticule (grid)
3. Base regions (unfilled or light)
4. Data visualization
5. Points/symbols
6. Text/annotations

## Common Patterns

### Choropleth (Colored Regions)

```javascript
Plot.plot({
  projection: "albers-usa",
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.geo(states, {
      fill: "populationDensity",
      stroke: "white",
      tip: true
    })
  ]
})
```

### Data Join (External Data)

Map external data values to GeoJSON features:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

const dataByState = new Map([
  ["CA", 39.5],
  ["TX", 29.0],
  ["FL", 21.5]
]);

Plot.plot({
  projection: "albers-usa",
  color: {scheme: "Blues"},
  marks: [
    Plot.geo(states, {
      fill: d => dataByState.get(d.properties.abbreviation),
      tip: true
    })
  ]
})
```

### Proportional Symbols (Bubble Map)

Combine regions with overlay points:

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    // Base regions
    Plot.geo(states, {fill: "#f5f5f5", stroke: "gray"}),

    // Proportional dots
    Plot.dot(cities, {
      x: "longitude",
      y: "latitude",
      r: d => Math.sqrt(d.population) / 50,
      fill: "red",
      fillOpacity: 0.6,
      stroke: "darkred",
      tip: true
    })
  ]
})
```

### Bivariate Choropleth

Show two variables with color combinations:

```javascript
const colorMap = {
  "lowLow": "#e8f4f8",
  "lowHigh": "#b3cde3",
  "highLow": "#fdd9b5",
  "highHigh": "#fe9929"
};

const medianX = d3.median(data, d => d.variable1);
const medianY = d3.median(data, d => d.variable2);

Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {
      fill: d => {
        const x = d.variable1 > medianX ? "High" : "Low";
        const y = d.variable2 > medianY ? "High" : "Low";
        return colorMap[`${x.toLowerCase()}${y.toLowerCase()}`];
      }
    })
  ]
})
```

### Filtered/Clipped Maps

Show only certain regions:

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {
      fill: d => d.properties.region === "West" ? "steelblue" : "#eee",
      stroke: "white"
    }),

    // Highlight only western states
    Plot.geo(
      states.features.filter(d => d.properties.region === "West"),
      {
        fill: d => d.properties.value,
        stroke: "black",
        strokeWidth: 2
      }
    )
  ]
})
```

## Advanced Techniques

### Hexbin on Map

Combine geographic projection with hexagonal binning:

```javascript
Plot.plot({
  projection: "mercator",
  marks: [
    // Base map
    Plot.geo(regions, {fill: "lightgray", stroke: "white"}),

    // Hexbin data layer
    Plot.dot(points, Plot.hexbin(
      {fill: "count"},
      {x: "longitude", y: "latitude", binWidth: 30}
    ))
  ],
  color: {scheme: "YlOrRd", legend: true}
})
```

### Contour on Map

Show density or values as contour lines:

```javascript
Plot.plot({
  projection: "mercator",
  marks: [
    // Base map
    Plot.geo(regions, {fill: "#f5f5f5"}),

    // Contours
    Plot.contour(gridPoints, {
      x: "longitude",
      y: "latitude",
      fill: "value",
      stroke: "black",
      strokeWidth: 0.5
    })
  ],
  color: {scheme: "RdYlBu", symmetric: true}
})
```

### Animated/Temporal Maps

Multiple maps in facets for temporal progression:

```javascript
const dataByYear = [
  {year: 2010, features: [...states with 2010 data]},
  {year: 2015, features: [...]},
  {year: 2020, features: [...]}
];

Plot.plot({
  fx: {label: "Year"},
  projection: "albers-usa",
  color: {scheme: "Blues", legend: true},
  marks: dataByYear.map(({year, features}) =>
    Plot.geo(features, {
      fx: () => year,
      fill: "value",
      stroke: "white"
    })
  )
})
```

## Performance Considerations

### Large Datasets

**Problem**: Many features or high-resolution geometries slow rendering

**Solutions**:
1. **Simplify geometries** - Use TopoJSON (built-in simplification)
2. **Reduce detail** - Use lower resolution (110m instead of 10m)
3. **Filter features** - Show only relevant regions
4. **Use hexbin** - Aggregate points into hexagons
5. **Use density** - Replace individual points with density contours

### Memory Usage

```javascript
// Calculate GeoJSON size
const size = JSON.stringify(geojson).length / (1024 * 1024);
console.log(`GeoJSON size: ${size.toFixed(2)} MB`);

// Simplify if needed (using topojson-simplify)
const simplified = topojson.presimplify(geojson);
```

### Rendering Optimization

```javascript
// Reduce stroke width for small features
Plot.geo(geojson, {
  stroke: "white",
  strokeWidth: features.length > 1000 ? 0.25 : 1  // Thinner for many features
})

// Use opacity for overlapping regions
Plot.geo(geojson, {
  fill: "value",
  fillOpacity: 0.8  // Slightly transparent
})

// Limit color precision for faster rendering
color: {scheme: "Blues", domain: [0, 10, 20, 30, 40, 50]}  // Discrete levels
```

## Troubleshooting

### Map Appears Blank
- Check projection domain fits data
- Verify coordinates are [longitude, latitude]
- Ensure GeoJSON is valid (test at geojson.io)

### Features Don't Align
- Verify coordinate system (WGS84/EPSG:4326 is standard)
- Check for holes/rings in polygons
- Test with simpler geometry first

### Performance Issues
- Reduce number of features
- Simplify geometries
- Use TopoJSON instead of GeoJSON
- Use hexbin/density for point data

### Wrong Projection
- Start with mercator (most familiar)
- Use albers-usa for US-specific data
- Use equal-earth for world maps
- Test different projections on your data

## Related Examples

- [choropleth-map.md](examples/choropleth-map.md) - Complete choropleth examples
- [vector-fields.md](examples/vector-fields.md) - Geographic vector fields
- [hexbin-heatmap.md](examples/hexbin-heatmap.md) - Hexbin on maps

## Related Reference

- [projections.md](projections.md) - All projection types and options
- [marks.md](marks.md) - Complete mark reference
- [scales.md](scales.md) - Color and scale configuration

## External Resources

**GeoJSON Standards**:
- https://tools.ietf.org/html/rfc7946 - Official GeoJSON spec
- https://geojson.io - Online GeoJSON editor and validator

**Data Sources**:
- https://www.naturalearthdata.com/ - Natural Earth
- https://gadm.org/ - GADM boundaries
- https://www.openstreetmap.org/ - OpenStreetMap

**Tools**:
- https://mapshaper.org/ - Simplify/convert geographic data
- https://github.com/topojson/topojson-client - TopoJSON utilities
- https://leafletjs.com/ - Web mapping reference

## D3 Integration

Observable Plot uses D3 for projections. For advanced geographic operations, use D3 directly:

```javascript
import * as d3 from "d3-geo";

// Create custom projection
const projection = d3.geoMercator();

// Get bounds
const bounds = d3.geoBounds(geojson);

// Get centroid
const centroid = d3.geoCentroid(geojson);

// Check if point in polygon
const pointInPolygon = d3.geoContains(feature, [lng, lat]);
```
