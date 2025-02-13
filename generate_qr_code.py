import qrcode
from PIL import Image, ImageDraw, ImageFilter

def generate_qr_code(text, image_path=None, output_path="qrcode.png"):
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
            img = img.filter(ImageFilter.FIND_EDGES)  # Apply edge detection
            img = img.point(lambda x: 0 if x < 128 else 255, '1')  # Thresholding

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


# Example usage
if __name__ == "__main__":
    # Generate a QR code with embedded text and optional image
    text_input = "https://lelandgreen.com"
    image_input_path = "Self-Portrait.jpg"  # Provide a valid image path, or None to skip
    generate_qr_code(text_input, image_path=image_input_path, output_path="lelandgreen.com_qrcode.png")