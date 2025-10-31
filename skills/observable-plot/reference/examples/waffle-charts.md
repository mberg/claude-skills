# Waffle Chart Examples

Waffle charts use small squares or units to represent proportions and quantities. Observable Plot provides the `Plot.cell()` and `Plot.waffle()` marks for creating these visualizations.

## Basic Waffle Chart

Simple proportion visualization:

```javascript
import * as Plot from "@observablehq/plot";

// Generate waffle grid (10x10 = 100 units)
const waffleData = [];
for (let i = 0; i < 100; i++) {
  waffleData.push({
    index: i,
    row: Math.floor(i / 10),
    col: i % 10,
    category: i < 35 ? "Category A" :
               i < 70 ? "Category B" :
               "Category C"
  });
}

Plot.plot({
  width: 400,
  height: 400,
  aspectRatio: 1,
  axis: null,
  color: {
    domain: ["Category A", "Category B", "Category C"],
    range: ["#1f77b4", "#ff7f0e", "#2ca02c"],
    legend: true
  },
  marks: [
    Plot.cell(waffleData, {
      x: "col",
      y: "row",
      fill: "category",
      inset: 1,
      tip: true
    })
  ]
}).display();
```

## Stacked Waffle Chart

Multiple categories stacked vertically:

```javascript
const categories = [
  {name: "Product A", value: 45, row: 0},
  {name: "Product B", value: 30, row: 1},
  {name: "Product C", value: 25, row: 2}
];

const stackedWaffle = [];
categories.forEach(cat => {
  for (let i = 0; i < cat.value; i++) {
    stackedWaffle.push({
      category: cat.name,
      row: cat.row,
      col: i,
      value: 1
    });
  }
});

Plot.plot({
  width: 600,
  height: 200,
  axis: null,
  color: {
    scheme: "category10",
    legend: true
  },
  marks: [
    Plot.cell(stackedWaffle, {
      x: "col",
      y: "row",
      fill: "category",
      inset: 0.5,
      tip: true
    })
  ]
}).display();
```

## Survey Results Waffle

100-unit waffle for percentage visualization:

```javascript
const survey = [
  {response: "Strongly Agree", count: 28},
  {response: "Agree", count: 42},
  {response: "Neutral", count: 15},
  {response: "Disagree", count: 10},
  {response: "Strongly Disagree", count: 5}
];

// Generate 100 squares
const surveyWaffle = [];
let currentIndex = 0;

survey.forEach(item => {
  for (let i = 0; i < item.count; i++) {
    surveyWaffle.push({
      index: currentIndex++,
      row: Math.floor((currentIndex - 1) / 10),
      col: (currentIndex - 1) % 10,
      response: item.response
    });
  }
});

Plot.plot({
  width: 500,
  height: 500,
  aspectRatio: 1,
  axis: null,
  color: {
    domain: ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
    range: ["#d73027", "#fc8d59", "#fee08b", "#91cf60", "#1a9850"],
    legend: true
  },
  marks: [
    Plot.cell(surveyWaffle, {
      x: "col",
      y: "row",
      fill: "response",
      inset: 1.5,
      rx: 2,  // Rounded corners
      tip: true
    })
  ]
}).display();
```

## Part-to-Whole Waffle

Showing portion of total:

```javascript
// 73 out of 100
const partToWhole = [];
for (let i = 0; i < 100; i++) {
  partToWhole.push({
    index: i,
    row: Math.floor(i / 10),
    col: i % 10,
    filled: i < 73
  });
}

Plot.plot({
  title: "73% Completion Rate",
  width: 400,
  height: 400,
  axis: null,
  marks: [
    Plot.cell(partToWhole, {
      x: "col",
      y: "row",
      fill: d => d.filled ? "#2ca02c" : "#e0e0e0",
      inset: 1,
      tip: true,
      channels: {
        Status: d => d.filled ? "Complete" : "Incomplete"
      }
    })
  ]
}).display();
```

## Icon/Pictogram Waffle

Using text symbols instead of squares:

```javascript
const pictogramData = [];
for (let i = 0; i < 50; i++) {
  pictogramData.push({
    row: Math.floor(i / 10),
    col: i % 10,
    category: i < 20 ? "Type A" : i < 35 ? "Type B" : "Type C"
  });
}

Plot.plot({
  width: 400,
  height: 200,
  axis: null,
  color: {
    domain: ["Type A", "Type B", "Type C"],
    scheme: "category10",
    legend: true
  },
  marks: [
    Plot.text(pictogramData, {
      x: "col",
      y: "row",
      text: "●",  // or use emoji/icons
      fill: "category",
      fontSize: 20,
      tip: true
    })
  ]
}).display();
```

## Comparison Waffle

Multiple waffle charts for comparison:

