# Syncthing

Set up on server...

```
USER=thisisme
DEVICE_ID=CLIENT-DEVICE-ID # get this from the client!
DEVICE_NAME=DEVICE-NAME
SHARE_PATH=/path/to/shared/dir/
SHARE_ID=shared-dir-name
sudo systemctl enable "syncthing@$USER.service"
sudo systemctl start "syncthing@$USER.service"
syncthing cli config devices list
# on the client, add the server's device id
syncthing cli config devices add --device-id "$DEVICE_ID" --name "$DEVICE_NAME"
syncthing cli config folders add --id "$SHARE_ID" --path "$SHARE_PATH"
syncthing cli config folders "$SHARE_ID" devices add --device-id "$DEVICE_ID"
```
