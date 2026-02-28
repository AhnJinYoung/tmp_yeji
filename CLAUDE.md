# Dynamic Halftone Pastel Dot Density Map

## Overview
Interactive map visualization using screen-space hexagonal dot grid with pastel colors on dark background. Zoom reveals more dots (fixed screen-space grid), not larger dots.

## Architecture
- **Python script** (`preprocess.py`): Merges `map_boundaries.geojson` + `population.csv` → `merged_data.geojson` via GeoPandas join on `region_code`
- **HTML/JS** (`index.html`): Single-file app using D3.js + Canvas

## Rendering Pipeline
1. D3 zoom captures pan/zoom transform
2. Offscreen canvas: draw GeoJSON polygons filled with grayscale (density → 0-255)
3. Main canvas: fixed hex grid (step=10px), sample offscreen pixel at each point
4. Map grayscale → pastel palette, draw circle (r=3.5px)

## Visual Spec
- Background: `#000000` (black)
- Empty areas: no dot or `#2A2A2A`
- Palette: `#DCD3FF` (purple) → `#FFB3BA` (pink) → `#BAE1FF` (blue)
- Hex grid spacing: ~10px screen-space
- Dot radius: ~3.5px

## Data Schema
GeoJSON properties: `{ region_code, density }`

## Tech Stack
D3.js v7, HTML5 Canvas, Python/GeoPandas
