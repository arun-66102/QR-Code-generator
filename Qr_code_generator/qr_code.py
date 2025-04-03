import qrcode

def generate_qr(data, filename="qrcode.png"):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  
        border=4  
    )
    
    qr.add_data(data)  
    qr.make(fit=True)  

    # Generate QR code image
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the QR code
    img.save(filename)
    print(f"QR code saved as {filename}")

# Get user input
text = input("Enter text or URL for QR Code: ")
generate_qr(text)