from PIL import Image
import os


def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)

    # Convert based on image mode
    if image.mode == "RGBA":
        has_alpha = True
        image = image.convert("RGBA")
    else:
        has_alpha = False
        image = image.convert("RGB")

    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):

            if has_alpha:
                r, g, b, a = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b, a)
            else:
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"✅ Encrypted image saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)

    if image.mode == "RGBA":
        has_alpha = True
        image = image.convert("RGBA")
    else:
        has_alpha = False
        image = image.convert("RGB")

    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):

            if has_alpha:
                r, g, b, a = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b, a)
            else:
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"✅ Decrypted image saved as {output_path}")


def main():
    print("===== Image Encryption Tool (PNG + JPG Supported) =====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Choose option (1/2): ").strip()
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path (include .png or .jpg): ").strip()

    try:
        key = int(input("Enter encryption key (number): "))
    except ValueError:
        print("❌ Key must be a number.")
        return

    if not os.path.exists(input_path):
        print("❌ Input file not found.")
        return

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
