[Role Setup]
You are an expert Frontend and Python developer specializing in Geospatial Data processing and advanced HTML5 Canvas/WebGL rendering. I want to build a "Dynamic Halftone Pastel Dot Density Map" that reacts to user zoom interactions.

[Core Requirement: Dynamic Zoom & Screen-Space Rendering]

When zooming in, the pixel size of the dots (e.g., radius 3px) and the pixel spacing between them (e.g., 10px screen distance) MUST remain constant on the screen.

Instead of the dots getting larger, zooming in should reveal more dots for a specific geographic region because that region now occupies a larger screen area. The grid is fixed to the screen, not the map.

[Detailed Implementation Plan & Requests]

Step 1: Data Merging & Formatting (Python / GeoPandas)

Data: map_boundaries.geojson (polygons) and population.csv (densities). Both share a region_code.

Task: Use geopandas to join the CSV density data into the GeoJSON.

Schema: Output a standard GeoJSON file where the density is injected into the properties:

JSON

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Polygon", "coordinates": [...] },
      "properties": { "region_code": "A1", "density": 4500 }
    }
  ]
}
Step 2: Dynamic Sampling via Offscreen Canvas (JavaScript / D3.js + HTML5 Canvas)
To achieve the dynamic grid efficiently without expensive client-side geometry intersections, use the "Pixel Sampling" technique. Write the code based on this logic:

D3 Zoom Setup: Implement d3.zoom() to capture pan/zoom transform states.

Hidden Canvas Rendering (Data Pass):

Create an in-memory Offscreen Canvas matching the screen dimensions.

On every zoom/pan event, use D3's geoPath with the current transform to draw the GeoJSON polygons onto this hidden canvas.

Map the density property to a Grayscale value (0-255) and fill the polygons with this grayscale color (representing the data value).

Screen-space Hex Grid Sampling (Render Pass):

On the visible Main Canvas, clear the background with #121212 (Dark Grey).

Loop through a fixed, screen-space hexagonal grid (staggered X, Y coordinates, e.g., step = 10px).

For each screen (X, Y) point, read the pixel value from the Offscreen Canvas using getImageData (or read from a cached pixel array for performance).

Pastel Palette Mapping & Drawing:

If the hidden pixel is empty, draw a dark grey dot #2A2A2A or nothing.

If there is a grayscale value, map it back to a density weight.

Use a d3.scaleLinear to map the weight to a pastel palette: [Low density -> #DCD3FF (Pastel Purple) -> #FFB3BA (Pastel Pink) -> #BAE1FF (Pastel Blue) -> High density].

Draw a circle with a fixed radius (r=3.5px) at (X, Y) on the Main Canvas and fill it with the mapped pastel color.

Based on this plan, please provide: 1) The Python preprocessing script (Geopandas merge), and 2) The complete, single-file HTML/JS code containing the D3 projection, zoom handling, offscreen rendering, pixel sampling, and drawing logic.