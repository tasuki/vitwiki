# PDAL

Install?? I used conda. You do not want to use conda.

```
pdal info points.laz
```

Compress:
```
pdal translate points.{las,laz}
```

Merge, while preserving 1 mm precision:
```
pdal merge all/*.laz all.laz --writers.las.scale_x=0.001 --writers.las.scale_y=0.001 --writers.las.scale_z=0.001
```

Reproject:
```
pdal translate in.laz out.laz reprojection \
    --writers.las.scale_x=0.001 \
    --writers.las.scale_y=0.001 \
    --writers.las.scale_z=0.001 \
    --writers.las.offset_x="auto" \
    --writers.las.offset_y="auto" \
    --writers.las.offset_z="auto" \
    --filters.reprojection.out_srs="EPSG:4326"
```

## Custom fields

PDAL happily ignores custom fields. So does CloudCompare. Use [laspy](laspy.md)
