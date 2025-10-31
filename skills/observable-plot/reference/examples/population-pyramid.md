# Population Pyramid Examples

Population pyramids visualize age and gender distributions using diverging horizontal bars. These are special cases of diverging bar charts optimized for demographic data.

## Basic Population Pyramid

Age groups by gender:

```javascript
import * as Plot from "@observablehq/plot";

const populationData = [
  {age: "0-9", male: -12, female: 11},
  {age: "10-19", male: -15, female: 14},
  {age: "20-29", male: -18, female: 17},
  {age: "30-39", male: -16, female: 16},
  {age: "40-49", male: -14, female: 14},
  {age: "50-59", male: -12, female: 13},
  {age: "60-69", male: -9, female: 10},
  {age: "70-79", male: -6, female: 8},
  {age: "80+", male: -3, female: 5}
];

Plot.plot({
  marginLeft: 60,
  x: {
    label: "Population (millions)",
    tickFormat: d => Math.abs(d) + "M"
  },
  y: {label: "Age Group"},
  marks: [
    // Male (left)
    Plot.barX(populationData, {
      y: "age",
      x: "male",
      fill: "#3498db",
      tip: true,
      channels: {
        Gender: () => "Male",
        Population: d => Math.abs(d.male) + "M"
      }
    }),

    // Female (right)
    Plot.barX(populationData, {
      y: "age",
      x: "female",
      fill: "#e74c3c",
      tip: true,
      channels: {
        Gender: () => "Female",
        Population: d => d.female + "M"
      }
    }),

    // Center line
    Plot.ruleX([0], {stroke: "black", strokeWidth: 1}),

    // Labels
    Plot.text([{x: -10, y: "0-9", label: "Male"}], {
      x: "x", y: "y", text: "label", textAnchor: "end", dy: -20
    }),
    Plot.text([{x: 10, y: "0-9", label: "Female"}], {
      x: "x", y: "y", text: "label", textAnchor: "start", dy: -20
    })
  ]
}).display();
```

## Comparative Population Pyramids

Compare two time periods or regions:

```javascript
const comparison = [
  {age: "0-9", year: 2000, male: -10, female: 9},
  {age: "0-9", year: 2020, male: -8, female: 7},
  {age: "10-19", year: 2000, male: -12, female: 11},
  {age: "10-19", year: 2020, male: -10, female: 9},
  {age: "20-29", year: 2000, male: -14, female: 13},
  {age: "20-29", year: 2020, male: -15, female: 14},
  {age: "30-39", year: 2000, male: -13, female: 12},
  {age: "30-39", year: 2020, male: -16, female: 15},
  {age: "40-49", year: 2000, male: -11, female: 11},
  {age: "40-49", year: 2020, male: -14, female: 14},
  {age: "50+", year: 2000, male: -10, female: 12},
  {age: "50+", year: 2020, male: -15, female: 18}
];

Plot.plot({
  fx: {label: "Year"},
  marginLeft: 60,
  x: {
    label: "Population (millions)",
    tickFormat: d => Math.abs(d) + "M"
  },
  marks: [
    Plot.barX(comparison, {
      fx: "year",
      y: "age",
      x: "male",
      fill: "#3498db",
      tip: true
    }),
    Plot.barX(comparison, {
      fx: "year",
      y: "age",
      x: "female",
      fill: "#e74c3c",
      tip: true
    }),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Stacked Population Pyramid

Show subgroups within each gender:

```javascript
const stackedPop = [
  {age: "0-19", gender: "Male", race: "Group A", value: -15},
  {age: "0-19", gender: "Male", race: "Group B", value: -10},
  {age: "0-19", gender: "Female", race: "Group A", value: 14},
  {age: "0-19", gender: "Female", race: "Group B", value: 9},
  {age: "20-39", gender: "Male", race: "Group A", value: -20},
  {age: "20-39", gender: "Male", race: "Group B", value: -14},
  {age: "20-39", gender: "Female", race: "Group A", value: 19},
  {age: "20-39", gender: "Female", race: "Group B", value: 13},
  {age: "40-59", gender: "Male", race: "Group A", value: -16},
  {age: "40-59", gender: "Male", race: "Group B", value: -11},
  {age: "40-59", gender: "Female", race: "Group A", value: 17},
  {age: "40-59", gender: "Female", race: "Group B", value: 12},
  {age: "60+", gender: "Male", race: "Group A", value: -8},
  {age: "60+", gender: "Male", race: "Group B", value: -6},
  {age: "60+", gender: "Female", race: "Group A", value: 10},
  {age: "60+", gender: "Female", race: "Group B", value: 8}
];

