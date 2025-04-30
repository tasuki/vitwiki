# sudo apt install python3-fonttools

from fontTools import subset
from pathlib import Path

home = Path.home()

fonts = {
    f"{home}/.fonts/RecursiveMonoCslSt-Regular.woff2":
        f"{home}/.fonts/rec-mono-csl-regular.woff2",
    f"{home}/.fonts/RecursiveMonoCslSt-Italic.woff2":
        f"{home}/.fonts/rec-mono-csl-italic.woff2",
    f"{home}/.fonts/RecursiveMonoCslSt-Bold.woff2":
        f"{home}/.fonts/rec-mono-csl-bold.woff2",
}

# basic latin, left/right angle quotation marks, curly apostrophe
limit = "--unicodes=0020-007F, 2039-203A, 00D7"

for src, dst in fonts.items():
    args = [
        src,
        limit,
        f"--no-layout-closure",
        f"--output-file={dst}",
        f"--flavor=woff2",
    ]
    subset.main(args)
