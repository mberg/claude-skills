# Transform Reference

Transforms process data within Plot specifications, eliminating the need for external data wrangling. Transforms are composable and can be chained together.

## Aggregation Transforms

### Plot.groupX(outputs, options) / Plot.groupY(outputs, options) / Plot.groupZ(outputs, options)

Groups data by one or more dimensions and applies aggregation functions.

**Outputs**: Object mapping channel names to reducer functions
**Common reducers**: `"count"`, `"sum"`, `"mean"`, `"median"`, `"min"`, `"max"`, `"mode"`, `"deviation"`, `"variance"`

**Example**:
```javascript
// Group by x, sum y values
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "value"}))

// Group by x, count occurrences
Plot.barY(data, Plot.groupX({y: "count"}, {x: "category"}))

// Multiple aggregations
Plot.dot(data, Plot.groupX(
  {y: "mean", r: "count"},
  {x: "category", y: "value"}
))
```

### Plot.binX(outputs, options) / Plot.binY(outputs, options)

Bins continuous data into discrete intervals (histograms).

**Outputs**: Aggregation functions for each bin
**Options**: `thresholds` (number or array), `domain`, `cumulative`

**Example**:
```javascript
// Histogram with auto bins
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))

// Custom thresholds
Plot.rectY(data, Plot.binX(
  {y: "count"},
  {x: "score", thresholds: [0, 60, 70, 80, 90, 100]}
))

// Cumulative distribution
Plot.lineY(data, Plot.binX(
  {y: "count"},
  {x: "value", cumulative: true}
))
```

### Plot.hexbin(outputs, options)

Bins 2D points into hexagonal bins.

**Outputs**: Aggregations for each hex
**Options**: `binWidth`, `r` (visual radius)

**Example**:
```javascript
// Color by count
Plot.dot(data, Plot.hexbin(
  {fill: "count"},
  {x: "x", y: "y", binWidth: 10}
))

// Size by count, color by mean
Plot.dot(data, Plot.hexbin(
  {r: "count", fill: "mean"},
  {x: "x", y: "y", z: "value"}
))
```

## Positional Transforms

### Plot.stackY(options) / Plot.stackX(options)

Stacks values vertically (stackY) or horizontally (stackX).

**Options**: `offset`, `order`
**Offset values**: `null` (default), `"expand"` (normalize to 100%), `"center"`, `"wiggle"`
**Order values**: `null`, `"sum"`, `"appearance"`, `"inside-out"`

**Example**:
```javascript
// Basic stacking
Plot.barY(data, Plot.stackY({x: "quarter", y: "revenue", fill: "product"}))

// Normalized (100%) stacking
Plot.barY(data, Plot.stackY({
  offset: "expand",
  x: "quarter",
  y: "revenue",
  fill: "product"
}))

// Streamgraph (centered)
Plot.areaY(data, Plot.stackY({
  offset: "center",
  x: "year",
  y: "value",
  fill: "category"
}))
```

### Plot.dodge(options)

Shifts overlapping marks to avoid collision (beeswarm plots).

**Options**: `anchor`, `padding`

**Example**:
```javascript
Plot.dot(data, Plot.dodge({
  x: "category",
  r: 5,
  fill: "steelblue"
}))
```

### Plot.shift(interval, options)

Shifts data by a time interval.

**Example**:
```javascript
// Compare current vs previous period
Plot.lineY(data, {x: "date", y: "value", stroke: "current"})
Plot.lineY(data, Plot.shift("month", {
  x: "date",
  y: "value",
  stroke: "previous"
}))
```

## Statistical Transforms

### Plot.normalizeY(basis, options) / Plot.normalizeX(basis, options)

Normalizes values to a specified basis.

**Basis values**: `"first"`, `"last"`, `"sum"`, `"extent"`, `"min"`, `"max"`, `"mean"`, `"median"`, `"deviation"`, number

**Example**:
```javascript
// Normalize to first value (index to 100)
Plot.lineY(data, Plot.normalizeY("first", {
  x: "date",
  y: "value",
  stroke: "series"
}))

// Normalize to sum (show proportions)
Plot.areaY(data, Plot.stackY(Plot.normalizeY("sum", {
  x: "date",
  y: "value",
  fill: "category"
})))
```

### Plot.windowY(options) / Plot.windowX(options)

Applies a moving window function (rolling averages, etc.).

**Options**: `k` (window size), `anchor`, `reduce`, `strict`
**Reduce values**: `"mean"`, `"median"`, `"sum"`, `"min"`, `"max"`, `"deviation"`

**Example**:
```javascript
// 7-day moving average
Plot.lineY(data, Plot.windowY(
  {k: 7},
  {x: "date", y: "value"}
))

// Median smoothing
Plot.lineY(data, Plot.windowY(
  {k: 5, reduce: "median"},
  {x: "date", y: "value"}
))
```

## Filtering Transforms

### Plot.filter(test, options)

Filters data based on a predicate function.

**Example**:
```javascript
// Filter positive values
Plot.dot(data, Plot.filter(
  d => d.value > 0,
  {x: "x", y: "value"}
))

// Filter by channel
Plot.dot(data, {
  x: "x",
  y: "y",
  filter: d => d.category === "A"
})
```

