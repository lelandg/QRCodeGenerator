# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based QR Code Generator that creates QR codes from text/URLs and can embed images in the center. The project supports:
- QR code generation from text/URLs
- Optional image embedding in QR code centers (with filtering)
- QR code reading/decoding from image files
- Wi-Fi network QR code generation (Windows-specific)

## Commands

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
# Show help/usage
python main.py

# Basic QR code generation
python main.py -t "https://example.com"

# With embedded image
python main.py -t "https://example.com" -i "logo.png" -o "output.png"

# Disable image filtering (recommended for B&W images 92-100px with white background)
python main.py -t "https://example.com" -i "logo.png" -f

# Read QR code from file
python main.py -r "qrcode.png"

# Generate Wi-Fi QR code (Windows only)
python main.py --wifi
```

### CLI Options Reference
From `usage.txt`:
- `--text, -t TEXT` - Text to encode (required for generation, except with --wifi)
- `--image, -i IMAGE` - Optional image to embed in center
- `--filter, -f` - Disable image filtering (edge detection/thresholding)
- `--outname, -o OUTNAME` - Output filename (default: qrcode.png)
- `--version` - Show version
- `-r, --read` - Read QR code from image file
- `--wifi, -w` - Generate Wi-Fi QR code using current network

### Testing
No formal test suite exists. Manual testing is done by:
1. Creating QR codes with various parameters
2. Reading them back with the `-r` flag to verify correctness

## Code Architecture

### Main Components

1. **main.py** - Entry point with argument parsing and command orchestration
   - Handles CLI arguments using argparse
   - Routes to appropriate functions based on operation mode (generate/read/wifi)
   - Contains version info and metadata

2. **qr_code_utils.py** - Core QR code functionality
   - `generate_qr_code()` - Main QR generation with optional image embedding
   - `read_qrcode_from_file()` - QR code decoding from images
   - `get_wifi_details()` - Windows-specific Wi-Fi credential extraction
   - `create_wifi_qr()` - Wi-Fi QR code generation

### Key Dependencies
- `qrcode` - QR code generation library
- `pillow` - Image processing for embedding and filtering
- `pyzbar` - QR code reading/decoding

### Image Processing Pipeline
When embedding images in QR codes:
1. Convert to grayscale
2. Apply edge detection filter (optional, controlled by `--filter` flag)
3. Apply thresholding to create black/white outline
4. Resize to 1/4 of QR code dimensions
5. Paste in center of QR code

### Wi-Fi QR Code Format
Uses standard Wi-Fi QR format: `WIFI:S:{ssid};T:{encryption};P:{password};;`

## Development Notes

- The codebase is straightforward Python with minimal dependencies
- Error handling is basic but functional
- Wi-Fi functionality is Windows-specific (uses `netsh` commands)
- Image filtering is recommended to be disabled for B&W images with white backgrounds
- QR codes use high error correction to allow for image embedding