import os
from PIL import Image

def convert_webp_to_jpeg_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            # Construct paths for input and output files
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
            
            # Convert the WebP file to JPEG
            img = Image.open(input_path)
            img.convert("RGB").save(output_path, "JPEG")

# Example usage:
convert_webp_to_jpeg_folder("/home/vempati/Downloads/dalle", "/home/vempati/Downloads/dallejpg")

