# Scale Reference

Scales map abstract data values to visual values (position, color, size, etc.). Plot automatically infers appropriate scales from data and mark specifications.

## Scale Types

### Continuous Scales

For quantitative (numeric) data.

**linear** - Linear mapping (default for continuous data)
```javascript
{x: {type: "linear", domain: [0, 100], range: [0, 640]}}
```

**sqrt** - Square root mapping (better for area encodings)
```javascript
{r: {type: "sqrt", range: [2, 20]}}
```

**pow** - Power scale
```javascript
{y: {type: "pow", exponent: 2}}
```

**log** - Logarithmic scale
```javascript
{x: {type: "log", base: 10}}
```

**symlog** - Symmetric log (handles negative values)
```javascript
{y: {type: "symlog"}}
```

### Temporal Scales

For date/time data.

**time** - Local time
```javascript
{x: {type: "time", domain: [new Date("2023-01-01"), new Date("2023-12-31")]}}
```

**utc** - UTC time
```javascript
{x: {type: "utc"}}
```

### Discrete Scales

For categorical data.

**ordinal** - Categorical mapping (default for string data)
```javascript
{color: {type: "ordinal", domain: ["A", "B", "C"]}}
```

**point** - Maps categories to points in continuous range
```javascript
{x: {type: "point", domain: ["Small", "Medium", "Large"]}}
```

**band** - Maps categories to bands (for bar charts)
```javascript
{x: {type: "band", padding: 0.1}}
```

## Scale Options

### Domain and Range

**domain** - Input data extent
```javascript
{y: {domain: [0, 100]}}        // Fixed domain
{y: {domain: undefined}}        // Auto-compute from data (default)
{color: {domain: ["A", "B"]}}  // Categorical domain
```

**range** - Output visual extent
```javascript
{r: {range: [2, 20]}}          // Size range
{color: {range: ["blue", "red"]}}  // Color range
```

**reverse** - Reverse the scale direction
```javascript
{y: {reverse: true}}  // Flip y-axis
```

### Domain Adjustment

**nice** - Extend domain to nice round numbers
```javascript
{y: {nice: true}}     // Rounds domain to nice values
{y: {nice: 10}}       // Rounds to multiples of 10
```

**clamp** - Clamp values outside domain
```javascript
{x: {clamp: true}}    // Values outside domain are clamped
```

**zero** - Include zero in domain
```javascript
{y: {zero: true}}     // Force domain to include 0
```

**percent** - Format as percentage
```javascript
{y: {percent: true}}  // Show as 0% to 100%
```

### Axis Configuration

**label** - Axis label
```javascript
{y: {label: "Revenue ($)"}}
```

**ticks** - Number or interval of ticks
```javascript
{x: {ticks: 10}}              // Approximately 10 ticks
{x: {ticks: "month"}}         // Monthly ticks for time scales
{x: {ticks: [0, 25, 50, 75, 100]}}  // Explicit tick values
```

**tickFormat** - Custom tick formatting
```javascript
{y: {tickFormat: ".2f"}}      // 2 decimal places
{y: {tickFormat: "~s"}}       // SI prefix
{y: {tickFormat: d => `$${d}`}}  // Custom function
```

**tickSize** - Tick mark size
```javascript
{x: {tickSize: 6}}
```

**tickPadding** - Space between ticks and labels
```javascript
{y: {tickPadding: 5}}
```

**axis** - Axis position
```javascript
{x: {axis: "top"}}            // x-axis on top
{y: {axis: "right"}}          // y-axis on right
{x: {axis: null}}             // Hide axis
```

**grid** - Show grid lines
```javascript
{y: {grid: true}}
```

## Color Scales

### Sequential Color Schemes

For continuous data in one direction.

**Single hue**:
- `"blues"`, `"greens"`, `"greys"`, `"oranges"`, `"purples"`, `"reds"`

**Multi-hue**:
- `"turbo"` - Rainbow-like, high contrast
- `"viridis"` - Perceptually uniform, colorblind-safe
- `"magma"`, `"inferno"`, `"plasma"` - Perceptually uniform variants
- `"cividis"` - Colorblind-optimized
- `"warm"`, `"cool"` - Warm/cool color progressions
- `"cubehelix"` - Spiral through color space
- `"bugn"`, `"bupu"`, `"gnbu"`, `"orrd"`, `"pubu"`, `"pubugn"`, `"purd"`, `"rdpu"`, `"ylgn"`, `"ylgnbu"`, `"ylorbr"`, `"ylorrd"` - ColorBrewer schemes

**Example**:
```javascript
{
  color: {
    scheme: "viridis",
    legend: true,
    label: "Temperature"
  }
}
```