Plot.plot({
  marginLeft: 60,
  x: {
    label: "Population (millions)",
    tickFormat: d => Math.abs(d) + "M"
  },
  color: {
    domain: ["Group A", "Group B"],
    legend: true
  },
  marks: [
    // Male side (stacked)
    Plot.barX(
      stackedPop.filter(d => d.gender === "Male"),
      Plot.stackX({
        y: "age",
        x: "value",
        fill: "race",
        tip: true
      })
    ),

    // Female side (stacked)
    Plot.barX(
      stackedPop.filter(d => d.gender === "Female"),
      Plot.stackX({
        y: "age",
        x: "value",
        fill: "race",
        tip: true
      })
    ),

    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Percentage-Based Pyramid

Normalize to percentages:

```javascript
const percentData = [
  {age: "0-9", male: -8.5, female: 8.2},
  {age: "10-19", male: -9.2, female: 8.8},
  {age: "20-29", male: -11.5, female: 11.0},
  {age: "30-39", male: -10.8, female: 10.5},
  {age: "40-49", male: -9.5, female: 9.7},
  {age: "50-59", male: -8.2, female: 8.8},
  {age: "60-69", male: -6.0, female: 6.8},
  {age: "70-79", male: -4.0, female: 5.5},
  {age: "80+", male: -2.0, female: 3.5}
];

Plot.plot({
  marginLeft: 60,
  x: {
    label: "Percentage of Total Population",
    tickFormat: d => Math.abs(d) + "%",
    domain: [-12, 12]
  },
  marks: [
    Plot.barX(percentData, {
      y: "age",
      x: "male",
      fill: "#3498db",
      tip: true
    }),
    Plot.barX(percentData, {
      y: "age",
      x: "female",
      fill: "#e74c3c",
      tip: true
    }),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Labeled Population Pyramid

With population counts displayed:

```javascript
const labeledData = [
  {age: "0-14", male: 15.2, female: 14.5},
  {age: "15-24", male: 12.8, female: 12.1},
  {age: "25-54", male: 35.5, female: 34.8},
  {age: "55-64", male: 10.2, female: 11.0},
  {age: "65+", male: 8.5, female: 12.3}
];

Plot.plot({
  marginLeft: 70,
  marginRight: 70,
  x: {
    label: "Population (millions)",
    tickFormat: d => Math.abs(d) + "M",
    domain: [-40, 40]
  },
  marks: [
    // Bars
    Plot.barX(labeledData, {
      y: "age",
      x: d => -d.male,
      fill: "#3498db",
      tip: true
    }),
    Plot.barX(labeledData, {
      y: "age",
      x: "female",
      fill: "#e74c3c",
      tip: true
    }),

    // Labels on bars
    Plot.text(labeledData, {
      y: "age",
      x: d => -d.male / 2,
      text: d => d.male.toFixed(1) + "M",
      fill: "white",
      fontWeight: "bold"
    }),
    Plot.text(labeledData, {
      y: "age",
      x: d => d.female / 2,
      text: d => d.female.toFixed(1) + "M",
      fill: "white",
      fontWeight: "bold"
    }),

    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Detailed Age Pyramid (Single-Year)

Fine-grained age distribution:

```javascript
const detailedAges = [];
for (let age = 0; age <= 100; age += 5) {
  const factor = Math.exp(-(age - 30) ** 2 / 800);  // Peak around 30
  detailedAges.push({
    age: age + "-" + (age + 4),
    male: -(10 + Math.random() * 5) * factor,
    female: (10 + Math.random() * 5) * factor
  });
}

Plot.plot({
  height: 600,
  marginLeft: 70,
  x: {
    label: "Population (thousands)",
    tickFormat: d => Math.abs(d) + "K"
  },
  y: {label: "Age Group"},
  marks: [
    Plot.barX(detailedAges, {
      y: "age",
      x: "male",
      fill: "#3498db"
    }),
    Plot.barX(detailedAges, {
      y: "age",
      x: "female",
      fill: "#e74c3c"
    }),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Dependency Ratio Visualization

Highlight working-age vs dependent populations:

```javascript
const dependencyData = [
  {age: "0-14", type: "Dependent", male: -20, female: 19},
  {age: "15-64", type: "Working Age", male: -62, female: 60},
  {age: "65+", type: "Dependent", male: -10, female: 13}
];

Plot.plot({
  marginLeft: 70,
  x: {
    label: "Population (%)",
    tickFormat: d => Math.abs(d) + "%"
  },
  color: {
    domain: ["Dependent", "Working Age"],
    range: ["#e74c3c", "#2ecc71"],
    legend: true
  },
  marks: [
    Plot.barX(dependencyData, {
      y: "age",
      x: "male",
      fill: "type",
      tip: true
    }),
    Plot.barX(dependencyData, {
      y: "age",
      x: "female",
      fill: "type",
      tip: true
    }),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Key Patterns

### Basic Structure
```javascript
// Male (negative values)
Plot.barX(data, {
  y: "ageGroup",
  x: d => -d.maleCount,  // or pre-negated in data
  fill: "#3498db"
})

// Female (positive values)
Plot.barX(data, {
  y: "ageGroup",
  x: "femaleCount",
  fill: "#e74c3c"
})

// Center line
Plot.ruleX([0])
```

### Age Ordering
```javascript
// Ensure proper ordering (youngest at bottom)
{
  y: {
    domain: ["0-9", "10-19", "20-29", ...].reverse()
  }
}
```

### Color Conventions
```javascript
// Traditional
{
  male: "#3498db",    // Blue
  female: "#e74c3c"   // Red/Pink
}

// Alternative
{
  male: "#5DA5DA",
  female: "#F15854"
}
```

### Axis Formatting
```javascript
{
  x: {
    label: "Population",
    tickFormat: d => Math.abs(d) + "M",  // Show absolute values
    symmetric: true  // Equal range on both sides
  }
}
```

## Design Guidelines

1. **Age at bottom** - youngest ages at bottom, oldest at top
2. **Equal scales** - same scale on both sides for fair comparison
3. **Clear labels** - show which side is male/female
4. **Appropriate units** - millions, thousands, or percentages
5. **Consistent colors** - use conventional gender colors or clear legend

## Common Variants

- **Standard pyramid** - expanding base (growing population)
- **Column/box** - roughly equal widths (stable population)
- **Inverted pyramid** - narrowing base (aging population)
- **Irregular** - various bulges (baby booms, wars, migration)

## Related Examples
- [diverging-stacked-bars.md](diverging-stacked-bars.md) - Similar diverging pattern
- [bar-chart.md](bar-chart.md) - Standard bar charts

## Reference
- [reference/marks.md](../marks.md) - Bar mark documentation
- [reference/transforms.md](../transforms.md) - Stack transform
