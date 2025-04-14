# QGIS

- `sudo apt install qgis`
- Try to do things using [GDAL](gdal.md) when possible.
- Unless there's a reason to do otherwise, save vector layers in `.gpkg`.

Reload layer: Open Python Console (Ctrl+Alt+P), paste:
```
iface.activeLayer().dataProvider().reloadData()
```
