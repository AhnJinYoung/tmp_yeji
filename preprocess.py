"""
Preprocessing script: Merges map_boundaries.geojson with population.csv
Output: merged_data.geojson with density in properties
"""
import geopandas as gpd
import pandas as pd

# Load data
gdf = gpd.read_file("map_boundaries.geojson")
csv = pd.read_csv("population.csv")

# Merge on region_code
merged = gdf.merge(csv[["region_code", "density"]], on="region_code", how="left")
merged["density"] = merged["density"].fillna(0).astype(int)

# Save merged GeoJSON
merged.to_file("merged_data.geojson", driver="GeoJSON")
print(f"Merged {len(merged)} features → merged_data.geojson")
print(merged[["region_code", "density"]].to_string(index=False))
