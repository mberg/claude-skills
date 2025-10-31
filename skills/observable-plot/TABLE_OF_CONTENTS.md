# Observable Plot Documentation - Table of Contents

Complete reference for creating data visualizations with Observable Plot.

## Getting Started

- **[SKILL.md](SKILL.md)** - Main skill overview with core concepts and quick start
- **[reference/examples.md](reference/examples.md)** - Basic example and links to all examples

## Examples

Browse complete working examples:

### Basic Visualizations
- **[Scatterplot](reference/examples/scatterplot.md)** - Point-based visualizations with encodings
- **[Bar Chart](reference/examples/bar-chart.md)** - Categorical comparisons with grouping and stacking
- **[Time Series](reference/examples/time-series.md)** - Temporal data with lines, areas, and moving averages

### Statistical Visualizations
- **[Hexbin Heatmap](reference/examples/hexbin-heatmap.md)** - Density visualization with hexagonal binning
- **[Density Contour](reference/examples/density-contour.md)** - Smooth density estimation and contours

### Geographic Visualizations
- **[Choropleth Map](reference/examples/choropleth-map.md)** - Regional data on maps with projections

### Advanced Compositions
- **[Faceted Plot](reference/examples/faceted-plot.md)** - Small multiples for comparing across categories
- **[Interactive Tips](reference/examples/interactive-tips.md)** - Tooltips, crosshairs, and pointer interactions

## Reference Documentation

Comprehensive API reference:

### Core Concepts
- **[Marks](reference/marks.md)** - All 30+ mark types (dot, bar, line, area, geo, etc.)
- **[Transforms](reference/transforms.md)** - Data transformations (bin, group, stack, etc.)
- **[Scales](reference/scales.md)** - Scale types and color schemes

### Specialized Topics
- **[Projections](reference/projections.md)** - Geographic projection types
- **[Faceting](reference/faceting.md)** - Small multiples configuration
- **[Interactions](reference/interactions.md)** - Tooltips, crosshairs, and pointer interactions
- **[Plot Options](reference/plot-options.md)** - Layout, margins, dimensions, and styling
- **[Common Patterns](reference/common-patterns.md)** - Recipes for common tasks

## By Visualization Type

### Categorical Data
- Bar charts → [bar-chart.md](reference/examples/bar-chart.md)
- Grouped bars → [bar-chart.md](reference/examples/bar-chart.md)
- Stacked bars → [bar-chart.md](reference/examples/bar-chart.md)
- Lollipop charts → [common-patterns.md](reference/common-patterns.md)

### Continuous Data
- Scatterplots → [scatterplot.md](reference/examples/scatterplot.md)
- Line charts → [time-series.md](reference/examples/time-series.md)
- Area charts → [time-series.md](reference/examples/time-series.md)
- Regression → [scatterplot.md](reference/examples/scatterplot.md)

### Distributions
- Histograms → [bar-chart.md](reference/examples/bar-chart.md)
- Density plots → [density-contour.md](reference/examples/density-contour.md)
- Box plots → [marks.md](reference/marks.md)
- Beeswarm → [common-patterns.md](reference/common-patterns.md)

### Spatial Data
- Hexbin heatmaps → [hexbin-heatmap.md](reference/examples/hexbin-heatmap.md)
- Density contours → [density-contour.md](reference/examples/density-contour.md)
- Choropleth maps → [choropleth-map.md](reference/examples/choropleth-map.md)
- Point maps → [choropleth-map.md](reference/examples/choropleth-map.md)

### Time Series
- Line charts → [time-series.md](reference/examples/time-series.md)
- Area charts → [time-series.md](reference/examples/time-series.md)
- Stacked areas → [time-series.md](reference/examples/time-series.md)
- Moving averages → [time-series.md](reference/examples/time-series.md)

### Comparisons
- Small multiples → [faceted-plot.md](reference/examples/faceted-plot.md)
- Grouped bars → [bar-chart.md](reference/examples/bar-chart.md)
- Before/after → [common-patterns.md](reference/common-patterns.md)
- Rankings → [common-patterns.md](reference/common-patterns.md)

## By Mark Type

### Point Marks
- **Plot.dot** → [marks.md](reference/marks.md), [scatterplot.md](reference/examples/scatterplot.md)
- **Plot.image** → [marks.md](reference/marks.md)
- **Plot.text** → [marks.md](reference/marks.md), [scatterplot.md](reference/examples/scatterplot.md)

### Rectangular Marks
- **Plot.barY / Plot.barX** → [marks.md](reference/marks.md), [bar-chart.md](reference/examples/bar-chart.md)
- **Plot.cell** → [marks.md](reference/marks.md)
- **Plot.rect** → [marks.md](reference/marks.md)

### Line Marks
- **Plot.line / Plot.lineY / Plot.lineX** → [marks.md](reference/marks.md), [time-series.md](reference/examples/time-series.md)
- **Plot.area / Plot.areaY / Plot.areaX** → [marks.md](reference/marks.md), [time-series.md](reference/examples/time-series.md)

