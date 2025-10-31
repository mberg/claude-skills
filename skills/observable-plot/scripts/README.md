# Observable Plot Viewer

A live code editor and preview tool for Observable Plot visualizations.

## Features

- **Split-pane interface**: Chart preview on the left, code editor on the right
- **Live updates**: Chart updates automatically as you type (500ms debounce)
- **Monaco Editor**: Full-featured code editor with syntax highlighting
- **Built-in examples**: Load example charts with one click
- **Resizable panes**: Drag the divider to adjust pane sizes
- **Keyboard shortcuts**: ⌘+Enter (or Ctrl+Enter) to manually run code
- **Error display**: Clear error messages when code fails
- **Temp file integration**: Claude can write code to a temp file that loads in the viewer

## Quick Start

### Launch the viewer:

```bash
cd skills/observable-plot/scripts
uv run plot-viewer
```

This will:
1. Install dependencies (first time only)
2. Start a local HTTP server on port 8765
3. Open your browser to the viewer
4. Enable temp file watching for Claude integration

### Options:

```bash
# Use a different port
uv run plot-viewer --port 8080

# Don't auto-open browser
uv run plot-viewer --no-browser

# Create example temp file
uv run plot-viewer --create-example
```

## Usage

### Manual Editing

1. Type or paste Observable Plot code in the right editor pane
2. The chart updates automatically as you type
3. Click "Run" or press ⌘+Enter to manually evaluate
4. Click "Load Example" to try built-in examples
5. Click "Load Temp File" to load code from `/tmp/observable-plot-code.js`

### Claude Integration

Claude can write visualization code that automatically loads in the viewer:

**Ask Claude:**
> "Create a hexbin heatmap and write it to the temp file"

Claude will write the code to `/tmp/observable-plot-code.js` and you can load it with the "Load Temp File" button.

## Code Requirements

Your code should:
- Return a `Plot.plot()` result
- Use the available globals: `Plot`, `d3`
- Be valid JavaScript

### Example:

```javascript
const data = [
  { x: 1, y: 2 },
  { x: 2, y: 5 },
  { x: 3, y: 3 }
];

Plot.plot({
  marks: [
    Plot.dot(data, { x: "x", y: "y", r: 5 }),
    Plot.ruleY([0])
  ]
})
```

## Technical Details

- **Frontend**: Monaco Editor + Observable Plot
- **Backend**: Python HTTP server (managed by UV)
- **Port**: 8765 (configurable)
- **Temp file**: `/tmp/observable-plot-code.js`

## Keyboard Shortcuts

- `⌘+Enter` (or `Ctrl+Enter`): Run code
- Standard Monaco shortcuts for editing

## Development

### Install UV

If you don't have UV installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Run the viewer

```bash
cd skills/observable-plot/scripts
uv run plot-viewer
```

UV will automatically:
- Create a virtual environment
- Install dependencies (none required currently)
- Run the server

## Troubleshooting

**Port already in use:**
```bash
uv run plot-viewer --port 8766
```

**Browser doesn't open:**
```bash
# Manually navigate to:
http://localhost:8765/index.html
```

**Code doesn't load:**
- Make sure you're returning a Plot.plot() result
- Check the error display below the toolbar
- Open browser console for detailed errors

**UV command not found:**
```bash
# Install UV first
curl -LsSf https://astral.sh/uv/install.sh | sh
```
