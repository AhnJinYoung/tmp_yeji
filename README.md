# Dynamic Halftone Pastel Dot Density Map

A full-screen interactive world map that visualizes population density using a screen-space hexagonal dot grid with a continuous pastel color gradient on a dark background.

![Halftone Dot Density Map](https://img.shields.io/badge/D3.js-v7-orange) ![Canvas](https://img.shields.io/badge/HTML5-Canvas-blue)

## Features

- **Screen-space halftone rendering** — dots remain a fixed pixel size; zooming in reveals more dots rather than enlarging them
- **Per-dot color variation** — fractal Brownian motion noise gives each dot a unique color shift for an organic, glowing aesthetic
- **Continuous pastel gradient** — 9-stop HSL-interpolated scale from deep plum (low density) to electric cyan/white (high density)
- **Interactive pan & zoom** — powered by D3.js zoom behavior
- **Built-in legend** — vertical gradient bar with log-spaced density tick labels

## Quick Start

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- Any local HTTP server (see options below)

> **Note:** Opening `index.html` directly via `file://` will not work because the app fetches world map data from a CDN, which browsers block under the `file://` protocol (CORS policy).

### Option 1: Python (recommended)

```bash
cd ver2
python -m http.server 8080
```

Open **http://localhost:8080** in your browser.

### Option 2: Node.js

```bash
cd ver2
npx serve .
```

### Option 3: VS Code Live Server

1. Install the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension
2. Right-click `index.html` → **Open with Live Server**

## Project Structure

```
ver2/
├── index.html              # Main application (single-file HTML/JS/Canvas)
├── preprocess.py           # Python script to merge GeoJSON + CSV (optional)
├── map_boundaries.geojson  # South Korea regional boundaries (sample data)
├── population.csv          # Population density by region (sample data)
├── merged_data.geojson     # Output of preprocess.py (auto-generated)
├── implementationPlan.md   # Original design specification
├── CLAUDE.md               # Project conventions for AI-assisted development
└── README.md
```

## How It Works

1. **Data loading** — Fetches [Natural Earth 110m](https://github.com/topojson/world-atlas) country boundaries (TopoJSON) from CDN, with ~190 countries' population density values embedded inline
2. **Offscreen pass** — Draws country polygons onto a hidden canvas, filled with grayscale values mapped from density via a log scale
3. **Hex grid sampling** — Iterates a fixed screen-space hexagonal grid (~10px spacing) and reads each pixel's grayscale value from the offscreen canvas
4. **Per-dot coloring** — Adds 4-octave FBM noise to each dot's base density weight, then maps the result through a 1024-entry pre-baked color lookup table
5. **Legend overlay** — Draws a vertical gradient bar with log-spaced numeric labels directly on the canvas

## Optional: South Korea Data Preprocessing

To regenerate the merged South Korea dataset:

```bash
pip install geopandas
python preprocess.py
```

This joins `map_boundaries.geojson` with `population.csv` on `region_code` and outputs `merged_data.geojson`. The main world map visualization does not depend on this step.

## Tech Stack

- [D3.js v7](https://d3js.org/) — projection, zoom, color scales
- [TopoJSON Client](https://github.com/topojson/topojson-client) — boundary data decoding
- [world-atlas](https://github.com/topojson/world-atlas) — Natural Earth 110m country boundaries (loaded from CDN)
- HTML5 Canvas — all rendering (no SVG/DOM elements)
- Python / GeoPandas — optional data preprocessing
