def caesar_cipher(text, shift, mode):
    result = ""

    # Loop through each character in the text
    for char in text:
        if char.isupper():  # Check if the character is an uppercase letter
            if mode == 1:  # Encryption mode
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 2:  # Decryption mode
                result += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():  # Check if the character is a lowercase letter
            if mode == 1:  # Encryption mode
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 2:  # Decryption mode
                result += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            result += char  # Non-alphabet characters are added unchanged

    return result

# Menu-driven implementation for Caesar Cipher
def caesar_menu():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))


        if choice == 1:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted Text: ", caesar_cipher(text, shift, 1))
            
        elif choice == 2:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted Text: ", caesar_cipher(text, shift, 2))
            
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")

# Call menu
caesar_menu()
