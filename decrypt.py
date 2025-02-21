from PIL import Image
import os

def decrypt_message(encoded_image):
    """
    Extracts a hidden message from a stego-image.
    """
    if not os.path.isfile(encoded_image):
        print("Error: Encoded image file does not exist.")
        return False, ""

    image = Image.open(encoded_image)
    pixels = list(image.getdata())

    binary_message = ""
    for pixel in pixels:
        for i in range(3):  # Extract only RGB values
            binary_message += str(pixel[i] & 1)

    # Convert binary data to characters
    secret_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        secret_message += chr(int(byte, 2))
        if "####" in secret_message:  # Stop at delimiter
            break

    return True, secret_message.replace("####", "")  # Return success status and message

def main():
    encoded_image = input("Enter stego image filename (with extension): ")
    success, extracted_message = decrypt_message(encoded_image)
    if success:
        print(f"Extracted Message: {extracted_message}")
    else:
        print("Failed to extract message.")

if __name__ == "__main__":
    main()

