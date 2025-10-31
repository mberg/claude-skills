# Interaction Reference

Observable Plot provides declarative interactivity through tips (tooltips), crosshairs, and pointer transforms. No external JavaScript required.

## Tooltips (tip option)

### Basic Tooltip

Add `tip: true` to any mark:

```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  tip: true  // Shows all encoded channels
})
```

### Custom Tooltip Content

Use `channels` to specify what appears in tooltips:

```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  fill: "category",
  tip: true,
  channels: {
    Name: "name",
    Value: "value",
    Category: "category",
    Computed: d => d.x + d.y
  }
})
```

### Tooltip Formatting

Format values in tooltips:

```javascript
Plot.dot(data, {
  x: "x",
  y: "revenue",
  tip: {
    format: {
      x: ".2f",         // 2 decimal places
      y: "$,.0f"        // Currency format
    }
  },
  channels: {
    Revenue: d => `$${d.revenue.toLocaleString()}`,
    Growth: d => `${(d.growth * 100).toFixed(1)}%`
  }
})
```

### Tooltip Options

```javascript
{
  tip: {
    format: {
      x: ".2f",        // Format x values
      y: "~s"          // SI prefix for y
    },
    anchor: "top",     // Tooltip position
    fontSize: 12,      // Custom font size
    lineWidth: 20      // Text wrapping width
  }
}
```

## Crosshair

### Basic Crosshair

Add crosshair lines that track the pointer:

```javascript
Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "date",
      y: "value"
    }),
    Plot.crosshair(data, {
      x: "date",
      y: "value"
    })
  ]
})
```

### Crosshair with Tooltip

Combine crosshair and tooltip:

```javascript
Plot.plot({
  marks: [
    Plot.lineY(data, {x: "date", y: "value"}),
    Plot.crosshair(data, {
      x: "date",
      y: "value",
      tip: true  // Add tooltip to crosshair
    })
  ]
})
```

### Crosshair Options

```javascript
Plot.crosshair(data, {
  x: "x",
  y: "y",
  color: "red",              // Crosshair color
  opacity: 0.5,              // Crosshair opacity
  ruleStroke: "blue",        // Rule line color
  ruleStrokeWidth: 2         // Rule line width
})
```

## Pointer Transform

### Nearest Point Highlight

Highlight the point nearest to the pointer:

```javascript
Plot.plot({
  marks: [
    // All points (faint)
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "lightgray",
      r: 3
    }),

    // Nearest point (highlighted)
    Plot.dot(data, Plot.pointer({
      x: "x",
      y: "y",
      fill: "red",
      r: 8,
      tip: true
    }))
  ]
})
```

### Pointer with Lines

Highlight nearest point on a line chart:

```javascript
Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "steelblue"
    }),
    Plot.dot(data, Plot.pointer({
      x: "date",
      y: "value",
      fill: "red",
      r: 5,
      tip: true
    }))
  ]
})
```

### Pointer Options

```javascript
Plot.pointer({
  x: "x",
  y: "y",
  px: "x",  // Pointer distance metric (default: x)
  py: "y",  // Pointer distance metric (default: y)
  maxRadius: Infinity  // Maximum distance to match
})
```

## Multiple Series Interaction

### Tips on Multiple Series

```javascript
Plot.plot({
  color: {legend: true},
  marks: [
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "series",
      tip: true  // Tooltip on each series
    })
  ]
})
```

### Crosshair Across Series

```javascript
Plot.plot({
  marks: [
    Plot.lineY(data, {
      x: "date",
      y: "value",
      z: "series",
      stroke: "series"
    }),
    Plot.crosshairX(data, {
      x: "date",
      y: "value"
    })
  ]
})
```

## Directional Crosshairs

### Horizontal Crosshair Only

```javascript
Plot.crosshairY(data, {
  x: "x",
  y: "y"
})
```

### Vertical Crosshair Only

```javascript
Plot.crosshairX(data, {
  x: "date",
  y: "value"
})
```

## Voronoi Interaction

Improved hit-testing for sparse data:

```javascript
Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "category"
    }),
    Plot.dot(data, Plot.pointer(Plot.voronoi({
      x: "x",
      y: "y",
      fill: "red",
      r: 8,
      tip: true
    })))
  ]
})
```

## Geographic Interaction

