#!/usr/bin/env python3

# sudo apt install python3-fonttools

import argparse
import sys
from fontTools import subset
from pathlib import Path

def subset_font(input_path, unicodes="0020-00FF", output_path=None, flavor="woff2"):
    src = Path(input_path)
    if not src.exists():
        raise FileNotFoundError(f"Source font not found: {src}")

    if output_path is None:
        dst = src.parent / f"{src.stem}.subset.{flavor}"
    else:
        dst = Path(output_path)

    # Some interesting unicode ranges:
    # 0020-007F: basic latin
    # 0080-00FF: latin supplement (western europe)
    # 0100-017F: latin extended-a (central europe)
    # 2000-206F: punctuation

    args = [
        str(src),
        f"--unicodes={unicodes}",
        f"--no-layout-closure",
        f"--output-file={dst}",
        f"--flavor={flavor}",
    ]
    subset.main(args)
    return dst

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subset font files")
    parser.add_argument("files", nargs="+", help="Input font files")
    parser.add_argument("--unicodes", default="0020-007F, 0080-00FF", help="Unicode ranges to include")
    parser.add_argument("--out-dir", help="Output directory")
    parser.add_argument("--flavor", default="woff2", help="Output format (default: woff2)")

    args = parser.parse_args()
    for file_path in args.files:
        try:
            target_dst = None
            if args.out_dir:
                target_dst = Path(args.out_dir) / f"{Path(file_path).stem}.subset.{args.flavor}"

            result = subset_font(
                input_path=file_path,
                unicodes=args.unicodes,
                output_path=target_dst,
                flavor=args.flavor
            )
            print(f"Success: {result}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
