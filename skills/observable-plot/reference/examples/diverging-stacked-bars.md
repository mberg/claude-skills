# Diverging Stacked Bar Examples

Diverging stacked bars display data that diverges from a center baseline, commonly used for Likert scale surveys (agree/disagree), sentiment analysis, or any data with opposing categories.

## Basic Diverging Stacked Bar

Survey responses centered at zero:

```javascript
import * as Plot from "@observablehq/plot";

const surveyData = [
  {question: "Q1", response: "Strongly Disagree", value: -20},
  {question: "Q1", response: "Disagree", value: -15},
  {question: "Q1", response: "Neutral", value: 0},
  {question: "Q1", response: "Agree", value: 25},
  {question: "Q1", response: "Strongly Agree", value: 30},
  {question: "Q2", response: "Strongly Disagree", value: -10},
  {question: "Q2", response: "Disagree", value: -20},
  {question: "Q2", response: "Neutral", value: 0},
  {question: "Q2", response: "Agree", value: 35},
  {question: "Q2", response: "Strongly Agree", value: 25}
];

Plot.plot({
  x: {
    label: "Percentage",
    tickFormat: d => Math.abs(d) + "%"
  },
  color: {
    domain: ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
    range: ["#ca0020", "#f4a582", "#f7f7f7", "#92c5de", "#0571b0"],
    legend: true
  },
  marks: [
    // Negative side (disagree)
    Plot.barX(
      surveyData.filter(d => d.value < 0),
      Plot.stackX({
        y: "question",
        x: "value",
        fill: "response",
        tip: true
      })
    ),

    // Positive side (agree)
    Plot.barX(
      surveyData.filter(d => d.value > 0),
      Plot.stackX({
        y: "question",
        x: "value",
        fill: "response",
        tip: true
      })
    ),

    // Center line
    Plot.ruleX([0], {stroke: "black", strokeWidth: 2})
  ]
}).display();
```

## Likert Scale (5-Point)

Classic Likert survey visualization:

```javascript
const likertData = [
  {item: "Service Quality", category: "Very Poor", count: 5},
  {item: "Service Quality", category: "Poor", count: 12},
  {item: "Service Quality", category: "Neutral", count: 20},
  {item: "Service Quality", category: "Good", count: 45},
  {item: "Service Quality", category: "Excellent", count: 18},
  {item: "Value for Money", category: "Very Poor", count: 8},
  {item: "Value for Money", category: "Poor", count: 15},
  {item: "Value for Money", category: "Neutral", count: 25},
  {item: "Value for Money", category: "Good", count: 35},
  {item: "Value for Money", category: "Excellent", count: 17}
];

// Convert to percentages centered at zero
const total = d3.rollup(likertData, v => d3.sum(v, d => d.count), d => d.item);

const centered = likertData.map(d => {
  const itemTotal = total.get(d.item);
  const pct = (d.count / itemTotal) * 100;

  // Make negative categories negative
  const value = ["Very Poor", "Poor"].includes(d.category) ? -pct : pct;

  return {...d, value, percent: pct};
});

Plot.plot({
  marginLeft: 120,
  x: {
    label: "← Negative    Positive →",
    tickFormat: d => Math.abs(d) + "%",
    domain: [-60, 60]
  },
  color: {
    domain: ["Very Poor", "Poor", "Neutral", "Good", "Excellent"],
    range: ["#d7191c", "#fdae61", "#ffffbf", "#abd9e9", "#2c7bb6"]
  },
  marks: [
    Plot.barX(centered, Plot.stackX({
      y: "item",
      x: "value",
      fill: "category",
      inset: 0.5,
      tip: true,
      channels: {
        Category: "category",
        Count: "count",
        Percent: d => `${d.percent.toFixed(1)}%`
      }
    })),
    Plot.ruleX([0], {stroke: "black", strokeWidth: 1.5})
  ]
}).display();
```

## Sentiment Analysis

Positive/negative sentiment with neutral:

