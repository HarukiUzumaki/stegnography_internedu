from PIL import Image
import os  # Added for file path validation

def encrypt_message(input_image, output_image, secret_message):
    """
    Encrypts a secret message into an image using LSB (Least Significant Bit) steganography.
    """
    if not os.path.isfile(input_image):
        print("Error: Input image file does not exist.")
        return
    if not output_image:
        print("Error: Output image filename cannot be empty.")
        return

    image = Image.open(input_image)
    encoded_image = image.copy()
    
    # Append a delimiter to mark the end of the message
    secret_message += "####"  # End delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    
    data_index = 0
    pixels = list(encoded_image.getdata())

    new_pixels = []
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify only RGB values (ignore Alpha if present)
            if data_index < len(binary_message):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[data_index])  # Modify LSB
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    # Update image with new pixel values
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_image)
    print(f"Message encrypted successfully into {output_image}")

if __name__ == "__main__":
    input_image = input("Enter input image filename (with extension): ")
    output_image = input("Enter output image filename (with extension): ")
    secret_message = input("Enter the secret message: ")
    if secret_message:  # Validate secret message is not empty
        encrypt_message(input_image, output_image, secret_message)
    else:
        print("Error: Secret message cannot be empty.")
