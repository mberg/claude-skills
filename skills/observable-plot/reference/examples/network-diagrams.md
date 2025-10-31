# Network and Hierarchical Diagram Examples

Network diagrams visualize relationships between entities using arrows, links, and tree layouts. Observable Plot provides declarative marks for creating these visualizations.

## Arc Diagram

Visualize network connections as arcs:

```javascript
import * as Plot from "@observablehq/plot";

const links = [
  {source: "A", target: "B"},
  {source: "A", target: "C"},
  {source: "B", target: "D"},
  {source: "C", target: "D"},
  {source: "D", target: "E"}
];

// Create node positions
const nodes = ["A", "B", "C", "D", "E"];
const nodeMap = new Map(nodes.map((d, i) => [d, i]));

Plot.plot({
  marginTop: 60,
  marks: [
    // Arcs connecting nodes
    Plot.link(links, {
      x1: d => nodeMap.get(d.source),
      x2: d => nodeMap.get(d.target),
      y1: 0,
      y2: 0,
      curve: "arc",
      stroke: "steelblue",
      strokeWidth: 2
    }),

    // Node dots
    Plot.dot(nodes, {
      x: (d, i) => i,
      y: 0,
      r: 8,
      fill: "red",
      stroke: "white",
      strokeWidth: 2
    }),

    // Node labels
    Plot.text(nodes, {
      x: (d, i) => i,
      y: 0,
      text: d => d,
      dy: -15,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Link Diagram

Direct node-to-node connections:

```javascript
const nodes = [
  {id: "A", x: 50, y: 50},
  {id: "B", x: 150, y: 30},
  {id: "C", x: 150, y: 70},
  {id: "D", x: 250, y: 50}
];

const links = [
  {source: "A", target: "B", weight: 3},
  {source: "A", target: "C", weight: 1},
  {source: "B", target: "D", weight: 2},
  {source: "C", target: "D", weight: 4}
];

const nodeMap = new Map(nodes.map(d => [d.id, d]));

Plot.plot({
  marks: [
    // Links with varying thickness
    Plot.link(links, {
      x1: d => nodeMap.get(d.source).x,
      y1: d => nodeMap.get(d.source).y,
      x2: d => nodeMap.get(d.target).x,
      y2: d => nodeMap.get(d.target).y,
      stroke: "lightgray",
      strokeWidth: d => d.weight,
      tip: true
    }),

    // Nodes
    Plot.dot(nodes, {
      x: "x",
      y: "y",
      r: 10,
      fill: "steelblue",
      stroke: "white",
      strokeWidth: 2
    }),

    // Labels
    Plot.text(nodes, {
      x: "x",
      y: "y",
      text: "id",
      fill: "white",
      fontWeight: "bold"
    })
  ]
}).display();
```

## Arrow Diagram

Show directionality with arrows:

```javascript
const transitions = [
  {from: "Start", to: "Processing", x1: 50, y1: 50, x2: 150, y2: 50},
  {from: "Processing", to: "Complete", x1: 150, y1: 50, x2: 250, y2: 50},
  {from: "Processing", to: "Error", x1: 150, y1: 50, x2: 150, y2: 150}
];

Plot.plot({
  marks: [
    // Arrows
    Plot.arrow(transitions, {
      x1: "x1",
      y1: "y1",
      x2: "x2",
      y2: "y2",
      stroke: "steelblue",
      strokeWidth: 2,
      headLength: 12,
      tip: true,
      channels: {
        From: "from",
        To: "to"
      }
    }),

    // State nodes
    Plot.rect([
      {x: 50, y: 50, label: "Start"},
      {x: 150, y: 50, label: "Processing"},
      {x: 250, y: 50, label: "Complete"},
      {x: 150, y: 150, label: "Error"}
    ], {
      x: "x",
      y: "y",
      width: 60,
      height: 30,
      fill: "lightblue",
      stroke: "steelblue"
    }),

    // Labels
    Plot.text([
      {x: 50, y: 50, label: "Start"},
      {x: 150, y: 50, label: "Processing"},
      {x: 250, y: 50, label: "Complete"},
      {x: 150, y: 150, label: "Error"}
    ], {
      x: "x",
      y: "y",
      text: "label",
      fontSize: 10
    })
  ]
}).display();
```

## Difference Arrows (Change Visualization)

Show changes between two points:

```javascript
const data = [
  {category: "Product A", before: 100, after: 150},
  {category: "Product B", before: 120, after: 90},
  {category: "Product C", before: 80, after: 130},
  {category: "Product D", before: 140, after: 145}
];

