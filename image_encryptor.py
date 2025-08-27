from PIL import Image

def encrypt_image(input_path, output_path):
    # Open the image file
    img = Image.open(input_path)
    pixels = img.load()  # Load the pixel data
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel

            # Apply encryption logic by modifying the RGB values
            r_new = (r + 50) % 256  # Shift red value
            g_new = (g + 100) % 256  # Shift green value
            b_new = (b + 150) % 256  # Shift blue value

            pixels[i, j] = (r_new, g_new, b_new)

    img.save(output_path)
    print(f"[✓] Image encrypted and saved as '{output_path}'")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel
            r_new = (r - 50) % 256  # Shift red value back
            g_new = (g - 100) % 256  # Shift green value back
            b_new = (b - 150) % 256  # Shift blue value back
            pixels[i, j] = (r_new, g_new, b_new)
    img.save(output_path)
    print(f"[✓] Image decrypted and saved as '{output_path}'")


def main():
    print("=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")
    input_path = input("Enter input image file name (with extension): ")
    output_path = input("Enter output image file name (with extension): ")

    # Perform the chosen operation
    if choice == '1':
        encrypt_image(input_path, output_path)
    elif choice == '2':
        decrypt_image(input_path, output_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Entry point of the program
if __name__ == "__main__":
    main()