```javascript
const comparisonData = [
  {group: "2022", category: "Category A", count: 35},
  {group: "2022", category: "Category B", count: 45},
  {group: "2022", category: "Category C", count: 20},
  {group: "2023", category: "Category A", count: 40},
  {group: "2023", category: "Category B", count: 38},
  {group: "2023", category: "Category C", count: 22}
];

const comparisonWaffle = [];
comparisonData.forEach(item => {
  const groupOffset = item.group === "2022" ? 0 : 11;  // Space between groups

  for (let i = 0; i < item.count; i++) {
    const existing = comparisonWaffle.filter(d =>
      d.group === item.group
    ).length;

    comparisonWaffle.push({
      group: item.group,
      category: item.category,
      row: Math.floor(existing / 10),
      col: (existing % 10) + groupOffset
    });
  }
});

Plot.plot({
  width: 800,
  height: 400,
  axis: null,
  color: {
    scheme: "category10",
    legend: true
  },
  marks: [
    Plot.cell(comparisonWaffle, {
      x: "col",
      y: "row",
      fill: "category",
      inset: 1,
      tip: true,
      channels: {
        Group: "group",
        Category: "category"
      }
    }),

    // Labels
    Plot.text(["2022", "2023"], {
      x: [5, 16],
      y: -1,
      text: d => d,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Faceted Waffle Charts

Small multiples of waffle charts:

```javascript
const facetedData = [];
const groups = ["Region A", "Region B", "Region C"];

groups.forEach((region, regionIndex) => {
  for (let i = 0; i < 100; i++) {
    facetedData.push({
      region,
      row: Math.floor(i / 10),
      col: i % 10,
      category: i < 30 + regionIndex * 5 ? "Cat 1" :
                 i < 70 ? "Cat 2" :
                 "Cat 3"
    });
  }
});

Plot.plot({
  fx: {label: null},
  axis: null,
  color: {
    scheme: "tableau10",
    legend: true
  },
  marks: [
    Plot.cell(facetedData, {
      fx: "region",
      x: "col",
      y: "row",
      fill: "category",
      inset: 0.5,
      tip: true
    }),

    // Region labels
    Plot.text(facetedData, {
      fx: "region",
      x: 4.5,
      y: -1,
      text: "region",
      fontWeight: "bold",
      frameAnchor: "top"
    })
  ]
}).display();
```

## Rounded/Styled Waffle

Custom styling for visual appeal:

```javascript
const styledData = [];
for (let i = 0; i < 100; i++) {
  styledData.push({
    row: Math.floor(i / 10),
    col: i % 10,
    value: i < 62,
    index: i
  });
}

Plot.plot({
  width: 450,
  height: 450,
  axis: null,
  marks: [
    Plot.cell(styledData, {
      x: "col",
      y: "row",
      fill: d => d.value ? "#FF6B6B" : "#f0f0f0",
      inset: 2,
      rx: 3,  // Rounded corners
      tip: true,
      channels: {
        Value: d => d.value ? "Yes" : "No",
        Index: "index"
      }
    })
  ]
}).display();
```

## Progress Waffle

Show completion status:

```javascript
const progressData = [];
const total = 100;
const completed = 67;
const inProgress = 18;
const notStarted = 15;

let index = 0;
for (let i = 0; i < completed; i++) {
  progressData.push({
    row: Math.floor(index / 10),
    col: index % 10,
    status: "Completed"
  });
  index++;
}
for (let i = 0; i < inProgress; i++) {
  progressData.push({
    row: Math.floor(index / 10),
    col: index % 10,
    status: "In Progress"
  });
  index++;
}
for (let i = 0; i < notStarted; i++) {
  progressData.push({
    row: Math.floor(index / 10),
    col: index % 10,
    status: "Not Started"
  });
  index++;
}

Plot.plot({
  title: "Project Status",
  width: 500,
  height: 500,
  axis: null,
  color: {
    domain: ["Completed", "In Progress", "Not Started"],
    range: ["#2ecc71", "#f39c12", "#ecf0f1"],
    legend: true
  },
  marks: [
    Plot.cell(progressData, {
      x: "col",
      y: "row",
      fill: "status",
      inset: 1.5,
      rx: 2,
      tip: true
    })
  ]
}).display();
```

## Key Patterns

### Grid Generation
```javascript
// 10x10 grid (100 units)
const grid = [];
for (let i = 0; i < 100; i++) {
  grid.push({
    row: Math.floor(i / 10),
    col: i % 10,
    // ... other properties
  });
}
```

### Cell Mark
```javascript
Plot.cell(data, {
  x: "col",          // Column position
  y: "row",          // Row position
  fill: "category",  // Color encoding
  inset: 1,          // Gap between cells
  rx: 2,             // Rounded corners
  tip: true
})
```

### Color Schemes
```javascript
// Diverging (for agree/disagree)
range: ["#d73027", "#fc8d59", "#fee08b", "#91cf60", "#1a9850"]

// Sequential (for intensity)
scheme: "blues"

// Categorical
scheme: "category10"
```

### Sizing
```javascript
{
  width: 400,
  height: 400,
  aspectRatio: 1,  // Square grid
  axis: null       // Hide axes
}
```

## Common Use Cases

- **Survey results** (percentage breakdowns)
- **Progress tracking** (completion rates)
- **Part-to-whole** (proportion visualization)
- **Demographic data** (population breakdowns)
- **Comparison** (side-by-side proportions)
- **Status boards** (completed/in-progress/pending)

## Design Guidelines

1. **Use 100 units** for easy percentage interpretation
2. **Order matters** - arrange by category importance
3. **Limit colors** - 3-5 categories maximum
4. **Add legends** - always include color legend
5. **Round corners** - softer appearance with `rx` option
6. **Spacing** - use `inset` for clear separation

## Related Examples
- [diverging-stacked-bars.md](diverging-stacked-bars.md) - Alternative for Likert scales
- [heatmaps.md](heatmaps.md) - Continuous value grids

## Reference
- [reference/marks.md](../marks.md) - Cell mark documentation
