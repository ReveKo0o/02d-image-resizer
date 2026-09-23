from PIL import Image
import os

def resize_icon(input_image_path):
    try:
        img = Image.open(input_image_path)
        sizes = [16, 48, 128]
        
        for size in sizes:
            img_resized = img.resize((size, size), Image.Resampling.LANCZOS)
            output_name = f"icon{size}.png"
            img_resized.save(output_name, "PNG")
            print(f"[SUCCESS] {output_name} has been created.")
            
    except Exception as e:
        print(f"[ERROR] An issue occurred: {e}")

if __name__ == "__main__":
    print("--- Automatic Icon Resizer ---")
    file_name = input("Enter the source PNG file name with extension (e.g., logo.png): ").strip()
    
    if os.path.exists(file_name):
        resize_icon(file_name)
    else:
        print("[ERROR] The specified file was not found in this directory!")