### Reference Marks
- **Plot.ruleY / Plot.ruleX** → [marks.md](reference/marks.md)
- **Plot.tickY / Plot.tickX** → [marks.md](reference/marks.md)
- **Plot.gridY / Plot.gridX** → [marks.md](reference/marks.md)
- **Plot.frame** → [marks.md](reference/marks.md)

### Geographic Marks
- **Plot.geo** → [marks.md](reference/marks.md), [choropleth-map.md](reference/examples/choropleth-map.md)
- **Plot.sphere** → [marks.md](reference/marks.md), [projections.md](reference/projections.md)
- **Plot.graticule** → [marks.md](reference/marks.md)

### Density Marks
- **Plot.density** → [marks.md](reference/marks.md), [density-contour.md](reference/examples/density-contour.md)
- **Plot.contour** → [marks.md](reference/marks.md), [density-contour.md](reference/examples/density-contour.md)
- **Plot.hexgrid** → [marks.md](reference/marks.md), [hexbin-heatmap.md](reference/examples/hexbin-heatmap.md)

### Statistical Marks
- **Plot.boxY / Plot.boxX** → [marks.md](reference/marks.md)
- **Plot.linearRegressionY** → [marks.md](reference/marks.md), [scatterplot.md](reference/examples/scatterplot.md)

### Interaction Marks
- **Plot.tip** → [marks.md](reference/marks.md), [interactive-tips.md](reference/examples/interactive-tips.md)
- **Plot.crosshair** → [marks.md](reference/marks.md), [interactive-tips.md](reference/examples/interactive-tips.md)

## By Transform

### Aggregation
- **Plot.groupX / Plot.groupY / Plot.groupZ** → [transforms.md](reference/transforms.md), [bar-chart.md](reference/examples/bar-chart.md)
- **Plot.binX / Plot.binY** → [transforms.md](reference/transforms.md), [bar-chart.md](reference/examples/bar-chart.md)
- **Plot.hexbin** → [transforms.md](reference/transforms.md), [hexbin-heatmap.md](reference/examples/hexbin-heatmap.md)

### Positioning
- **Plot.stackY / Plot.stackX** → [transforms.md](reference/transforms.md), [bar-chart.md](reference/examples/bar-chart.md)
- **Plot.dodge** → [transforms.md](reference/transforms.md)
- **Plot.shift** → [transforms.md](reference/transforms.md)

### Statistical
- **Plot.normalizeY / Plot.normalizeX** → [transforms.md](reference/transforms.md), [time-series.md](reference/examples/time-series.md)
- **Plot.windowY / Plot.windowX** → [transforms.md](reference/transforms.md), [time-series.md](reference/examples/time-series.md)

### Filtering
- **Plot.filter** → [transforms.md](reference/transforms.md)
- **Plot.select** → [transforms.md](reference/transforms.md)
- **Plot.interval** → [transforms.md](reference/transforms.md)

### Ordering
- **Plot.sort** → [transforms.md](reference/transforms.md)
- **Plot.reverse** → [transforms.md](reference/transforms.md)

## By Use Case

### Exploratory Analysis
- Quick scatterplot → [scatterplot.md](reference/examples/scatterplot.md)
- Histogram → [bar-chart.md](reference/examples/bar-chart.md)
- Density visualization → [density-contour.md](reference/examples/density-contour.md)

### Dashboards
- Small multiples → [faceted-plot.md](reference/examples/faceted-plot.md)
- Multiple series → [time-series.md](reference/examples/time-series.md)
- Interactive tooltips → [interactive-tips.md](reference/examples/interactive-tips.md)

### Presentations
- Clean bar charts → [bar-chart.md](reference/examples/bar-chart.md)
- Annotated plots → [scatterplot.md](reference/examples/scatterplot.md)
- Geographic visualizations → [choropleth-map.md](reference/examples/choropleth-map.md)

### Publications
- Statistical plots → [density-contour.md](reference/examples/density-contour.md)
- Regression analysis → [scatterplot.md](reference/examples/scatterplot.md)
- Comparison plots → [faceted-plot.md](reference/examples/faceted-plot.md)

## Quick Reference

### Common Tasks
- **Aggregate data** → [transforms.md](reference/transforms.md)
- **Stack bars/areas** → [bar-chart.md](reference/examples/bar-chart.md), [time-series.md](reference/examples/time-series.md)
- **Create histogram** → [bar-chart.md](reference/examples/bar-chart.md)
- **Add tooltips** → [interactive-tips.md](reference/examples/interactive-tips.md)
- **Facet by category** → [faceted-plot.md](reference/examples/faceted-plot.md)
- **Choose colors** → [scales.md](reference/scales.md)
- **Format axes** → [plot-options.md](reference/plot-options.md)

### Design Principles
- **Minimize JavaScript** → [common-patterns.md](reference/common-patterns.md)
- **Use transforms** → [transforms.md](reference/transforms.md)
- **Layer marks** → [common-patterns.md](reference/common-patterns.md)
- **Think in channels** → [SKILL.md](SKILL.md)

## External Resources

- **Official Documentation**: https://observablehq.com/plot/
- **Gallery**: https://observablehq.com/@observablehq/plot-gallery
- **API Reference**: https://github.com/observablehq/plot
- **Getting Started**: https://observablehq.com/plot/getting-started
