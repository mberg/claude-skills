# Heatmap Examples

Heatmaps use color to encode values in a 2D grid. Observable Plot provides the `Plot.cell()` mark for creating matrix-style heatmaps.

## Basic Heatmap

Simple value matrix:

```javascript
import * as Plot from "@observablehq/plot";

const heatmapData = [
  {x: "Mon", y: "9am", value: 12},
  {x: "Mon", y: "10am", value: 18},
  {x: "Mon", y: "11am", value: 25},
  {x: "Tue", y: "9am", value: 15},
  {x: "Tue", y: "10am", value: 22},
  {x: "Tue", y: "11am", value: 30},
  {x: "Wed", y: "9am", value: 20},
  {x: "Wed", y: "10am", value: 28},
  {x: "Wed", y: "11am", value: 35}
];

Plot.plot({
  color: {
    scheme: "YlOrRd",
    legend: true,
    label: "Value"
  },
  marks: [
    Plot.cell(heatmapData, {
      x: "x",
      y: "y",
      fill: "value",
      inset: 0.5,
      tip: true
    })
  ]
}).display();
```

## Calendar Heatmap

Day-by-day activity:

```javascript
// Generate year of data
const calendarData = [];
const startDate = new Date(2023, 0, 1);

for (let i = 0; i < 365; i++) {
  const date = new Date(startDate);
  date.setDate(date.getDate() + i);

  calendarData.push({
    date,
    week: Math.floor(i / 7),
    day: date.getDay(),
    value: Math.random() * 100
  });
}

Plot.plot({
  width: 900,
  height: 150,
  x: {label: "Week of Year"},
  y: {
    domain: [0, 1, 2, 3, 4, 5, 6],
    tickFormat: i => ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][i]
  },
  color: {
    scheme: "Greens",
    legend: true
  },
  marks: [
    Plot.cell(calendarData, {
      x: "week",
      y: "day",
      fill: "value",
      inset: 0.5,
      tip: true,
      channels: {
        Date: d => d.date.toLocaleDateString(),
        Value: "value"
      }
    })
  ]
}).display();
```

## Correlation Matrix

Show correlations between variables:

```javascript
const variables = ["Var1", "Var2", "Var3", "Var4"];

const correlations = [];
variables.forEach(var1 => {
  variables.forEach(var2 => {
    // Generate correlation value (-1 to 1)
    const corr = var1 === var2 ? 1 :
                 Math.random() * 2 - 1;

    correlations.push({
      var1,
      var2,
      correlation: corr
    });
  });
});

Plot.plot({
  aspectRatio: 1,
  color: {
    scheme: "RdBu",
    domain: [-1, 1],
    symmetric: true,
    legend: true,
    label: "Correlation"
  },
  marks: [
    Plot.cell(correlations, {
      x: "var1",
      y: "var2",
      fill: "correlation",
      inset: 0.5,
      tip: true
    }),

    // Add correlation values
    Plot.text(correlations, {
      x: "var1",
      y: "var2",
      text: d => d.correlation.toFixed(2),
      fill: d => Math.abs(d.correlation) > 0.5 ? "white" : "black",
      fontSize: 12
    })
  ]
}).display();
```

## Time Series Heatmap

Hour by day pattern:

```javascript
const timeData = [];
const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
const hours = Array.from({length: 24}, (_, i) => i);

days.forEach(day => {
  hours.forEach(hour => {
    timeData.push({
      day,
      hour,
      activity: Math.random() * 100
    });
  });
});

Plot.plot({
  marginLeft: 50,
  x: {label: "Hour of Day"},
  y: {label: "Day of Week"},
  color: {
    scheme: "Turbo",
    legend: true,
    label: "Activity Level"
  },
  marks: [
    Plot.cell(timeData, {
      x: "hour",
      y: "day",
      fill: "activity",
      tip: true
    })
  ]
}).display();
```

## Confusion Matrix