### Plot.select(selector, options)

Selects specific data points from each group.

**Selector values**: `"first"`, `"last"`, `"min"`, `"max"`, `"minIndex"`, `"maxIndex"`

**Example**:
```javascript
// Select maximum value per category
Plot.dot(data, Plot.selectMaxY({
  x: "category",
  y: "value"
}))

// Select first and last points
Plot.dot(data, Plot.select({
  selector: "first",
  x: "date",
  y: "value",
  fill: "series"
}))
```

### Plot.interval(period, options)

Filters data to regular intervals.

**Period values**: `"year"`, `"month"`, `"week"`, `"day"`, `"hour"`, etc.

**Example**:
```javascript
// Show monthly data points only
Plot.dot(data, Plot.interval(
  "month",
  {x: "date", y: "value"}
))
```

## Ordering Transforms

### Plot.sort(order, options)

Sorts data by a channel or comparator.

**Order values**: Channel name, `{channel: "ascending"}`, `{channel: "descending"}`, comparator function

**Example**:
```javascript
// Sort by y value descending
Plot.barY(data, Plot.sort(
  {y: "descending"},
  {x: "category", y: "value"}
))

// Sort by custom function
Plot.barY(data, Plot.sort(
  (a, b) => b.value - a.value,
  {x: "name", y: "value"}
))
```

### Plot.reverse(options)

Reverses the data order.

**Example**:
```javascript
Plot.barY(data, Plot.reverse({x: "category", y: "value"}))
```

## Spatial Transforms

### Plot.centroid(options)

Computes centroids of geographic features.

**Example**:
```javascript
Plot.dot(geojson, Plot.centroid({
  fill: "value",
  r: 5
}))
```

### Plot.tree(options)

Hierarchical tree layout transform.

**Example**:
```javascript
Plot.tree(hierarchy, Plot.treeLink())
```

## Mapping Transforms

### Plot.map(mappers, options)

Applies custom mapping functions to channels.

**Example**:
```javascript
Plot.dot(data, Plot.map({
  x: d => d.x * 2,
  y: d => Math.log(d.y),
  fill: d => d.category.toUpperCase()
}, {x: "x", y: "y", fill: "category"}))
```

## Transform Composition

Transforms can be chained together for complex operations:

```javascript
// Group, then sort, then stack
Plot.barY(data, Plot.stackY(
  Plot.sort(
    {y: "descending"},
    Plot.groupX(
      {y: "sum"},
      {x: "category", y: "value", fill: "subcategory"}
    )
  )
))

// Bin, then normalize
Plot.areaY(data, Plot.normalizeY(
  "sum",
  Plot.binX(
    {y: "count"},
    {x: "value", fill: "category"}
  )
))
```

## Common Patterns

### Histogram
```javascript
Plot.rectY(data, Plot.binX({y: "count"}, {x: "value"}))
```

### Grouped Bar Chart
```javascript
Plot.barY(data, Plot.groupX({y: "sum"}, {x: "category", y: "value"}))
```

### Stacked Area Chart
```javascript
Plot.areaY(data, Plot.stackY({x: "date", y: "value", fill: "series"}))
```

### 100% Stacked
```javascript
Plot.areaY(data, Plot.stackY(Plot.normalizeY({
  x: "date",
  y: "value",
  fill: "series"
})))
```

### Moving Average
```javascript
Plot.lineY(data, Plot.windowY({k: 7}, {x: "date", y: "value"}))
```

### Hexbin Heatmap
```javascript
Plot.dot(data, Plot.hexbin({fill: "count"}, {x: "x", y: "y"}))
```

## Transform Order

When combining multiple transforms, order matters:

1. **Filter** - Remove unwanted data first
2. **Map** - Transform values
3. **Bin/Group** - Aggregate data
4. **Sort** - Order results
5. **Stack/Dodge** - Position adjustments
6. **Normalize** - Final value transformations

**Example**:
```javascript
Plot.barY(data,
  Plot.stackY(              // 4. Stack bars
    Plot.sort(              // 3. Sort by value
      {y: "descending"},
      Plot.groupX(          // 2. Group and sum
        {y: "sum"},
        Plot.filter(        // 1. Filter first
          d => d.year === 2023,
          {x: "category", y: "revenue", fill: "product"}
        )
      )
    )
  )
)
```

## Reducer Functions

Common aggregation functions for groupX/groupY/binX/binY:

- `"count"`: Count of items
- `"sum"`: Sum of values
- `"mean"`: Average
- `"median"`: Median value
- `"min"`, `"max"`: Minimum/maximum
- `"mode"`: Most common value
- `"deviation"`: Standard deviation
- `"variance"`: Variance
- `"first"`, `"last"`: First/last value
- Custom function: `(values) => ...`

**Example**:
```javascript
Plot.dot(data, Plot.groupX({
  y: "mean",           // Average y
  r: "count",          // Count as size
  fill: values => values[0].category  // Custom: first category
}, {x: "month", y: "value"}))
```

## Related Documentation
- [marks.md](marks.md) - Mark types that use transforms
- [common-patterns.md](common-patterns.md) - Transform recipes
