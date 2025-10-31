import json, os
import click
from pathlib import Path

@click.command()
@click.option("--in",  "in_path",  required=True, type=click.Path(exists=True), help="Input image (OME-TIFF, etc.)")
@click.option("--out", "out_dir",  required=True, type=click.Path(), help="Output directory")
def main(in_path, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    summary = {
        "input": os.path.abspath(in_path),
        "n_cells": 0,
        "counts": {"G1": 0, "S": 0, "G2/M": 0}
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"[cellcycle] Wrote {out/'summary.json'}")

if __name__ == "__main__":
    main()