Classification results:

```javascript
const confusionData = [
  {actual: "Cat", predicted: "Cat", count: 85},
  {actual: "Cat", predicted: "Dog", count: 10},
  {actual: "Cat", predicted: "Bird", count: 5},
  {actual: "Dog", predicted: "Cat", count: 8},
  {actual: "Dog", predicted: "Dog", count: 90},
  {actual: "Dog", predicted: "Bird", count: 2},
  {actual: "Bird", predicted: "Cat", count: 12},
  {actual: "Bird", predicted: "Dog", count: 5},
  {actual: "Bird", predicted: "Bird", count: 83}
];

Plot.plot({
  aspectRatio: 1,
  x: {label: "Predicted"},
  y: {label: "Actual"},
  color: {
    scheme: "Blues",
    legend: true,
    label: "Count"
  },
  marks: [
    Plot.cell(confusionData, {
      x: "predicted",
      y: "actual",
      fill: "count",
      inset: 0.5,
      tip: true
    }),

    // Add counts
    Plot.text(confusionData, {
      x: "predicted",
      y: "actual",
      text: "count",
      fontSize: 14,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Geographic Grid Heatmap

State-by-metric matrix:

```javascript
const stateMetrics = [
  {state: "CA", metric: "GDP", value: 95},
  {state: "CA", metric: "Population", value: 90},
  {state: "CA", metric: "Area", value: 60},
  {state: "TX", metric: "GDP", value: 75},
  {state: "TX", metric: "Population", value: 70},
  {state: "TX", metric: "Area", value: 95},
  {state: "NY", metric: "GDP", value: 80},
  {state: "NY", metric: "Population", value: 65},
  {state: "NY", metric: "Area", value: 30}
];

Plot.plot({
  x: {label: "Metric"},
  y: {label: "State"},
  color: {
    scheme: "Viridis",
    legend: true
  },
  marks: [
    Plot.cell(stateMetrics, {
      x: "metric",
      y: "state",
      fill: "value",
      inset: 0.5,
      tip: true
    })
  ]
}).display();
```

## Presence/Absence Heatmap

Binary data visualization:

```javascript
const presenceData = [];
const features = ["Feature A", "Feature B", "Feature C", "Feature D"];
const items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"];

items.forEach(item => {
  features.forEach(feature => {
    presenceData.push({
      item,
      feature,
      present: Math.random() > 0.5
    });
  });
});

Plot.plot({
  x: {label: "Features"},
  y: {label: "Items"},
  marks: [
    Plot.cell(presenceData, {
      x: "feature",
      y: "item",
      fill: d => d.present ? "#2ecc71" : "#ecf0f1",
      inset: 0.5,
      tip: true,
      channels: {
        Status: d => d.present ? "Present" : "Absent"
      }
    })
  ]
}).display();
```

## Annotated Heatmap

With text labels:

```javascript
const annotatedData = [
  {row: "A", col: "X", value: 23, label: "Low"},
  {row: "A", col: "Y", value: 87, label: "High"},
  {row: "A", col: "Z", value: 45, label: "Med"},
  {row: "B", col: "X", value: 91, label: "High"},
  {row: "B", col: "Y", value: 12, label: "Low"},
  {row: "B", col: "Z", value: 67, label: "Med"},
  {row: "C", col: "X", value: 54, label: "Med"},
  {row: "C", col: "Y", value: 34, label: "Med"},
  {row: "C", col: "Z", value: 89, label: "High"}
];

