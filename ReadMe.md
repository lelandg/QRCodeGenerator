Features:
* Automatically generate a QR code for your website, Wi-Fi network, etc.
* Optionally include your own image in the center of the QR code.
* Specify the output file name.

**Installation:** 

Download/clone the repository and run the following commands in the root directory of the project:
pip install -r requirements.txt

**Usage:**

Running `python main.py` with no arguments will show this help screen:

```
usage: main.py [-h] [--image IMAGE] [--filter] [--outname OUTNAME] [--version] [-r] link

Generate a QR code with optional embedded image.

positional arguments:
  link                  The link or text to encode in the QR code. This is the only *required* argument.

options:
  -h, --help            show this help message and exit
  --image IMAGE, -i IMAGE
                        Optional image path to embed in the center of the generated QR code.
  --filter, -f          Disable image filtering (edge detection and thresholding).
  --outname OUTNAME, -o OUTNAME
                        Optional output file name for the generated QR code. (Default: qrcode.png)
  --version             show program's version number and exit
  -r, --read            Follow this with the file name to read. E.g. '-r my_qrcode.png' Read and decode QR codes from
                        an image file and display the text inside. This overrides the QR code generation, so nothing
                        else is required.
```

**Examples**

Where [IMAGE] and [OUTNAME] are valid file paths.

`python main.py [--image IMAGE] [--outname OUTNAME] link`

`python main.py "https://example.com" -i "logo.png" <-f> -o "logo_qr.png"` 

`python main.py -r [IMAGE]`  

**Notes**

Using -i lets you specify an image for the center of the QR code.

Using -f will disable filtering of this image. (Recommended if your image is B&W/Grayscale, 
between 92 and 100 pixels in size, and has a white background.)

Using -o lets you specify the output file name. Default is "qrcode.png".

Using -r will read the contents of a QR code and print it to the console. 

The only required argument is "link". May include spaces if enclosed in double quotes. Can be a URL, text, etc.
