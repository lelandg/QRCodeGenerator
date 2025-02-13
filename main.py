__author__ = "Leland Green"
__version__ = "0.1.1"
__date_created__ = "2025-02-13"
__last_updated__ = "2025-02-13"
__email__ = "lelandgreenproductions@gmail.com"

__license__ = "Open Source"  # License of this script is free for all purposes.

f"""
* Automatically generate a QR code for your website, Wi-Fi network, etc.
* Optionally include your own image in the center of the QR code.
* Specify the output file name.

Author: {__author__}
Version: {__version__}
Date: {__date_created__}
Last Updated: {__last_updated__}
Email: {__email__}

License:
{__license__}

"""
import argparse
from generate_qr_code import generate_qr_code  # Assuming generate_qr_code is defined elsewhere


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Generate a QR code with optional embedded image.")

    # Define the arguments
    parser.add_argument("link", type=str,
                        help="The link or text to encode in the QR code. This is the only *required* argument.")
    parser.add_argument("--image", "-i", type=str, default=None,
                        help="Optional image path to embed in the center of the generated QR code.")
    parser.add_argument("--outname", "-o", type=str, default="qrcode.png",
                        help="Optional output file name for the generated QR code. (Default: qrcode.png)")

    # Check if no arguments were passed
    import sys
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Parse the command line arguments
    args = parser.parse_args()

    # Generate the QR code with the parsed arguments
    generate_qr_code(text=args.link, image_path=args.image, output_path=args.outname)


if __name__ == "__main__":
    main()
