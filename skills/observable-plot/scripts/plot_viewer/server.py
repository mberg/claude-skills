"""
Observable Plot Viewer Server

Starts a local HTTP server and opens the Observable Plot viewer in your browser.
Claude can write plot code to a temp file that the viewer will load.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import argparse
from pathlib import Path

PORT = 8765
TEMP_FILE = "/tmp/observable-plot-code.js"


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve the viewer and temp code file"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/code":
            # Serve the temp code file
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                if os.path.exists(TEMP_FILE):
                    with open(TEMP_FILE, 'r') as f:
                        code = f.read()
                    self.wfile.write(code.encode())
                else:
                    self.wfile.write(b"// No code file found")
            except Exception as e:
                self.wfile.write(f"// Error reading code: {e}".encode())
        else:
            # Serve static files normally
            super().do_GET()

    def log_message(self, format, *args):
        """Custom logging"""
        if self.path != "/code":  # Don't log code polling requests
            print(f"[{self.address_string()}] {format % args}")


def create_temp_file_with_example():
    """Create temp file with example code"""
    example_code = '''// Observable Plot Example
// Edit this code and it will update in the viewer

const data = [
  { x: 1, y: 2, category: "A" },
  { x: 2, y: 5, category: "B" },
  { x: 3, y: 3, category: "A" },
  { x: 4, y: 8, category: "B" },
  { x: 5, y: 6, category: "A" }
];

Plot.plot({
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

    with open(TEMP_FILE, 'w') as f:
        f.write(example_code)
    print(f"Created temp file: {TEMP_FILE}")


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


def main():
    parser = argparse.ArgumentParser(description='Launch Observable Plot Viewer')
    parser.add_argument('--port', type=int, default=PORT, help=f'Port to run server on (default: {PORT})')
    parser.add_argument('--no-browser', action='store_true', help='Don\'t open browser automatically')
    parser.add_argument('--create-example', action='store_true', help='Create example temp file')
    args = parser.parse_args()

    # Change to the static directory
    try:
        static_dir = find_static_dir()
        os.chdir(static_dir)
        print(f"Serving files from: {static_dir}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create example temp file if requested
    if args.create_example:
        create_temp_file_with_example()

    # Start the server
    Handler = CustomHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", args.port), Handler) as httpd:
            url = f"http://localhost:{args.port}/index.html"

            print("=" * 60)
            print("Observable Plot Viewer")
            print("=" * 60)
            print(f"Server running at: {url}")
            print(f"Temp code file: {TEMP_FILE}")
            print()
            print("Instructions:")
            print("  1. Edit code in the right pane")
            print("  2. The chart updates automatically as you type")
            print("  3. Claude can write code to the temp file")
            print("  4. Press Ctrl+C to stop the server")
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
            print(f"\nError: Port {args.port} is already in use.")
            print(f"Try a different port with: uv run plot-viewer --port 8766")
        else:
            print(f"\nError starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
