# GDAL - Geospatial Data Abstraction Library

- `sudo apt install gdal`
- `export GDAL_NUM_THREADS=ALL_CPUS` to parallelize


## Vectors

- Prefer `GPKG`.
- Consider compressing `GeoJSON` files.

Convert:
```
ogr2ogr -f GPKG out.gpkg in.json
```

Convert and set layer name:
```
ogr2ogr -f GPKG out.gpkg in.json -nln layername
```

Reproject:
```
ogr2ogr -f GeoJSON out.json in.json -t_srs EPSG:4326
ogr2ogr -f GPKG out.gpkg in.gpkg -t_srs EPSG:4326
```

**Note: This moves things by two meters for me, better use QGIS?**



## Rasters

- Use compression, `DEFLATE` for single-band (eg DSM), `YCbCr JPEG` for RGB (eg orthophotos).
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

Turn a single-band GeoTIFF into COG:
```
gdal_translate -of COG -stats -co COMPRESS=DEFLATE -co PREDICTOR=YES in.tif out.tif
```

Turn a RGB GeoTIFF into COG with JPEG compression:
```
gdal_translate -of COG -stats -co COMPRESS=JPEG in.tif out.tif
```

Merge GeoTIFFs:
```
gdalwarp -of COG -stats -co COMPRESS=DEFLATE in*.tif out.tif
```

### Transparency

There are at least four ways a GeoTIFF can encode transparency:
- an alpha band (for RGB, the 4th band): rather heavy, allows partial transparency
- a `nodata` value: one loses the
- a `PER_DATASET` mask: the most ergonomic option, global bitmask

Set a `nodata` value:
```
gdal_translate -a_nodata 0 -of COG -stats -co COMPRESS=JPEG in.tif out.tif
```

Reproject a 1-band tif with nodata:
```
gdalwarp -s_srs EPSG:4326 -t_srs EPSG:32633 -dstalpha in.tif tmp_alpha.tif
rio cogeo create tmp_alpha.tif out.tif --cog-profile deflate --add-mask --bidx 1
```

### Clip GeoTIFF by mask

RGB:
```
gdalwarp -of GTIFF -co TILED=YES -overwrite -dstalpha \
    -cutline mask.gpkg -crop_to_cutline \
    in.tif /tmp/tmp_clipped.tif
gdal_translate -of COG -stats -co COMPRESS=JPEG /tmp/tmp_clipped.tif out.tif
```

Single-band:
```
gdalwarp -of GTIFF -co TILED=YES -overwrite -dstalpha \
    -cutline mask.gpkg -crop_to_cutline \
    in.tif /tmp/tmp_clipped.tif
gdal_translate -of COG -stats -co COMPRESS=DEFLATE -co PREDICTOR=YES \
	-b 1 -mask 2 /tmp/tmp_clipped.tif out.tif
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
