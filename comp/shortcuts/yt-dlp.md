# Downloading music from YooTube

Not really shortcuts, but here we go...

2024 Debian, `apt install pipx` to install python packages, then `pipx install yt-dlp` to get a reasonably working version of yt-dlp.

Download a playlist:

```
yt-dlp -f bestaudio -x --audio-format mp3 --output "%(playlist_index)02d - %(title)s.%(ext)s" 'https://www.youtube.com/watch?list=playlist-id'
```

---

Add id3 tags, presto:

```
for file in "$DIR"*.mp3; do
    TRACK=$(echo "$file" | sed -E 's/^([0-9]+) - .+\.mp3$/\1/')
    TITLE=$(echo "$file" | sed -E 's/^[0-9]+ - (.+)\.mp3$/\1/')

    id3v2 \
        --artist "" \
        --album "" \
        --year "" \
        --track "$TRACK" \
        --song "$TITLE" \
        "$file"

    echo "Updated: $file"
done
```

---

Put cover image into the folder as `cover.jpg` or something maybe...