### Map Tooltips

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {
      fill: "value",
      stroke: "white",
      tip: true,
      channels: {
        State: d => d.properties.name,
        Value: d => d.properties.value,
        Formatted: d => `${d.properties.value.toFixed(1)}%`
      }
    })
  ]
})
```

### City Points with Tips

```javascript
Plot.plot({
  projection: "albers-usa",
  marks: [
    Plot.geo(states, {fill: "lightgray"}),
    Plot.dot(cities, {
      x: "longitude",
      y: "latitude",
      r: "population",
      fill: "red",
      tip: true,
      channels: {
        City: "name",
        Population: d => `${(d.population / 1000000).toFixed(1)}M`,
        State: "state"
      }
    })
  ]
})
```

## Interaction Patterns

### Hover Effects

Tooltips automatically appear on hover:

```javascript
Plot.barY(data, {
  x: "category",
  y: "value",
  fill: "steelblue",
  tip: true
})
```

### Focus on Specific Data

Highlight data points meeting criteria:

```javascript
Plot.plot({
  marks: [
    // All data (faint)
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "lightgray",
      r: 3
    }),

    // Highlighted subset with tips
    Plot.dot(data.filter(d => d.important), {
      x: "x",
      y: "y",
      fill: "red",
      r: 6,
      tip: true,
      channels: {
        Value: "value",
        Note: "note"
      }
    })
  ]
})
```

### Combined Interactions

Layer multiple interaction types:

```javascript
Plot.plot({
  marks: [
    // Base line
    Plot.lineY(data, {
      x: "date",
      y: "value",
      stroke: "steelblue",
      strokeWidth: 2
    }),

    // Crosshair
    Plot.crosshair(data, {
      x: "date",
      y: "value"
    }),

    // Nearest point highlight
    Plot.dot(data, Plot.pointer({
      x: "date",
      y: "value",
      fill: "red",
      r: 6,
      tip: true,
      channels: {
        Date: "date",
        Value: "value",
        Change: d => d.value - d.previousValue
      }
    }))
  ]
})
```

## Accessibility

### Accessible Tooltips

Ensure tooltips are keyboard-accessible and screen-reader friendly:

```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  tip: true,
  ariaLabel: d => `${d.name}: ${d.value}`,
  channels: {
    Name: "name",
    Value: "value",
    Description: "description"
  }
})
```

### Alternative Text

Provide text alternatives:

```javascript
Plot.plot({
  ariaLabel: "Scatter plot showing correlation between age and income",
  marks: [
    Plot.dot(data, {
      x: "age",
      y: "income",
      tip: true
    })
  ]
})
```

## Performance Considerations

### Large Datasets

For datasets with >1000 points, consider:

1. **Aggregation**: Use hexbin or density instead of individual points
2. **Sampling**: Show subset with full data in tooltip
3. **Voronoi**: Improve hit-testing performance

```javascript
// Aggregated view with detailed tooltips
Plot.plot({
  marks: [
    // Hexbin for overview
    Plot.dot(data, Plot.hexbin(
      {fill: "count"},
      {x: "x", y: "y", binWidth: 10}
    )),

    // Invisible points for detailed tooltips
    Plot.dot(data, Plot.pointer({
      x: "x",
      y: "y",
      r: 0,  // Invisible
      tip: true,
      channels: {
        X: "x",
        Y: "y",
        Details: "details"
      }
    }))
  ]
})
```

## Custom Tooltip Content

### Rich Formatting

Use channels for custom formatting:

```javascript
Plot.dot(data, {
  x: "date",
  y: "value",
  tip: true,
  channels: {
    Date: d => d.date.toLocaleDateString(),
    Value: d => `$${d.value.toLocaleString()}`,
    "% Change": d => `${(d.change * 100).toFixed(1)}%`,
    Status: d => d.value > d.target ? "✓ Above target" : "✗ Below target"
  }
})
```

### Multi-line Content

```javascript
Plot.dot(data, {
  x: "x",
  y: "y",
  tip: true,
  title: d => `${d.name}\n${d.category}\nValue: ${d.value}`
})
```

## Related Documentation
- [examples/interactive-tips.md](examples/interactive-tips.md) - Interactive examples
- [marks.md](marks.md) - Marks that support interactivity
