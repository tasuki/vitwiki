# OpenDroneMap

Some settings I like, with overview of the time taken from the log:

Put images into `/data/odm/project/images/`, then:

```
CPUS="35";
MEMORY="400g";
PROJECT="project";
DATE=`date '+%Y-%m-%d_%H-%M'`;
ODM_DATASETS="/data/odm"
docker run --memory="$MEMORY" -it --rm \
	-v "$ODM_DATASETS:/datasets" opendronemap/odm:latest \
    --max-concurrency="$CPUS" --orthophoto-resolution=1 --dem-resolution=5 --min-num-features=20000 \
    --skip-3dmodel --dsm --feature-quality=high --pc-quality=high \
    --build-overviews --orthophoto-compression=JPEG --project-path /datasets "$PROJECT" > odm_log_"$DATE".log;
jq -r '.stages[] | "\(.startTime[:10]) \(.startTime[11:16])  \(.name)"' \
	"$ODM_DATASETS/$PROJECT/log.json" > ~/odm_log_"$DATE"_summary.txt
```

To process using the split/merge, add this line to params:

`--split 2000 --split-overlap 50 --sm-no-align \`
