"""
ABOUTME: Observable Plot Viewer Server - HTTP server for interactive plot visualization
ABOUTME: Serves static viewer files and plot JSON files from launch directory

Starts a local HTTP server and opens the Observable Plot viewer in your browser.
Claude can write plot code to JSON files that the viewer will load.

The server captures the launch directory on startup and creates/monitors a plots/
subdirectory there. Even though the server changes its working directory to serve
static HTML files, it maintains an absolute path to the plots directory for reading
plot files.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
import glob

PORT = 8765
# PLOTS_DIR will be set in main() based on --plots-dir argument, defaulting to ./plots
# Set a default here so the server can handle requests even during initialization
PLOTS_DIR = (Path.cwd() / "plots").absolute()
CURRENT_PLOT_FILE = PLOTS_DIR / ".current-plot.json"

# Track viewer state and errors for debugging
VIEWER_STATE = {
    "last_error": None,
    "last_error_time": None,
    "error_count": 0,
    "recent_errors": []  # Keep last 10 errors
}


def ensure_plots_dir():
    """Ensure plots directory exists"""
    PLOTS_DIR.mkdir(exist_ok=True)
    print(f"Using plots directory: {PLOTS_DIR.absolute()}")


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve the viewer and plot files"""

    def do_POST(self):
        """Handle POST requests"""
        if self.path == "/error":
            # Receive error reports from the viewer
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                error_data = json.loads(body.decode('utf-8'))

                # Update viewer state
                VIEWER_STATE["last_error"] = error_data.get("message", "Unknown error")
                VIEWER_STATE["last_error_time"] = datetime.now().isoformat()
                VIEWER_STATE["error_count"] += 1

                # Add to recent errors (keep last 10)
                VIEWER_STATE["recent_errors"].append({
                    "message": error_data.get("message", "Unknown error"),
                    "stack": error_data.get("stack", ""),
                    "timestamp": VIEWER_STATE["last_error_time"]
                })
                if len(VIEWER_STATE["recent_errors"]) > 10:
                    VIEWER_STATE["recent_errors"].pop(0)

                print(f"[ERROR] {error_data.get('message', 'Unknown error')}")

                self.wfile.write(json.dumps({"status": "ok"}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/code":
            # Serve the current plot code
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if PLOTS_DIR is None:
                    self.wfile.write(b"// Server not yet initialized")
                    return
                if CURRENT_PLOT_FILE and CURRENT_PLOT_FILE.exists():
                    with open(CURRENT_PLOT_FILE, 'r') as f:
                        data = json.load(f)
                    code = data.get('code', '')
                    self.wfile.write(code.encode())
                else:
                    self.wfile.write(b"// No code file found")
            except Exception as e:
                self.wfile.write(f"// Error reading code: {e}".encode())

        elif self.path == "/code-mtime":
            # Return modification time of current plot file
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if PLOTS_DIR is None or CURRENT_PLOT_FILE is None:
                    self.wfile.write(json.dumps({"mtime": None}).encode())
                    return
                if CURRENT_PLOT_FILE.exists():
                    mtime = os.path.getmtime(CURRENT_PLOT_FILE)
                    response = json.dumps({"mtime": mtime})
                    self.wfile.write(response.encode())
                else:
                    self.wfile.write(json.dumps({"mtime": None}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif self.path == "/plots-dir":
            # Return the plots directory path for display
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if PLOTS_DIR is None:
                    self.wfile.write(json.dumps({
                        "error": "Server not yet initialized",
                        "plots_dir": None,
                        "exists": False
                    }).encode())
                    return
                response = {
                    "plots_dir": str(PLOTS_DIR.absolute()),
                    "exists": PLOTS_DIR.exists()
                }
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif self.path == "/plots":
            # List all plot files
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if PLOTS_DIR is None:
                    self.wfile.write(json.dumps([]).encode())
                    return
                ensure_plots_dir()
                plot_files = []
                for json_file in sorted(PLOTS_DIR.glob("*.json"), key=os.path.getmtime, reverse=True):
                    # Skip the current plot marker file
                    if json_file.name.startswith('.'):
                        continue
                    try:
                        with open(json_file, 'r') as f:
                            data = json.load(f)
                        plot_files.append({
                            'filename': json_file.name,
                            'name': data.get('name', json_file.stem),
                            'description': data.get('description', ''),
                            'timestamp': data.get('timestamp', os.path.getmtime(json_file)),
                            'mtime': os.path.getmtime(json_file)
                        })
                    except Exception as e:
                        print(f"Error reading {json_file}: {e}")

                self.wfile.write(json.dumps(plot_files).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif self.path == "/viewer-status":
            # Return viewer state and errors for debugging
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                status = {
                    **VIEWER_STATE,
                    "plots_dir": str(PLOTS_DIR.absolute()) if PLOTS_DIR else None,
                    "plots_dir_exists": PLOTS_DIR.exists() if PLOTS_DIR else False,
                    "server_time": datetime.now().isoformat()
                }
                self.wfile.write(json.dumps(status, indent=2).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif self.path.startswith("/plot/"):
            # Load a specific plot file
            filename = self.path[6:]  # Remove "/plot/" prefix
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if PLOTS_DIR is None:
                    self.wfile.write(json.dumps({"error": "Server not yet initialized"}).encode())
                    return
                plot_file = PLOTS_DIR / filename
                if plot_file.exists() and plot_file.suffix == '.json':
                    with open(plot_file, 'r') as f:
                        data = json.load(f)
                    # Update current plot
                    with open(CURRENT_PLOT_FILE, 'w') as f:
                        json.dump(data, f, indent=2)
                    self.wfile.write(json.dumps(data).encode())
                else:
                    self.wfile.write(json.dumps({"error": "Plot file not found"}).encode())
            except Exception as e:
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            # Serve static files normally
            super().do_GET()

    def log_message(self, format, *args):
        """Custom logging"""
        # Don't log code polling or plots listing requests
        quiet_paths = ["/code", "/code-mtime", "/plots", "/plots-dir", "/viewer-status", "/error"]
        if self.path not in quiet_paths and not self.path.startswith("/plot/"):
            print(f"[{self.address_string()}] {format % args}")


def create_example_plot():
    """Create example plot file"""
    ensure_plots_dir()

    example_code = '''// Observable Plot Example
// Edit this code and it will update in the viewer

const data = [
  { x: 1, y: 2, category: "A" },
  { x: 2, y: 5, category: "B" },
  { x: 3, y: 3, category: "A" },
  { x: 4, y: 8, category: "B" },
  { x: 5, y: 6, category: "A" }
];

return Plot.plot({
  marks: [
    Plot.dot(data, {
      x: "x",
      y: "y",
      fill: "category",
      r: 8,
      tip: true
    }),
    Plot.ruleY([0])
  ],
  color: { legend: true }
})'''

    plot_data = {
        'name': 'Example Plot',
        'description': 'Basic scatterplot with categories',
        'code': example_code,
        'timestamp': datetime.now().isoformat()
    }

    # Save as a named file
    filename = f"example-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(PLOTS_DIR / filename, 'w') as f:
        json.dump(plot_data, f, indent=2)

    # Also set as current plot
    with open(CURRENT_PLOT_FILE, 'w') as f:
        json.dump(plot_data, f, indent=2)

    print(f"Created example plot: {PLOTS_DIR / filename}")


def find_static_dir():
    """Find the directory containing index.html"""
    # Try package directory
    package_dir = Path(__file__).parent.parent
    if (package_dir / "index.html").exists():
        return package_dir

    # Try current directory
    if Path("index.html").exists():
        return Path.cwd()

    raise FileNotFoundError("Could not find index.html. Make sure you're in the viewer directory.")


def check_server_running(port):
    """Check if a server is already running on the port"""
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0


def main():
    global PLOTS_DIR, CURRENT_PLOT_FILE

    parser = argparse.ArgumentParser(description='Launch Observable Plot Viewer')
    parser.add_argument('--port', type=int, default=PORT, help=f'Port to run server on (default: {PORT})')
    parser.add_argument('--plots-dir', type=str, help='Directory containing plot JSON files (default: ./plots)')
    parser.add_argument('--no-browser', action='store_true', help='Don\'t open browser automatically')
    parser.add_argument('--create-example', action='store_true', help='Create example plot file')
    args = parser.parse_args()

    # Set PLOTS_DIR based on argument or default to current directory
    if args.plots_dir:
        PLOTS_DIR = Path(args.plots_dir).absolute()
    else:
        PLOTS_DIR = (Path.cwd() / "plots").absolute()

    CURRENT_PLOT_FILE = PLOTS_DIR / ".current-plot.json"

    print(f"Plots directory will be: {PLOTS_DIR}")

    # Check if server is already running
    url = f"http://localhost:{args.port}/index.html"
    if check_server_running(args.port):
        print("=" * 60)
        print("Observable Plot Viewer")
        print("=" * 60)
        print(f"Server already running at: {url}")
        print(f"NOTE: The server was launched with its own plots directory.")
        print(f"Your specified plots directory: {PLOTS_DIR}")
        print(f"Make sure they match, or stop and restart the server.")
        print("=" * 60)

        # Open browser if requested
        if not args.no_browser:
            print(f"Opening browser to {url}...")
            webbrowser.open(url)
        return

    # Ensure plots directory exists (do this BEFORE changing directories)
    ensure_plots_dir()

    # Change to the static directory
    try:
        static_dir = find_static_dir()
        print(f"Serving static files from: {static_dir}")
        os.chdir(static_dir)
        print(f"Changed working directory to: {Path.cwd()}")
        print(f"Will read plot files from: {PLOTS_DIR}")

        # Verify we can still access the plots directory
        if not PLOTS_DIR.exists():
            print(f"WARNING: Plots directory not accessible: {PLOTS_DIR}")
        else:
            print(f"✓ Plots directory is accessible")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create example plot file if requested
    if args.create_example:
        create_example_plot()

    # Start the server
    Handler = CustomHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", args.port), Handler) as httpd:
            print("=" * 60)
            print("Observable Plot Viewer")
            print("=" * 60)
            print(f"Server running at: {url}")
            print(f"Watching plots directory: {PLOTS_DIR}")
            print()
            print("Instructions:")
            print(f"  1. Claude should write plot files to: {PLOTS_DIR}")
            print("  2. Use the history sidebar to switch between plots")
            print("  3. Edit code in the editor to see live updates")
            print("  4. Charts update automatically as you type")
            print("  5. Press Ctrl+C to stop the server")
            print("=" * 60)

            # Open browser
            if not args.no_browser:
                print(f"Opening browser to {url}...")
                webbrowser.open(url)

            print("\nServer is ready. Press Ctrl+C to stop.\n")
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\nShutting down server...")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\nPort {args.port} is already in use.")
            print(f"Assuming viewer is already running at: {url}")
            if not args.no_browser:
                webbrowser.open(url)
        else:
            print(f"\nError starting server: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