```javascript
const sentimentData = [
  {topic: "Product Features", sentiment: "Negative", value: -25},
  {topic: "Product Features", sentiment: "Neutral", value: 0},
  {topic: "Product Features", sentiment: "Positive", value: 75},
  {topic: "Customer Support", sentiment: "Negative", value: -15},
  {topic: "Customer Support", sentiment: "Neutral", value: 0},
  {topic: "Customer Support", sentiment: "Positive", value: 85},
  {topic: "Pricing", sentiment: "Negative", value: -40},
  {topic: "Pricing", sentiment: "Neutral", value: 0},
  {topic: "Pricing", sentiment: "Positive", value: 60}
];

Plot.plot({
  marginLeft: 130,
  x: {
    label: "Sentiment Distribution (%)",
    tickFormat: d => Math.abs(d) + "%"
  },
  color: {
    domain: ["Negative", "Neutral", "Positive"],
    range: ["#d73027", "#f7f7f7", "#1a9850"],
    legend: true
  },
  marks: [
    Plot.barX(sentimentData, Plot.stackX({
      y: "topic",
      x: "value",
      fill: "sentiment",
      tip: true
    })),
    Plot.ruleX([0], {stroke: "black", strokeWidth: 2})
  ]
}).display();
```

## Year-over-Year Change

Show increases and decreases from baseline:

```javascript
const changeData = [
  {region: "North", category: "Large Decrease", value: -15},
  {region: "North", category: "Small Decrease", value: -10},
  {region: "North", category: "No Change", value: 0},
  {region: "North", category: "Small Increase", value: 20},
  {region: "North", category: "Large Increase", value: 35},
  {region: "South", category: "Large Decrease", value: -8},
  {region: "South", category: "Small Decrease", value: -12},
  {region: "South", category: "No Change", value: 0},
  {region: "South", category: "Small Increase", value: 30},
  {region: "South", category: "Large Increase", value: 40}
];

Plot.plot({
  x: {
    label: "Change from Previous Year (%)",
    tickFormat: d => (d > 0 ? "+" : "") + d + "%"
  },
  color: {
    domain: ["Large Decrease", "Small Decrease", "No Change", "Small Increase", "Large Increase"],
    range: ["#b2182b", "#ef8a62", "#f7f7f7", "#67a9cf", "#2166ac"],
    legend: true
  },
  marks: [
    Plot.barX(changeData, Plot.stackX({
      y: "region",
      x: "value",
      fill: "category",
      tip: true
    })),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Vertical Diverging Stacked Bars

Useful for timeline comparisons:

```javascript
const timelineData = [
  {year: "2020", category: "Strong Negative", value: -30},
  {year: "2020", category: "Weak Negative", value: -20},
  {year: "2020", category: "Neutral", value: 0},
  {year: "2020", category: "Weak Positive", value: 25},
  {year: "2020", category: "Strong Positive", value: 25},
  {year: "2021", category: "Strong Negative", value: -20},
  {year: "2021", category: "Weak Negative", value: -15},
  {year: "2021", category: "Neutral", value: 0},
  {year: "2021", category: "Weak Positive", value: 30},
  {year: "2021", category: "Strong Positive", value: 35}
];

Plot.plot({
  y: {
    label: "Percentage",
    tickFormat: d => Math.abs(d) + "%",
    grid: true
  },
  color: {
    domain: ["Strong Negative", "Weak Negative", "Neutral", "Weak Positive", "Strong Positive"],
    range: ["#d7191c", "#fdae61", "#ffffbf", "#a6d96a", "#1a9641"],
    legend: true
  },
  marks: [
    Plot.barY(timelineData, Plot.stackY({
      x: "year",
      y: "value",
      fill: "category",
      tip: true
    })),
    Plot.ruleY([0], {stroke: "black", strokeWidth: 2})
  ]
}).display();
```

## Net Promoter Score (NPS)

Detractors vs Promoters:

```javascript
const npsData = [
  {segment: "Q1", category: "Detractors (0-6)", value: -25},
  {segment: "Q1", category: "Passives (7-8)", value: 0},
  {segment: "Q1", category: "Promoters (9-10)", value: 50},
  {segment: "Q2", category: "Detractors (0-6)", value: -20},
  {segment: "Q2", category: "Passives (7-8)", value: 0},
  {segment: "Q2", category: "Promoters (9-10)", value: 55},
  {segment: "Q3", category: "Detractors (0-6)", value: -15},
  {segment: "Q3", category: "Passives (7-8)", value: 0},
  {segment: "Q3", category: "Promoters (9-10)", value: 60}
];