Plot.plot({
  aspectRatio: 1,
  color: {
    scheme: "Spectral",
    reverse: true,
    legend: true
  },
  marks: [
    Plot.cell(annotatedData, {
      x: "col",
      y: "row",
      fill: "value",
      inset: 0.5,
      tip: true
    }),

    // Value labels
    Plot.text(annotatedData, {
      x: "col",
      y: "row",
      text: "value",
      dy: -5,
      fontSize: 12,
      fontWeight: "bold"
    }),

    // Category labels
    Plot.text(annotatedData, {
      x: "col",
      y: "row",
      text: "label",
      dy: 8,
      fontSize: 10,
      fill: "gray"
    })
  ]
}).display();
```

## Clustered Heatmap

With row/column ordering:

```javascript
const clusterData = [];
const rows = ["Gene1", "Gene2", "Gene3", "Gene4", "Gene5"];
const cols = ["Sample A", "Sample B", "Sample C", "Sample D"];

rows.forEach(row => {
  cols.forEach(col => {
    clusterData.push({
      row,
      col,
      expression: Math.random() * 10
    });
  });
});

// Sort for clustering effect (simplified)
clusterData.sort((a, b) => a.expression - b.expression);

Plot.plot({
  marginLeft: 70,
  x: {label: "Samples"},
  y: {label: "Genes"},
  color: {
    scheme: "RdYlGn",
    legend: true,
    label: "Expression Level"
  },
  marks: [
    Plot.cell(clusterData, {
      x: "col",
      y: "row",
      fill: "expression",
      tip: true
    })
  ]
}).display();
```

## Sparse Heatmap

Only show cells with data:

```javascript
const sparseData = [
  {x: 1, y: 1, value: 10},
  {x: 1, y: 5, value: 25},
  {x: 3, y: 2, value: 15},
  {x: 3, y: 4, value: 30},
  {x: 5, y: 1, value: 20},
  {x: 5, y: 3, value: 35},
  {x: 5, y: 5, value: 40}
];

Plot.plot({
  width: 400,
  height: 400,
  color: {
    scheme: "Reds",
    legend: true
  },
  marks: [
    // Background grid
    Plot.frame({fill: "#f5f5f5"}),

    // Data cells only
    Plot.cell(sparseData, {
      x: "x",
      y: "y",
      fill: "value",
      inset: 0.5,
      tip: true
    })
  ]
}).display();
```

## Key Patterns

### Cell Mark
```javascript
Plot.cell(data, {
  x: "xColumn",
  y: "yColumn",
  fill: "value",     // Color encoding
  inset: 0.5,        // Gap between cells
  tip: true
})
```

### Color Schemes
```javascript
// Sequential (single direction)
{color: {scheme: "Blues"}}
{color: {scheme: "YlOrRd"}}

// Diverging (two directions)
{color: {scheme: "RdBu", symmetric: true}}

// Perceptually uniform
{color: {scheme: "Viridis"}}
{color: {scheme: "Plasma"}}
```

### Text Overlay
```javascript
Plot.text(data, {
  x: "x",
  y: "y",
  text: "value",
  fill: d => d.value > threshold ? "white" : "black"
})
```

### Aspect Ratio
```javascript
{
  aspectRatio: 1,  // Square cells
  width: 600,
  height: 600
}
```

## Common Use Cases

- **Temporal patterns** (hour × day, day × month)
- **Correlations** (variable × variable matrix)
- **Confusion matrices** (actual × predicted)
- **Geographic comparisons** (state × metric)
- **Gene expression** (gene × sample)
- **Presence/absence** (item × feature)
- **Survey responses** (question × response category)

## Design Guidelines

1. **Choose appropriate color scheme**
   - Sequential for one-directional data
   - Diverging for positive/negative
   - Perceptually uniform for accuracy

2. **Add text labels** for small matrices

3. **Use tooltips** for detailed values

4. **Consider clustering** to reveal patterns

5. **White space** (inset) improves readability

6. **Limit size** - large matrices become hard to read

## Related Examples
- [waffle-charts.md](waffle-charts.md) - Categorical grids
- [hexbin-heatmap.md](hexbin-heatmap.md) - Continuous spatial density

## Reference
- [reference/marks.md](../marks.md) - Cell mark documentation
- [reference/scales.md](../scales.md) - Color schemes
