# Simple Icon Resizer

A lightweight Python utility designed to quickly resize a single source PNG image into the essential icon dimensions (`16x16`, `48x48`, and `128x128`) needed for browser extensions. It uses high-quality resampling to ensure your icons stay crisp and clear, outperforming many bulky online tools.

## Features
- Automatically generates all standard extension icon sizes (`16`, `48`, `128`).
- Uses high-quality Lanczos resampling for superior image scaling.
- Clean and straightforward command-line interface with no unnecessary bloat.

## Prerequisites

Before running the script, make sure you have Python installed on your system along with the **Pillow** library for image processing.

### Linux (e.g., Ubuntu, Debian, Kali)
Modern Linux distributions manage Python environments strictly. It is recommended to use a virtual environment:

1. Open your terminal in the project folder.
2. Create and activate the virtual environment, then install Pillow:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install Pillow
### Windows
Open Command Prompt or PowerShell in the project folder.

Install the required Pillow library directly:
pip install Pillow

### How to Use
Place your source PNG image (e.g., logo.png) in the same directory as the icon_converter.py script.
Run the script: python3 icon_converter.py
When prompted, type the exact file name of your source image (including the extension, like logo.png) and press Enter.
The script will instantly process your image and output icon16.png, icon48.png, and icon128.png right into your project folder.
your-project-folder/
│
├── icon_converter.py
├── logo.png  <-- Your source image
(After running the script)
your-project-folder/
│
├── icon_converter.py
├── logo.png
├── icon16.png
├── icon48.png
├── icon128.png

### Example as an image:
<img width="878" height="538" alt="image" src="https://github.com/user-attachments/assets/3864907c-1f5f-4fb3-b927-109a82acc532" />