### Diverging Color Schemes

For data with a meaningful center point.

- `"brbg"` - Brown-blue-green
- `"prgn"` - Purple-green
- `"piyg"` - Pink-yellow-green
- `"puor"` - Purple-orange
- `"rdbu"` - Red-blue
- `"rdgy"` - Red-grey
- `"rdylbu"` - Red-yellow-blue
- `"rdylgn"` - Red-yellow-green
- `"spectral"` - Rainbow spectrum

**Example**:
```javascript
{
  color: {
    scheme: "rdbu",
    symmetric: true,  // Center at zero
    legend: true
  }
}
```

### Categorical Color Schemes

For discrete categories.

- `"category10"` - 10 distinct colors
- `"accent"`, `"dark2"`, `"paired"`, `"pastel1"`, `"pastel2"`, `"set1"`, `"set2"`, `"set3"` - ColorBrewer categorical
- `"tableau10"` - Tableau's 10-color palette
- `"observable10"` - Observable's default palette

**Example**:
```javascript
{
  color: {
    scheme: "category10",
    legend: true,
    domain: ["Category A", "Category B", "Category C"]
  }
}
```

### Cyclical Color Schemes

For periodic data.

- `"rainbow"` - Full spectrum
- `"sinebow"` - Smooth rainbow

**Example**:
```javascript
{
  color: {
    scheme: "rainbow",
    domain: [0, 360]  // Degrees
  }
}
```

## Color Scale Options

**scheme** - Named color scheme
```javascript
{color: {scheme: "viridis"}}
```

**range** - Custom colors
```javascript
{color: {range: ["#fff", "#000"]}}
{color: {range: ["white", "steelblue", "darkblue"]}}
```

**interpolate** - Color interpolation method
```javascript
{color: {interpolate: "hsl"}}  // HSL interpolation
{color: {interpolate: "lab"}}  // Lab interpolation
```

**legend** - Show color legend
```javascript
{color: {legend: true}}
{color: {legend: {width: 320}}}  // Custom legend width
```

**symmetric** - Center diverging scale at zero
```javascript
{color: {symmetric: true}}
```

**reverse** - Reverse color scheme
```javascript
{color: {scheme: "viridis", reverse: true}}
```

## Size Scales

**Radius (r)**:
```javascript
{
  r: {
    type: "sqrt",      // Square root (default for area)
    range: [2, 20],    // Min/max radius
    domain: [0, 100]   // Data extent
  }
}
```

**Opacity**:
```javascript
{
  opacity: {
    range: [0.1, 1],
    domain: [0, 100]
  }
}
```

**Stroke Width**:
```javascript
{
  strokeWidth: {
    range: [1, 5],
    domain: [0, 100]
  }
}
```

## Common Scale Configurations

### Logarithmic Axis
```javascript
Plot.plot({
  x: {type: "log"},
  y: {type: "log"},
  marks: [...]
})
```

### Custom Domain
```javascript
Plot.plot({
  y: {domain: [0, 100], zero: true},
  marks: [...]
})
```

### Reversed Y-Axis
```javascript
Plot.plot({
  y: {reverse: true},
  marks: [...]
})
```

### Time Axis with Custom Ticks
```javascript
Plot.plot({
  x: {
    type: "utc",
    ticks: "month",
    tickFormat: "%b %Y"
  },
  marks: [...]
})
```

### Diverging Color Scale
```javascript
Plot.plot({
  color: {
    scheme: "rdbu",
    symmetric: true,
    legend: true,
    label: "Change (%)"
  },
  marks: [...]
})
```

### Ordinal Color with Custom Domain
```javascript
Plot.plot({
  color: {
    domain: ["Small", "Medium", "Large"],
    range: ["#fee", "#f88", "#f00"]
  },
  marks: [...]
})
```

## Scale Inference

Plot automatically infers appropriate scales:

- **Numbers** → `linear` scale
- **Dates** → `utc` or `time` scale
- **Strings** → `ordinal` scale
- **Color channel** → Color scheme
- **Radius channel** → `sqrt` scale (for proper area encoding)

Override with explicit `type`:
```javascript
{x: {type: "log"}}  // Force logarithmic instead of linear
```

## Multiple Scales

Different marks can use different scales via `color`, `r`, `opacity`, etc.:

```javascript
Plot.plot({
  color: {scheme: "viridis"},
  r: {range: [2, 20]},
  marks: [
    Plot.dot(data, {x: "x", y: "y", fill: "temperature", r: "population"})
  ]
})
```

## Related Documentation
- [marks.md](marks.md) - Marks that use scales
- [plot-options.md](plot-options.md) - Plot-level configuration
