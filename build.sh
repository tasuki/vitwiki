#!/bin/bash

SUFFIX=${SUFFIX:-''}

FD="fdfind"
PANDOC="pandoc"

DIRS=$("$FD" --type d --exclude "/build*")
for D in $DIRS; do
	mkdir -p "build/$D"
done

FILES="index.md drink/tea.md"
FILES=$("$FD" --type f --exclude Makefile --exclude "/build*")
for FILE in $FILES; do
	if [[ "$FILE" == *.md ]]; then
		OUTFILE="build/"$(echo "$FILE" | sed -E "s/\.md/.html/g")
		if [ "$OUTFILE" -nt "$FILE" ] && [ "$OUTFILE" -nt build-template.html ]&& [ "$OUTFILE" -nt build.sh ]; then
			continue
		fi

		CONTENT=$("$PANDOC" "$FILE" | sed -E "s/\.md\"/$SUFFIX\"/g")
		TITLE=""
		for PART in $(echo "$FILE" | tr "/" "\n"); do
			# get rid of .md, replace - with space, uppercase first letter of each word
			TITLEPART=$(echo "$PART" | sed -E "s/\.md$//;s/-/ /g;s/(\b.)/\U\1/g")
			TITLE="$TITLEPART ~ $TITLE"
		done

		echo "mark: $FILE to $OUTFILE"
		export FILE TITLE CONTENT
		envsubst < build-template.html > "$OUTFILE"
	else
		OUTFILE="build/$FILE"
		if [ "$OUTFILE" -nt "$FILE" ]; then
			continue
		fi
		echo "copy: $FILE to $OUTFILE"
		cp "$FILE" "$OUTFILE"
	fi
done

echo "Built!"
