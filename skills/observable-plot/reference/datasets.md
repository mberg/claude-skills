# Sample Datasets Reference

Observable provides a collection of real-world datasets perfect for creating example visualizations. All datasets are hosted on GitHub and can be loaded directly via fetch.

**Repository**: https://github.com/observablehq/sample-datasets

## Available Datasets

### Apple Stock (aapl.csv)

**Description**: Historical Apple stock prices with date, open, high, low, close, and volume.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/aapl.csv

**Columns**: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`

**Use cases**: Time series, line charts, candlestick charts, volume charts

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/aapl.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.lineY(data, {x: "Date", y: "Close", stroke: "steelblue"})
  ]
})
```

---

### Alphabet Letter Frequency (alphabet.csv)

**Description**: Letter frequency in English text.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/alphabet.csv

**Columns**: `letter`, `frequency`

**Use cases**: Bar charts, sorted visualizations, text analysis

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/alphabet.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.barY(data, {x: "letter", y: "frequency", fill: "steelblue"})
  ]
})
```

---

### Olympic Athletes (athletes.csv)

**Description**: Olympic athletes with physical characteristics and sports.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/athletes.csv

**Columns**: `name`, `nationality`, `sex`, `height`, `weight`, `sport`, `gold`, `silver`, `bronze`

**Use cases**: Scatterplots, grouped visualizations, distribution analysis

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/athletes.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.dot(data, {x: "weight", y: "height", fill: "sex", tip: true})
  ]
})
```

---

### Automobile Data (cars.csv)

**Description**: Car characteristics including mpg, horsepower, weight, and origin.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/cars.csv

**Columns**: `Name`, `Miles_per_Gallon`, `Cylinders`, `Displacement`, `Horsepower`, `Weight_in_lbs`, `Acceleration`, `Year`, `Origin`

**Use cases**: Scatterplots, correlation analysis, grouped comparisons

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/cars.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "Weight_in_lbs",
      y: "Miles_per_Gallon",
      fill: "Origin",
      tip: true
    })
  ]
})
```

---

### Diamond Data (diamonds.csv)

**Description**: Diamond pricing with quality characteristics (carat, cut, color, clarity).

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/diamonds.csv

**Columns**: `carat`, `cut`, `color`, `clarity`, `depth`, `table`, `price`, `x`, `y`, `z`

**Use cases**: Price analysis, quality correlations, grouped visualizations

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/diamonds.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.dot(data, {x: "carat", y: "price", fill: "cut", r: 2, tip: true})
  ]
})
```

---

### Software Dependencies (flare.csv)

**Description**: Hierarchical software package structure.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/flare.csv

**Columns**: `id`, `value`

**Use cases**: Tree diagrams, hierarchical visualizations, treemaps

---

### Global Temperature (gistemp.csv)

**Description**: Global surface temperature anomalies from NASA GISS.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/gistemp.csv

**Columns**: `Date`, `Anomaly`

**Use cases**: Climate visualization, time series, trend analysis

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/gistemp.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.lineY(data, {x: "Date", y: "Anomaly", stroke: "red"}),
    Plot.ruleY([0])
  ]
})
```

---

### Industry Sectors (industries.csv)

**Description**: Industry data with employees and wage information.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/industries.csv

**Columns**: `industry`, `employees`, `wages`

**Use cases**: Bar charts, comparisons, economic analysis

---

### Palmer Penguins (penguins.csv)

**Description**: Penguin morphological measurements from Palmer Station Antarctica.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/penguins.csv

**Columns**: `species`, `island`, `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, `sex`, `year`

**Use cases**: Scatterplots, grouped analysis, statistical visualizations, species comparison

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/penguins.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  color: {legend: true},
  marks: [
    Plot.dot(data, {
      x: "flipper_length_mm",
      y: "body_mass_g",
      fill: "species",
      tip: true
    })
  ]
})
```

---

### Seattle Weather (seattle-weather.csv)

**Description**: Daily weather observations from Seattle including temperature and precipitation.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/seattle-weather.csv

**Columns**: `date`, `precipitation`, `temp_max`, `temp_min`, `wind`, `weather`

**Use cases**: Time series, weather patterns, seasonal analysis, heatmaps

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/seattle-weather.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.lineY(data, {x: "date", y: "temp_max", stroke: "red"}),
    Plot.lineY(data, {x: "date", y: "temp_min", stroke: "blue"})
  ]
})
```

---

### US County Unemployment (us-county-unemployment.csv)

**Description**: Unemployment rates by US county.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/us-county-unemployment.csv

**Columns**: `id`, `rate`

**Use cases**: Choropleth maps, geographic visualization, county-level analysis

**Example** (requires GeoJSON):
```javascript
const unemployment = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/us-county-unemployment.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

const counties = await fetch("us-counties.json").then(r => r.json());

const unemploymentById = new Map(unemployment.map(d => [d.id, d.rate]));

Plot.plot({
  projection: "albers-usa",
  color: {scheme: "YlOrRd", legend: true},
  marks: [
    Plot.geo(counties, {
      fill: d => unemploymentById.get(d.id),
      stroke: "white",
      strokeWidth: 0.25
    })
  ]
})
```

---

### US State Capitals (us-state-capitals.json)

**Description**: US state capitals with names and coordinates.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/us-state-capitals.json

**Columns**: `name`, `lat`, `lon`, `description`

**Use cases**: Geographic visualization, point maps, labeled maps

**Example**:
```javascript
const capitals = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/us-state-capitals.json"
).then(r => r.json());

Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.dot(capitals, {
      x: "lon",
      y: "lat",
      r: 5,
      fill: "steelblue",
      tip: true
    }),
    Plot.text(capitals, {
      x: "lon",
      y: "lat",
      text: "description",
      dy: -10,
      fontSize: 8
    })
  ]
})
```

---

### World Population (world-population.csv)

**Description**: Historical world population data.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/world-population.csv

**Columns**: `year`, `population`

**Use cases**: Time series, historical trends, population growth visualization

**Example**:
```javascript
const data = await fetch(
  "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/world-population.csv"
).then(r => r.text()).then(text => d3.csvParse(text, d3.autoType));

Plot.plot({
  marks: [
    Plot.lineY(data, {x: "year", y: "population", stroke: "steelblue"}),
    Plot.dot(data, {x: "year", y: "population", fill: "steelblue"})
  ]
})
```

---

## Loading Data

### CSV Files

```javascript
const data = await fetch(url)
  .then(response => response.text())
  .then(text => d3.csvParse(text, d3.autoType));
```

### JSON Files

```javascript
const data = await fetch(url)
  .then(response => response.json());
```

### Type Inference

Use `d3.autoType` to automatically infer column types (numbers, dates, booleans):

```javascript
d3.csvParse(text, d3.autoType)  // Automatic type inference
```

Or specify types manually:

```javascript
d3.csvParse(text, d => ({
  date: new Date(d.date),
  value: +d.value,
  category: d.category
}))
```

## Common Patterns

### Filter After Loading

```javascript
const data = await fetch(url)
  .then(r => r.text())
  .then(text => d3.csvParse(text, d3.autoType))
  .then(data => data.filter(d => d.value > 0));
```

### Sample Large Datasets

```javascript
const data = await fetch(url)
  .then(r => r.text())
  .then(text => d3.csvParse(text, d3.autoType))
  .then(data => data.slice(0, 1000));  // First 1000 rows
```

### Handle Missing Data

```javascript
const data = await fetch(url)
  .then(r => r.text())
  .then(text => d3.csvParse(text, d3.autoType))
  .then(data => data.filter(d => d.value != null));
```
