Automated cell-cycle classification for microscopy images (Fiji + Python).

## Quickstart
1) Create venv: `py -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
2) Install deps: `python -m pip install -U pip wheel` then `pip install -r requirements.txt`
3) (Desktop GPU) install torch CUDA wheels (see requirements-gpu.txt)
4) Test CLI: `python -m cellcycle.cli --in data\sample\example.ome.tif --out out\`
