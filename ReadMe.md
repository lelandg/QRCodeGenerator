Features:
* Automatically generate a QR code for your website, Wi-Fi network, etc.
* Optionally include your own image in the center of the QR code.
* Specify the output file name.
* Read and decode QR codes from an image file.
* Detect Wi-Fi network credentials and creat QR code. (Does not store password, other than in image. 
 Does nothing else with it... check the `code` in `qr_code_utils.py` to verify, if you prefer.)

**QR Code Generator Example for QR Code Generator!**
![QR Code Example](./qrcode_QRCodeGenerator.png) 

**Installation:** 

Download/clone the repository and run the following commands in the root directory of the project:
pip install -r requirements.txt

**Usage:**

Running `python main.py` with no arguments will show this help screen:

```
QR Code Generator v0.1.4. Author: Leland Green

usage: main.py [-h] [--text TEXT] [--image IMAGE] [--filter] [--outname OUTNAME] [--version] [-r] [--wifi]

Generate or read a QR code. Embed an optional embedded image, or create a Wi-Fi access QR code.

options:
  -h, --help            show this help message and exit
  --text TEXT, -t TEXT  The text to encode in the QR code, or image file name to read. This is the only *required*
                        argument.
  --image IMAGE, -i IMAGE
                        Optional image path to embed in the center of the generated QR code.
  --filter, -f          Disable image filtering (edge detection and thresholding).
  --outname OUTNAME, -o OUTNAME
                        Optional output file name for the generated QR code. (Default: qrcode.png)
  --version             show program's version number and exit
  -r, --read            Follow this with the file name to read. E.g. '-r my_qrcode.png'Read and decode QR codes from
                        an image file and display the text inside.This overrides the QR code generation, so nothing
                        else is required.
  --wifi, -w            Generate a QR code for a Wi-Fi network. This will use the current network details.This
                        provides all info needed for the QR code, so no other arguments are required.The output file
                        name will be 'wifi_qrcode.png', unless you specify it.(Yes, it detects your Wi-Fi password.
                        No, it doesn't store it, other than in the image.)
```

**Examples**

Where [IMAGE] and [OUTNAME] are valid file paths.

`python main.py [--image IMAGE] [--outname OUTNAME] -t link-or-text`

`python main.py "https://example.com" -i "logo.png" [-f] -o "logo_qr.png"` 

`python main.py -r [IMAGE]`

`python main.py --wifi`

**Notes**

Using -i lets you specify an image for the center of the QR code.

Using -f will disable filtering of this image. (Recommended if your image is B&W/Grayscale, 
between 92 and 100 pixels in size, and has a white background.)

Using -o lets you specify the output file name. Default is "qrcode.png".

Using -r will read the contents of a QR code and print it to the console. 

It is recommended that you create a QR code, then read and verify it using the -r option.
