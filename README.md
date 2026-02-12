PRODIGY_TrackCode_Task2
🔐 Image Encryption Tool

A simple yet powerful Python utility for encrypting and decrypting images using a numeric key-based cipher. Preserve your visual privacy with ease!
📋 Features

    ✅ Encrypt Images: Secure your images with a numeric encryption key
    ✅ Decrypt Images: Restore encrypted images to their original state
    ✅ Multi-Format Support: Works seamlessly with PNG and JPG formats
    ✅ Alpha Channel Support: Preserves transparency in RGBA images
    ✅ User-Friendly CLI: Interactive command-line interface for easy operation
    ✅ Cross-Platform: Works on Windows, macOS, and Linux

🚀 Quick Start
Prerequisites

Ensure you have Python 3.6+ installed and the required dependency:

Installation

1.Clone this repository:

git clone https://github.com/Shamirali/image-encryption-tool.git
cd image-encryption-tool

2.Install dependencies:

pip install -r requirements.txt

Usage

Run the tool with:

python image_encryption.py

Follow the interactive prompts:

    Choose an option: Select 1 to encrypt or 2 to decrypt
    Input image path: Provide the path to your image file
    Output image path: Specify where to save the processed image (include .png or .jpg)
    Encryption key: Enter a numeric key (e.g., 42, 123, etc.)

Example

===== Image Encryption Tool (PNG + JPG Supported) =====
1. Encrypt Image
2. Decrypt Image
Choose option (1/2): 1
Enter input image path: original.jpg
Enter output image path (include .png or .jpg): encrypted.jpg
Enter encryption key (number): 42
✅ Encrypted image saved as encrypted.jpg

🔬 How It Works

Encryption Algorithm

The tool uses a simple modular arithmetic cipher that shifts RGB color values:

    Each pixel is processed individually
    RGB channels are shifted by the encryption key value (modulo 256)
    Alpha channel (if present) remains unchanged for transparency preservation
    Formula: encrypted_value = (original_value + key) % 256

Decryption Algorithm

Reverses the encryption process:

    Formula: decrypted_value = (original_value - key) % 256

Note: For maximum security, use different images and keys. This method is suitable for casual privacy but not for critical security applications. 📁 Project Structure


image-encryption-tool/
├── image_encryption.py    # Main script
├── requirements.txt       # Python dependencies
└── README.md             # This file

🛠️ Requirements

    Pillow (PIL) - Python Imaging Library for image processing

Install via:

pip install pillow

💡 Examples

Encrypt an Image

python image_encryption.py
# Choose: 1
# Input: /path/to/photo.jpg
# Output: /path/to/photo_encrypted.jpg
# Key: 123

Decrypt an Image

python image_encryption.py
# Choose: 2
# Input: /path/to/photo_encrypted.jpg
# Output: /path/to/photo_decrypted.jpg
# Key: 123  (must be the same key used for encryption)

⚠️ Important Notes

    Keep your key safe: Without the correct encryption key, you cannot recover the original image
    Same key required: Use the identical key for both encryption and decryption
    Supported formats: PNG, JPG (JPEG)
    Transparency: RGBA images maintain their alpha channel during encryption/decryption
    Not cryptographically secure: This tool is for basic image obfuscation, not military-grade security

🔮 Future Enhancements

    Add support for additional image formats (BMP, GIF, TIFF)
    Implement stronger encryption algorithms
    Add batch processing for multiple images
    Create a GUI version for better user experience
    Add password-based key generation
    Support for image watermarking

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🤝 Contributing

Contributions are welcome! Feel free to:

    Report bugs or suggest features via Issues
    Submit pull requests for improvements
    Share your ideas and feedback

👨‍💻 Author

Shamirali

GitHub:@Shamirali
📞 Support

If you encounter any issues or have questions, please:

1.Check the Issues page 2.Create a new issue with detailed information about your problem 3.Include error messages and reproduction steps

Happy encrypting! 🔐✨



## 📋 Additional Files to Consider

I also recommend creating a `requirements.txt` file:

```txt name=requirements.txt
Pillow>=9.0.0
