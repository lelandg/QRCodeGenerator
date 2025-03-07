__author__ = "Leland Green"
__version__ = "0.1.4"
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
import sys


def main():
    print(f"QR Code Generator v{__version__}. Author: {__author__}\r\n")
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Generate or read a QR code. "
                                                 "Embed an optional embedded image, or create a Wi-Fi access QR code.")

    # Define the arguments
    parser.add_argument("--text", "-t", type=str, 
                        help="The text to encode in the QR code, or image file name to read. "
                             "This is required when creating a QR code. (Except when using '-w'.)")
    parser.add_argument("--image", "-i", type=str, default=None,
                        help="Optional image path to embed in the center of the generated QR code.")
    parser.add_argument("--filter", "-f", default=True, action="store_false",
                        help="Disable image filtering (edge detection and thresholding).")
    parser.add_argument("--outname", "-o", type=str, default="qrcode.png",
                        help="Optional output file name for the generated QR code. (Default: qrcode.png)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-r", "--read", default=False, action="store_true",
                        help="Follow this with the file name to read. E.g. '-r my_qrcode.png' "
                        "Read and decode QR codes from an image file and display the text inside. "
                        "This overrides the QR code generation, so nothing else is required.")
    parser.add_argument("--wifi", "-w", default=False, action="store_true",
                        help="Generate a QR code for a Wi-Fi network. This will use the current network details. "
                        "This provides all info needed for the QR code, so no other arguments are required. "
                        "The output file name will be 'wifi_qrcode.png', unless you specify it. "
                        "(Yes, it detects your Wi-Fi password. No, it doesn't store it, other than in the image.)")

    # Parse the command line arguments
    args = parser.parse_args()

    if args.read:
        # Read and decode QR codes from an image file
        qr_texts = read_qrcode_from_file(file_path=args.text)

        # Display the decoded text
        for i, text in enumerate(qr_texts, start=1):
            print(f"QR Code {i}: {text}")
    elif args.wifi:
        # Generate a QR code for a Wi-Fi network
        ssid, encryption, password = get_wifi_details()
        if ssid and encryption:
            if args.outname == "qrcode.png":
                args.outname = "wifi_qrcode.png"
            create_wifi_qr(ssid, encryption, password, output_filename=args.outname)
        else:
            print("Could not create QR code. Missing Wi-Fi details.")
    else:
        if not args.text:
            parser.print_help()
            print("\r\nError: No text provided for the QR code. Must use --text or -t argument."
                  "Unless you're reading a QR code with -r or creating one for Wi-Fi with -w.")
            sys.exit(1)
        # Generate the QR code with the parsed arguments
        generate_qr_code(text=args.text, image_path=args.image, output_path=args.outname, filter_image=args.filter)


if __name__ == "__main__":
    main()
