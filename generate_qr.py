import argparse
import sys
from pathlib import Path

import qrcode
from PIL import Image


def generate_qr_with_logo(url: str, logo_path: str, output: str = "qr_output.png") -> None:
    logo_file = Path(logo_path)
    if not logo_file.exists():
        print(f"Error: logo file '{logo_path}' not found.", file=sys.stderr)
        sys.exit(1)

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_width, qr_height = qr_img.size

    logo = Image.open(logo_file).convert("RGBA")
    max_logo_size = int(min(qr_width, qr_height) * 0.3)
    logo.thumbnail((max_logo_size, max_logo_size), Image.LANCZOS)

    logo_width, logo_height = logo.size
    x = (qr_width - logo_width) // 2
    y = (qr_height - logo_height) // 2

    qr_img.paste(logo, (x, y), mask=logo)
    qr_img.save(output)
    print(f"QR code saved to '{output}'")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code with an embedded logo.")
    parser.add_argument("url", help="The URL or data to encode in the QR code")
    parser.add_argument("logo", nargs="?", default="fgb_icon.png", help="Path to the image to embed in the center (default: fgb_icon.png)")
    parser.add_argument("-o", "--output", default="qr_output.png", help="Output file path (default: qr_output.png)")
    args = parser.parse_args()

    generate_qr_with_logo(args.url, args.logo, args.output)


if __name__ == "__main__":
    main()
