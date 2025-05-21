# GDAL - Geospatial Data Abstraction Library

- `sudo apt install gdal`
- `export GDAL_NUM_THREADS=ALL_CPUS` to parallelize


## Vectors

- Prefer `GPKG`.
- Consider compressing `GeoJSON` files.

Reproject:
```
ogr2ogr -f GeoJSON out.json in.json -t_srs EPSG:4326
ogr2ogr -f GPKG out.gpkg in.gpkg -t_srs EPSG:4326
```

**Note: This moves things by two meters for me, better use QGIS?**



## Rasters

- Use compression, `DEFLATE` for lossless, `JPEG` for lossy (large orthophotos).
- Use `COG` (Cloud Optimized GeoTIFF) for whatever needs to be opened in QGIS.

Inspect a GeoTIFF:
```
gdalinfo in.tif
```

See details of `*.tif` in the current dir:
```
for f in *.tif; do           
	printf "%s: %s %s with %s in EPSG:%s\n" "$f" \
		"$(gdalinfo -json "$f" | jq -r '"\(.size[0])x\(.size[1])"')" \
		"$(gdalinfo -json "$f" | jq -r '.metadata.IMAGE_STRUCTURE.LAYOUT')" \
		"$(gdalinfo -json "$f" | jq -r '.metadata.IMAGE_STRUCTURE.COMPRESSION')" \
		"$(gdalinfo -json "$f" | jq -r '.stac."proj:epsg"')"
done
```

Turn a GeoTIFF into COG (fast viewing):
```
gdal_translate -of COG -co COMPRESS=DEFLATE in.tif out.tif
```

Turn an orthophoto GeoTIFF into COG with JPEG compression:
```
gdal_translate -of COG -co COMPRESS=JPEG in.tif out.tif
```

Merge GeoTIFFs:
```
gdalwarp -of COG -co COMPRESS=DEFLATE in*.tif out.tif
```

### Sum GeoTIFFs (eg sparse LiDAR point clouds)

Change the boundaries of a GeoTIFF (upper left x, upper left y, lower right x, lower right y):
```
gdalwarp -of GTiff -co COMPRESS=DEFLATE \
	-t_srs "EPSG:5514" \
	-te -602000 -1166000 -594000 -1155000 \
	-r near in.tif out.tif
```

Merge two GeoTIFFs with the same boundaries, taking max value from each:
```
gdal_calc.py -A in1.tif -B in2.tif --outfile=out.tif \
	--calc="maximum(A,B)" --format=GTiff --co="COMPRESS=DEFLATE"
```
