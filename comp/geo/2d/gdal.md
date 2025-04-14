# GDAL - Geospatial Data Abstraction Library

- `sudo apt install gdal`
- `export GDAL_NUM_THREADS=ALL_CPUS` to parallelize
- Use compression, `DEFLATE` for lossless, `JPEG` for lossy (large orthophotos).
- Use `COG` (Cloud Optimized GeoTIFF) for whatever needs to be opened in QGIS.

## Snippets

Inspect a GeoTIFF:
```
gdalinfo in.tif
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
	-te -602000 -1155000 -594000 -1166000 \
	-r near in.tif out.tif
```

Merge two GeoTIFFs with the same boundaries, taking max value from each:
```
gdal_calc.py -A in1.tif -B in2.tif --outfile=out.tif \
	--calc="maximum(A,B)" --format=GTiff --co="COMPRESS=DEFLATE"
```


### Sum GeoTIFFs (eg sparse LiDAR point clouds)

```
gdal_translate -b mask -of COG -co COMPRESS=DEFLATE ortho_2024_podzim_14.tif ortho_2024_podzim_14_mask_deflate.tif
```

