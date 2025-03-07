import qrcode
from pyzbar.pyzbar import decode

from PIL import Image, ImageDraw, ImageFilter

def generate_qr_code(text, image_path=None, output_path="qrcode.png", filter_image=True):
    """
    Generate a QR code from text input and optionally embed an image in the center.
    
    Args:
        text (str): The text to encode in the QR code.
        image_path (str, optional): Path to the image file to embed in the center. Defaults to None.
        output_path (str): Path to save the output QR code image. Defaults to 'qrcode.png'.
    """
    # Step 1: Generate the basic QR Code
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for image embedding
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    qr_code_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if image_path:
        # Step 2: Process the image input
        try:
            img = Image.open(image_path)

            # Convert to black-and-white outline for aesthetics
            img = img.convert("L")  # Convert to grayscale
            if filter_image:
                # img = img.filter(ImageFilter.SMOOTH_MORE)  # Noise reduction
                img = img.filter(ImageFilter.FIND_EDGES)  # Apply edge detection
                img = img.point(lambda x: 255 if x < 128 else 0, '1')  # Thresholding

            # Resize the image to fit in the center of the QR code
            qr_width, qr_height = qr_code_image.size
            img_width = qr_width // 4
            img_height = qr_height // 4
            img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)

            # Step 3: Embed the image in the center of the QR code
            xpos = (qr_width - img_width) // 2
            ypos = (qr_height - img_height) // 2
            qr_code_image.paste(img, (xpos, ypos))

        except Exception as e:
            print(f"Error processing the image: {e}")
            return

    # Step 4: Save the generated QR code
    qr_code_image.save(output_path)
    print(f"QR Code generated and saved to {output_path}")

def read_qrcode_from_file(file_path):
    """
    Reads and decodes QR codes in the provided image file.

    Args:
        file_path (str): Path to the image file to scan for QR codes.

    Returns:
        list: A list of decoded text strings from the QR codes.
    """
    try:
        # Open the image using PIL
        image = Image.open(file_path)

        # Decode QR codes in the image
        decoded_objects = decode(image)

        # Extract text from each QR code
        qr_texts = [obj.data.decode('utf-8') for obj in decoded_objects]

        if qr_texts:
            return qr_texts
        else:
            return ["No QR codes were found in the image."]
    except Exception as e:
        return [f"Error reading QR code: {e}"]


# Example usage
if __name__ == "__main__":
    # Generate a QR code with embedded text and optional image
    text_input = "https://lelandgreen.com"
    image_input_path = "Self-Portrait.jpg - 99x99-B&W.jpg"  # Provide a valid image path, or None to skip
    generate_qr_code(text_input,
                     image_path=image_input_path,
                     output_path="lelandgreen.com_qrcode.png",
                     filter_image=False)