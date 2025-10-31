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

### City Wages (citywages.csv)

**Description**: Metropolitan area population and wage inequality data comparing 1980 and 2015. Includes population figures and 90th/10th percentile wage ratios for major US metro areas.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/citywages.csv

**Columns**: `Metro`, `POP_1980`, `LPOP_1980`, `R90_10_1980`, `POP_2015`, `LPOP_2015`, `R90_10_2015`, `nyt_display`, `state_display`, `highlight`

**Use cases**: Comparative analysis, wage inequality visualizations, population growth trends, time series comparisons

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

**Description**: Hierarchical software package structure from the Flare ActionScript visualization library. Contains package names and file sizes in a hierarchical format.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/flare.csv

**Columns**: `name`, `size`

**Use cases**: Tree diagrams, hierarchical visualizations, treemaps, sunburst charts

---


### Industry Sectors (industries.csv)

**Description**: Time series data of unemployment by industry sector from 2000-present. Tracks unemployed workers across major US industries including manufacturing, retail, services, and more.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/industries.csv

**Columns**: `date`, `industry`, `unemployed`

**Use cases**: Time series analysis, industry comparisons, unemployment trends, economic analysis

---

### Olympians (olympians.csv)

**Description**: Olympic athletes with physical characteristics, sports, and medal counts. Includes biographical data and performance statistics for Olympic competitors.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/olympians.csv

**Columns**: `id`, `name`, `nationality`, `sex`, `date_of_birth`, `height`, `weight`, `sport`, `gold`, `silver`, `bronze`, `info`

**Use cases**: Scatterplots, grouped visualizations, distribution analysis, medal statistics, athlete demographics

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

### Pizza (pizza.csv)

**Description**: Pizza sales data including orders, pricing, and revenue by pizza type. Contains daily transaction data with pizza categories (Classic, Specialty) and sizes.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/pizza.csv

**Columns**: `order_date`, `day_of_week`, `category`, `name`, `price`, `orders`, `revenue`

**Use cases**: Sales analysis, time series, revenue comparisons, categorical visualization, day-of-week patterns

---

### Weather (weather.csv)

**Description**: Daily weather observations for Seattle from 2012-2015. Includes temperature, precipitation, wind speed, and weather conditions.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/weather.csv

**Columns**: `location`, `date`, `precipitation`, `temp_max`, `temp_min`, `wind`, `weather`

**Use cases**: Time series, weather patterns, seasonal analysis, precipitation visualization, temperature trends

---

### Miserables (miserables.json)

**Description**: Character relationship network from Les Misérables. Contains nodes representing characters and links representing their relationships, structured for network graph visualizations.

**URL**: https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/miserables.json

**Structure**:
- `nodes`: Array of objects with `id` (character name) and `group` (community cluster)
- `links`: Array of objects with `source`, `target`, and `value` (relationship strength)

**Use cases**: Network diagrams, relationship visualization, force-directed graphs, community detection

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
