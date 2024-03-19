## Use

Just a personal wiki, using [vimwiki](https://github.com/vimwiki/vimwiki). Proceed to [the index](index.md).

Run like this:

	vim -c VimwikiIndex

If in vim already:

	<Leader>ww

## Build HTML

There's a [Makefile](Makefile), which runs [build.sh](build.sh), which generates HTML.

### Dependencies

Probably `fd` and `pandoc`, `php` for the dev web server. On Debians: `sudo apt install fdfind pandoc php`.

### Develop

	make develop

...and visit http://localhost:8321/

### Deploy

	make build

That creates html files with links without the `.html` part, requiring server-side url rewrites.

## Scala scripts

This repo contains some Ammonite scripts. To run them, install Ammonite:

	curl -L https://github.com/lihaoyi/ammonite/releases/download/2.5.5/2.13-2.5.5 > amm
	chmod +x amm && mv amm ~/.local/bin/

