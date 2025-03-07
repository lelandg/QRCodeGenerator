__author__ = "Leland Green"
__version__ = "0.1.3"
__date_created__ = "2025-02-13"
__last_updated__ = "2025-03-07" # Date of the last update. If I remember to update this! Trust GitHub more! ;-)
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
from qr_code_utils import *


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Generate a QR code with optional embedded image.")

    # Define the arguments
    parser.add_argument("link", type=str,
                        help="The link or text to encode in the QR code. This is the only *required* argument.")
    parser.add_argument("--image", "-i", type=str, default=None,
                        help="Optional image path to embed in the center of the generated QR code.")
    parser.add_argument("--filter", "-f", default=True, action="store_false",
                        help="Disable image filtering (edge detection and thresholding).")
    parser.add_argument("--outname", "-o", type=str, default="qrcode.png",
                        help="Optional output file name for the generated QR code. (Default: qrcode.png)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-r", "--read", default=False, action="store_true",
                        help="Follow this with the file name to read. E.g. '-r my_qrcode.png'\r\n"
                        "Read and decode QR codes from an image file and display the text inside.\r\n"
                        "This overrides the QR code generation, so nothing else is required.")

    # Check if no arguments were passed
    import sys
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Parse the command line arguments
    args = parser.parse_args()

    if args.read:
        # Read and decode QR codes from an image file
        qr_texts = read_qrcode_from_file(file_path=args.link)

        # Display the decoded text
        for i, text in enumerate(qr_texts, start=1):
            print(f"QR Code {i}: {text}")
        return
    else:
        # Generate the QR code with the parsed arguments
        generate_qr_code(text=args.link, image_path=args.image, output_path=args.outname, filter_image=args.filter)


if __name__ == "__main__":
    main()
