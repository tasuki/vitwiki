# OpenDroneMap

Some settings I like, with overview of the time taken from the log:

```
CPUS="35";
MEMORY="400g";
PROJECT="project";
DATE=`date '+%Y-%m-%d_%H-%M'`;
docker run --memory="$MEMORY" -it --rm \
    -v /data/odm:/datasets opendronemap/odm:latest \
    --max-concurrency="$CPUS" --orthophoto-resolution=1 --dem-resolution=5 --min-num-features=20000 \
    --skip-3dmodel --dsm --feature-quality=high --pc-quality=high \
    --build-overviews --orthophoto-compression=JPEG --project-path /datasets "$PROJECT" > odm_log_"$DATE".log;
jq -r '.stages[] | "\(.startTime[:10]) \(.startTime[11:16])  \(.name)"' \
    /data/odm/"$PROJECT"/log.json > ~/odm_log_"$DATE"_summary.txt;
```