Plot.plot({
  x: {
    label: "Net Promoter Score (%)",
    tickFormat: d => (d > 0 ? "+" : "") + d,
    domain: [-40, 80]
  },
  color: {
    domain: ["Detractors (0-6)", "Passives (7-8)", "Promoters (9-10)"],
    range: ["#d73027", "#fee08b", "#1a9850"]
  },
  marks: [
    Plot.barX(npsData, Plot.stackX({
      y: "segment",
      x: "value",
      fill: "category",
      tip: true
    })),
    Plot.ruleX([0], {stroke: "black", strokeWidth: 2}),

    // NPS score labels
    Plot.text(
      d3.rollup(npsData, v => d3.sum(v, d => d.value), d => d.segment),
      {
        x: ([segment, nps]) => nps,
        y: ([segment]) => segment,
        text: ([segment, nps]) => `NPS: ${nps > 0 ? '+' : ''}${nps}`,
        dx: nps => nps > 0 ? 10 : -10,
        textAnchor: nps => nps > 0 ? "start" : "end",
        fontWeight: "bold"
      }
    )
  ],
  color: {legend: true}
}).display();
```

## Normalized Diverging Stack

Show proportions instead of absolute values:

```javascript
const proportionData = [
  {category: "Product A", type: "Against", count: 30},
  {category: "Product A", type: "Neutral", count: 20},
  {category: "Product A", type: "For", count: 50},
  {category: "Product B", type: "Against", count: 15},
  {category: "Product B", type: "Neutral", count: 25},
  {category: "Product B", type: "For", count: 60}
];

// Convert to centered percentages
const totals = d3.rollup(proportionData, v => d3.sum(v, d => d.count), d => d.category);

const normalized = proportionData.map(d => {
  const total = totals.get(d.category);
  const pct = (d.count / total) * 100;
  const value = d.type === "Against" ? -pct : pct;
  return {...d, value, pct};
});

Plot.plot({
  x: {
    label: "Distribution (%)",
    tickFormat: d => Math.abs(d) + "%",
    domain: [-60, 80]
  },
  color: {
    domain: ["Against", "Neutral", "For"],
    range: ["#e66101", "#f7f7f7", "#5e3c99"],
    legend: true
  },
  marks: [
    Plot.barX(normalized, Plot.stackX({
      y: "category",
      x: "value",
      fill: "type",
      tip: true,
      channels: {
        Type: "type",
        Count: "count",
        Percent: d => `${d.pct.toFixed(1)}%`
      }
    })),
    Plot.ruleX([0], {stroke: "black"})
  ]
}).display();
```

## Key Patterns

### Basic Structure
```javascript
// Negative values
Plot.barX(
  data.filter(d => d.value < 0),
  Plot.stackX({y: "category", x: "value", fill: "type"})
)

// Positive values
Plot.barX(
  data.filter(d => d.value > 0),
  Plot.stackX({y: "category", x: "value", fill: "type"})
)

// Center baseline
Plot.ruleX([0])
```

### Color Schemes
```javascript
// Diverging (recommended)
{
  color: {
    domain: ["Negative", "Neutral", "Positive"],
    range: ["#d73027", "#f7f7f7", "#1a9850"]
  }
}

// ColorBrewer diverging schemes
range: ["#ca0020", "#f4a582", "#f7f7f7", "#92c5de", "#0571b0"]  // RdBu
range: ["#d7191c", "#fdae61", "#ffffbf", "#a6d96a", "#1a9641"]  // RdYlGn
```

### Axis Formatting
```javascript
// Show absolute values
{x: {tickFormat: d => Math.abs(d) + "%"}}

// Show +/- signs
{x: {tickFormat: d => (d > 0 ? "+" : "") + d}}

// Custom labels
{x: {label: "← Disagree    Agree →"}}
```

### Data Preparation
```javascript
// Convert counts to percentages
const total = d3.sum(data, d => d.count);
const pct = data.map(d => ({
  ...d,
  value: (d.count / total) * 100
}));

// Make negative categories negative
const centered = data.map(d => ({
  ...d,
  value: d.category.includes("Negative") ? -d.value : d.value
}));
```

## Common Use Cases

- **Likert scale surveys** (strongly disagree to strongly agree)
- **Sentiment analysis** (negative/neutral/positive)
- **NPS scores** (detractors/passives/promoters)
- **Before/after comparisons** (decrease/no change/increase)
- **Political polling** (oppose/neutral/support)
- **Performance reviews** (below/meets/exceeds)

## Related Examples
- [bar-chart.md](bar-chart.md) - Standard stacked bars
- [population-pyramid.md](population-pyramid.md) - Age/gender diverging bars

## Reference
- [reference/transforms.md](../transforms.md) - Stack transform
- [reference/scales.md](../scales.md) - Diverging color schemes
