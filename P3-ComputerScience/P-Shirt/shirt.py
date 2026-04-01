import sys
import os
from PIL import Image, ImageOps

PATH = os.path.dirname(__file__)
SHIRT_PATH = os.path.join(PATH, "shirt.png")
ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

def main():
    # Validate command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py input_image output_image")
        sys.exit(1)
    
    input_img_path = os.path.join(PATH, sys.argv[1])
    output_img_path = os.path.join(PATH, sys.argv[2])
    
    if not input_img_path.lower().endswith(ALLOWED_EXTENSIONS):
        print("Error: Input file must be a .jpg, .jpeg, or .png image.")
        sys.exit(1)

    if not input_img_path.split('.')[1].lower() == output_img_path.split('.')[1].lower():
        print("Error: Input and output file extensions must match.")
        sys.exit(1)

    try:
        input_img = Image.open(input_img_path)
    except FileNotFoundError:
        print(f"Error: File '{input_img_path}' not found.")
        sys.exit(1)
    

    # Resize input image to fit shirt template
    shirt_img = Image.open(SHIRT_PATH)
    input_img = ImageOps.fit(input_img, shirt_img.size)

    # Overlay the shirt template onto the input image using Image.paste()
    input_img.paste(shirt_img, (0, 0), shirt_img)

    # Save the resulting image
    input_img.save(output_img_path)
    

if __name__ == "__main__":
    main()