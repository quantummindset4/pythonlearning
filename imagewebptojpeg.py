from PIL import Image

def convert_webp_to_jpeg(webp_path, jpeg_path):
    img = Image.open(webp_path)
    img.convert("RGB").save(jpeg_path, "JPEG")

# Example usage:
convert_webp_to_jpeg("/home/vempati/Downloads/fear1.webp", "/home/vempati/Downloads/fear1.jpg")

