Features:
* Automatically generate a QR code for your website, Wi-Fi network, etc.
* Optionally include your own image in the center of the QR code.
* Specify the output file name.

**Installation:** 
Download/clone the repository and run the following commands in the root directory of the project:
pip install -r requirements.txt

**Usage:**
usage: 
python main.py [--image IMAGE] [--outname OUTNAME] link
python main.py "https://example.com" -i "logo.png" -o "logo_qr.png"

Running "python main.py" with no arguments will show the help screen.
The only required argument is "link". May include spaces if enclosed in double quotes. Can be a URL, text, etc.

