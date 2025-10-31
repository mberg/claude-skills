# Choropleth Map Examples

Choropleth maps visualize data values across geographic regions using color encoding. Plot uses the `Plot.geo()` mark with GeoJSON data and geographic projections.

## Basic Choropleth Map

```javascript
import * as Plot from "@observablehq/plot";

// GeoJSON FeatureCollection with data properties
const states = {
  type: "FeatureCollection",
  features: [
    {
      type: "Feature",
      properties: {name: "California", value: 39.5},
      geometry: {...}  // GeoJSON geometry
    },
    {
      type: "Feature",
      properties: {name: "Texas", value: 29.0},
      geometry: {...}
    }
    // ... more features
  ]
};

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "YlOrRd",
    legend: true,
    label: "Population (millions)"
  },
  marks: [
    Plot.geo(states, {
      fill: d => d.properties.value,
      stroke: "white",
      strokeWidth: 0.5,
      tip: true
    })
  ]
}).display();
```

## With External Data Join

Join external data to geographic features:

```javascript
// Geographic features
const counties = await fetch("counties.json").then(r => r.json());

// Separate data array
const unemploymentData = [
  {fips: "06001", rate: 4.2},
  {fips: "06003", rate: 5.1},
  // ... more data
];

// Create lookup
const dataByFips = new Map(unemploymentData.map(d => [d.fips, d]));

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "BuPu",
    legend: true,
    label: "Unemployment rate (%)"
  },
  marks: [
    Plot.geo(counties, {
      fill: d => dataByFips.get(d.properties.fips)?.rate,
      stroke: "white",
      strokeWidth: 0.25,
      tip: true
    })
  ]
}).display();
```

## Multiple Projections

Try different geographic projections:

```javascript
const world = await fetch("countries.json").then(r => r.json());

// Mercator projection
Plot.plot({
  projection: "mercator",
  marks: [
    Plot.geo(world, {fill: "lightgray", stroke: "white"})
  ]
}).display();

// Equal Earth projection
Plot.plot({
  projection: "equal-earth",
  marks: [
    Plot.geo(world, {fill: "lightgray", stroke: "white"})
  ]
}).display();

// Orthographic (globe)
Plot.plot({
  projection: {
    type: "orthographic",
    rotate: [-100, -30]
  },
  marks: [
    Plot.sphere(),  // Ocean background
    Plot.geo(world, {fill: "lightgray", stroke: "white"})
  ]
}).display();
```

## Layered Geographic Visualization

Combine multiple geographic marks:

```javascript
const states = await fetch("us-states.json").then(r => r.json());
const cities = [
  {name: "New York", lon: -74.0, lat: 40.7, population: 8.3},
  {name: "Los Angeles", lon: -118.2, lat: 34.0, population: 3.9},
  {name: "Chicago", lon: -87.6, lat: 41.9, population: 2.7}
];

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "YlOrRd",
    legend: true,
    label: "Population (millions)"
  },
  marks: [
    // Background states
    Plot.geo(states, {
      fill: "lightgray",
      stroke: "white"
    }),

    // City points
    Plot.dot(cities, {
      x: "lon",
      y: "lat",
      r: d => Math.sqrt(d.population) * 3,
      fill: "steelblue",
      stroke: "white",
      strokeWidth: 1,
      tip: true
    }),

    // City labels
    Plot.text(cities, {
      x: "lon",
      y: "lat",
      text: "name",
      dy: -12,
      fontSize: 10,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Diverging Color Scale

Show positive and negative values:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

// Data with positive and negative values
const changeData = new Map([
  ["California", 2.1],
  ["Texas", 3.5],
  ["New York", -0.3],
  ["Florida", 1.8],
  ["Illinois", -0.5]
]);

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "RdBu",
    legend: true,
    label: "Population change (%)",
    symmetric: true  // Center at 0
  },
  marks: [
    Plot.geo(states, {
      fill: d => changeData.get(d.properties.name) || 0,
      stroke: "white",
      tip: true
    })
  ]
}).display();
```

## Categorical Choropleth

Use discrete categories instead of continuous values:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

