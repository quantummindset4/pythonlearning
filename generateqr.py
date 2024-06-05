# Install dependencies:
# pip install qrcode[pil]

import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bgcolor)
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter data to encode: ")
    color= input ("Enter which primary color you need:")
    bgcolor= input("Enter the background color you need:")
    filename = input("Enter filename to save QR code (with extension, e.g., example.png): ")
    generate_qr_code(data, filename)

