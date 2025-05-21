# QGIS

- `sudo apt install qgis`
- Try to do things using [GDAL](gdal.md) when possible.
- Unless there's a reason to do otherwise, save vector layers in `.gpkg`.

## Runbooks

### Reload Layer

Open Python Console (Ctrl+Alt+P), paste:
```
iface.activeLayer().dataProvider().reloadData()
```

### Preview Images

1. Have image path in vector layer data, say in a field called `path`.
2. Layer Properties > Attributes Form > (select your path-to-image field)
3. Widget Type: Attachment, Store path as: Relative to Project Path
4. Display Resource Path: check everything I guess...
5. Integrated Document Viewer: Type: Image
6. Apply!
7. "Identify Features" > In "Identify Results" pane, right click feature and choose "View Feature Form"
