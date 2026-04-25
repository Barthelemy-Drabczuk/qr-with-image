# QR Code Generator

Generate QR codes with an embedded logo in the center, using high error correction to keep codes scannable.

## Requirements

- [Pixi](https://pixi.sh) — handles the Python environment and dependencies automatically

## Setup

```bash
pixi install
```

## Usage

```bash
pixi run python generate_qr.py <url> [logo] [-o output]
```

| Argument | Required | Default | Description |
|---|---|---|---|
| `url` | yes | — | URL or data to encode |
| `logo` | yes | — | Image to embed in the center |
| `-o`, `--output` | no | `qr_output.png` | Output file path |

## Examples

```bash
# Basic usage
pixi run python generate_qr.py "https://example.com" my_logo.png

# Custom output path
pixi run python generate_qr.py "https://example.com" my_logo.png -o result.png
```

## How it works

The script uses `ERROR_CORRECT_H` (30% error correction), which allows up to 30% of the QR code to be obscured while remaining scannable. The logo is resized to fit within 30% of the QR code area and centered on top.