const regions = new Map([
  ["California", "West"],
  ["Oregon", "West"],
  ["Texas", "South"],
  ["Florida", "South"],
  ["New York", "Northeast"],
  // ... more mappings
]);

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "tableau10",
    legend: true,
    label: "Region"
  },
  marks: [
    Plot.geo(states, {
      fill: d => regions.get(d.properties.name),
      stroke: "white",
      strokeWidth: 0.5
    })
  ]
}).display();
```

## Small Multiples (Faceted Maps)

Show multiple time periods or categories:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

const dataByYearAndState = [
  {year: 2010, state: "California", value: 37.3},
  {year: 2010, state: "Texas", value: 25.1},
  {year: 2020, state: "California", value: 39.5},
  {year: 2020, state: "Texas", value: 29.0}
  // ... more data
];

// Create lookup
const lookup = new Map(
  dataByYearAndState.map(d => [`${d.year}-${d.state}`, d.value])
);

Plot.plot({
  projection: "albers-usa",
  fx: {label: "Year"},
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.geo(states, {
      fx: (d, i, data) => 2010,  // Repeat for each year
      fill: d => lookup.get(`2010-${d.properties.name}`),
      stroke: "white"
    }),
    Plot.geo(states, {
      fx: (d, i, data) => 2020,
      fill: d => lookup.get(`2020-${d.properties.name}`),
      stroke: "white"
    })
  ]
}).display();
```

## Interactive Choropleth

Add interactivity with tips and highlighting:

```javascript
const states = await fetch("us-states.json").then(r => r.json());

Plot.plot({
  projection: "albers-usa",
  color: {
    scheme: "YlGnBu",
    legend: true,
    label: "Value"
  },
  marks: [
    Plot.geo(states, {
      fill: d => d.properties.value,
      stroke: "white",
      strokeWidth: 0.5,
      tip: true,
      channels: {
        Name: d => d.properties.name,
        Value: d => d.properties.value
      }
    })
  ]
}).display();
```

## Point-Based Choropleth (Hexbin Map)

Combine geographic boundaries with hexbin:

```javascript
const states = await fetch("us-states.json").then(r => r.json());
const events = Array.from({length: 1000}, () => ({
  lon: -125 + Math.random() * 50,
  lat: 25 + Math.random() * 25
}));

Plot.plot({
  projection: "albers-usa",
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    // State boundaries (background)
    Plot.geo(states, {
      fill: "none",
      stroke: "lightgray",
      strokeWidth: 1
    }),

    // Hexbin heatmap
    Plot.dot(events, Plot.hexbin(
      {fill: "count"},
      {
        x: "lon",
        y: "lat",
        binWidth: 30,
        r: 10
      }
    ))
  ]
}).display();
```

## Key Patterns

### Basic Geo Mark
```javascript
Plot.geo(geojson, {
  fill: "column",        // Color encoding
  stroke: "white",       // Boundary color
  strokeWidth: 0.5,      // Boundary width
  tip: true              // Interactive tooltip
})
```

### Projections
Common projection types:
- `"albers-usa"`: US-specific (includes Alaska, Hawaii)
- `"mercator"`: Web maps (preserves angles)
- `"equal-earth"`: Equal-area world map
- `"orthographic"`: Globe view
- `"azimuthal-equal-area"`: Polar regions

```javascript
{
  projection: {
    type: "orthographic",
    rotate: [lon, lat],  // Center point
    domain: geojson      // Auto-fit bounds
  }
}
```

### Color Schemes for Choropleth
- **Sequential**: `"YlOrRd"`, `"YlGnBu"`, `"Purples"` (one direction)
- **Diverging**: `"RdBu"`, `"RdYlGn"`, `"Spectral"` (two directions from center)
- **Categorical**: `"tableau10"`, `"category10"` (discrete categories)

Use `symmetric: true` for diverging scales centered at zero.

### Data Join Patterns
```javascript
// Create lookup from external data
const dataMap = new Map(data.map(d => [d.id, d.value]));

// Use in geo mark
Plot.geo(features, {
  fill: d => dataMap.get(d.properties.id)
})
```

### Layering Order
1. Ocean/background (`Plot.sphere()`)
2. Graticule/grid (`Plot.graticule()`)
3. Filled regions (`Plot.geo()` with fill)
4. Points/symbols (`Plot.dot()`, `Plot.text()`)
5. Boundaries (`Plot.geo()` with stroke only)

### Missing Data
Handle missing values explicitly:
```javascript
fill: d => dataMap.get(d.id) ?? "lightgray"
```

## Related Examples
- [hexbin-heatmap.md](hexbin-heatmap.md) - Spatial density on maps
- [faceted-plot.md](faceted-plot.md) - Multiple maps in small multiples

## Reference
- [geographic.md](../geographic.md) - Complete geographic visualization guide (GeoJSON, projections, patterns)
- [marks.md](../marks.md) - Geo mark options and documentation
- [projections.md](../projections.md) - All projection types and configuration
- [scales.md](../scales.md) - Color schemes and scale configuration
