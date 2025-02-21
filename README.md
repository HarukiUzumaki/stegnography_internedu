Overview:

Steganography is the practice of concealing information within other non-secret data, allowing for secure communication without drawing attention to the existence of the hidden message. This project aims to explore various techniques of steganography, providing tools and methods for embedding and extracting hidden messages in digital media such as images, audio files, and videos.

Features:
Image Steganography: Embed text messages within images using techniques like LSB (Least Significant Bit) manipulation.
Audio Steganography: Hide information within audio files by modifying the least significant bits of audio samples.
Video Steganography: Conceal messages in video files, leveraging both spatial and temporal redundancy.
User-Friendly Interface: A simple command-line interface (CLI) for easy interaction with the steganography tools.
Cross-Platform Compatibility: Works on Windows, macOS, and Linux.

Installation:
To get started with the project, clone the repository and install the required dependencies:
1. git clone https://github.com/HarukiUzumaki/stegnography_intern.git
2. cd steganography-project
3. pip install -r requirements.txt

Usage
Detailed instructions on how to use the tools will be provided in the documentation. Examples of embedding and extracting messages will be included to help users understand the functionality.

decrypt.py file:
 Example Usage

1. Run the script:
   ```bash
   python decrypt.py
   ```

2. Input the filename of the stego image when prompted:
   ```
   Enter stego image filename (with extension): example_image.png
   ```

3. Review the output for the extracted message or failure notification.

encrypt.py file:
### Input Prompts
- **Input Image Filename**: Provide the path to the image file you want to use for encryption.
- **Output Image Filename**: Specify the name for the output image file that will contain the encrypted message.
- **Secret Message**: Enter the message you want to hide in the image.


## Notes
- Ensure that the input image file exists and is accessible.
- The output image filename should not be empty.
- The secret message should not be empty.