Plot.plot({
  marginLeft: 100,
  marks: [
    Plot.ruleX([0]),

    // Arrows showing change
    Plot.arrow(data, {
      x1: "before",
      x2: "after",
      y: "category",
      stroke: d => d.after > d.before ? "green" : "red",
      strokeWidth: 2,
      headLength: 8,
      tip: true,
      channels: {
        Category: "category",
        Before: "before",
        After: "after",
        Change: d => d.after - d.before
      }
    }),

    // Starting points
    Plot.dot(data, {
      x: "before",
      y: "category",
      fill: "lightgray",
      r: 4
    }),

    // Ending points
    Plot.dot(data, {
      x: "after",
      y: "category",
      fill: d => d.after > d.before ? "green" : "red",
      r: 5
    })
  ]
}).display();
```

## Tree Diagram (Hierarchical)

Visualize hierarchical data:

```javascript
// Hierarchical data
const hierarchy = {
  name: "Root",
  children: [
    {
      name: "Branch A",
      children: [
        {name: "Leaf A1"},
        {name: "Leaf A2"}
      ]
    },
    {
      name: "Branch B",
      children: [
        {name: "Leaf B1"},
        {name: "Leaf B2"},
        {name: "Leaf B3"}
      ]
    }
  ]
};

// Convert to Plot-compatible tree
const root = d3.hierarchy(hierarchy);
const tree = d3.tree().size([640, 400])(root);

Plot.plot({
  marks: [
    // Links between nodes
    Plot.link(root.links(), {
      x1: d => d.source.x,
      y1: d => d.source.y,
      x2: d => d.target.x,
      y2: d => d.target.y,
      stroke: "lightgray",
      strokeWidth: 2
    }),

    // Nodes
    Plot.dot(root.descendants(), {
      x: d => d.x,
      y: d => d.y,
      r: 5,
      fill: "steelblue",
      stroke: "white",
      strokeWidth: 2
    }),

    // Labels
    Plot.text(root.descendants(), {
      x: d => d.x,
      y: d => d.y,
      text: d => d.data.name,
      dy: -10,
      fontSize: 10
    })
  ]
}).display();
```

## Chord/Circular Network

Circular layout for network visualization:

```javascript
const nodes = ["A", "B", "C", "D", "E"];
const n = nodes.length;

const links = [
  {source: 0, target: 1, value: 3},
  {source: 0, target: 2, value: 1},
  {source: 1, target: 3, value: 2},
  {source: 2, target: 4, value: 4},
  {source: 3, target: 4, value: 2}
];

// Position nodes in circle
const radius = 150;
const nodePositions = nodes.map((name, i) => {
  const angle = (i / n) * 2 * Math.PI - Math.PI / 2;
  return {
    name,
    x: 200 + radius * Math.cos(angle),
    y: 200 + radius * Math.sin(angle)
  };
});

Plot.plot({
  width: 400,
  height: 400,
  marks: [
    // Curved links
    Plot.link(links, {
      x1: d => nodePositions[d.source].x,
      y1: d => nodePositions[d.source].y,
      x2: d => nodePositions[d.target].x,
      y2: d => nodePositions[d.target].y,
      stroke: "steelblue",
      strokeOpacity: 0.3,
      strokeWidth: d => d.value,
      curve: "bundle"
    }),

    // Nodes
    Plot.dot(nodePositions, {
      x: "x",
      y: "y",
      r: 8,
      fill: "red",
      stroke: "white",
      strokeWidth: 2
    }),

    // Labels
    Plot.text(nodePositions, {
      x: "x",
      y: "y",
      text: "name",
      dy: -15,
      fontWeight: "bold"
    })
  ]
}).display();
```

## Sankey/Alluvial-Style Flow

Flow between categories:

```javascript
const flows = [
  {source: "A", target: "X", value: 30},
  {source: "A", target: "Y", value: 20},
  {source: "B", target: "X", value: 10},
  {source: "B", target: "Y", value: 40},
  {source: "B", target: "Z", value: 15}
];

// Simple vertical flow layout
const sourceY = new Map([["A", 50], ["B", 150]]);
const targetY = new Map([["X", 40], ["Y", 100], ["Z", 160]]);

Plot.plot({
  marks: [
    // Flow ribbons
    Plot.link(flows, {
      x1: 100,
      x2: 300,
      y1: d => sourceY.get(d.source),
      y2: d => targetY.get(d.target),
      stroke: "steelblue",
      strokeOpacity: 0.5,
      strokeWidth: d => d.value / 2,
      curve: "bundle",
      tip: true
    }),

    // Source nodes
    Plot.dot([...sourceY.keys()], {
      x: 100,
      y: d => sourceY.get(d),
      r: 10,
      fill: "red"
    }),

    // Target nodes
    Plot.dot([...targetY.keys()], {
      x: 300,
      y: d => targetY.get(d),
      r: 10,
      fill: "green"
    }),

    // Labels
    Plot.text([...sourceY.keys()], {
      x: 100,
      y: d => sourceY.get(d),
      text: d => d,
      dx: -20
    }),
    Plot.text([...targetY.keys()], {
      x: 300,
      y: d => targetY.get(d),
      text: d => d,
      dx: 20
    })
  ]
}).display();
```

## Force-Directed Network (Simulated Positions)

Using pre-computed force layout positions:

```javascript
// Assume positions computed from d3-force simulation
const nodes = [
  {id: 1, name: "Node 1", x: 100, y: 100, group: 1},
  {id: 2, name: "Node 2", x: 200, y: 150, group: 1},
  {id: 3, name: "Node 3", x: 300, y: 100, group: 2},
  {id: 4, name: "Node 4", x: 250, y: 250, group: 2},
  {id: 5, name: "Node 5", x: 150, y: 200, group: 1}
];

const links = [
  {source: 1, target: 2},
  {source: 1, target: 5},
  {source: 2, target: 3},
  {source: 3, target: 4},
  {source: 4, target: 5}
];

const nodeMap = new Map(nodes.map(d => [d.id, d]));

Plot.plot({
  color: {legend: true},
  marks: [
    // Edges
    Plot.link(links, {
      x1: d => nodeMap.get(d.source).x,
      y1: d => nodeMap.get(d.source).y,
      x2: d => nodeMap.get(d.target).x,
      y2: d => nodeMap.get(d.target).y,
      stroke: "#999",
      strokeWidth: 1
    }),

    // Nodes
    Plot.dot(nodes, {
      x: "x",
      y: "y",
      r: 8,
      fill: "group",
      stroke: "white",
      strokeWidth: 2,
      tip: true,
      channels: {Name: "name", Group: "group"}
    })
  ]
}).display();
```

## Key Patterns

### Arrow Mark
```javascript
Plot.arrow(data, {
  x1: "startX",
  y1: "startY",
  x2: "endX",
  y2: "endY",
  stroke: "color",
  headLength: 12,    // Arrow head size
  headAngle: 60,     // Arrow head angle
  inset: 10          // Shorten arrow ends
})
```

### Link Mark
```javascript
Plot.link(data, {
  x1: "sourceX",
  y1: "sourceY",
  x2: "targetX",
  y2: "targetY",
  stroke: "color",
  strokeWidth: "weight",
  curve: "arc"       // or "bundle", "linear"
})
```

### Curve Options
- `"linear"`: Straight lines (default)
- `"arc"`: Circular arcs (for arc diagrams)
- `"bundle"`: Curved paths (for hierarchies)

### Common Node Positioning
```javascript
// Linear (arc diagram)
const x = (d, i) => i * spacing;

// Circular
const angle = i => (i / n) * 2 * Math.PI;
const x = i => centerX + radius * Math.cos(angle(i));
const y = i => centerY + radius * Math.sin(angle(i));

// Grid
const x = i => (i % cols) * spacing;
const y = i => Math.floor(i / cols) * spacing;

// Tree (use d3.hierarchy + d3.tree)
```

### Network Data Structures

**Edge list**:
```javascript
[{source: "A", target: "B"}, ...]
```

**Adjacency with positions**:
```javascript
nodes: [{id: "A", x: 10, y: 20}, ...]
links: [{source: "A", target: "B"}, ...]
```

**Hierarchical**:
```javascript
{name: "root", children: [{name: "child"}, ...]}
```

## Related Examples
- [arrow mark in marks.md](../marks.md)
- [link mark in marks.md](../marks.md)
- [tree transform in transforms.md](../transforms.md)

## External Resources
- D3 hierarchy for tree layouts: https://d3js.org/d3-hierarchy
- D3 force simulation: https://d3js.org/d3-force
