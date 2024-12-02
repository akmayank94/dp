'''def load_dictionary(file_path):
    file_path = file_path.strip().strip('"').strip("'")  # Remove surrounding quotes
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return []
    
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()  # Read all words into a list
        return words
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
'''

import random
import string

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_password(word_list, num_words):
    password = ''.join(random.choice(word_list) for _ in range(num_words))

    # Ensure at least one uppercase, one lowercase, one digit, and one special character
    if not any(char.isupper() for char in password):
        password += random.choice(string.ascii_uppercase)
    if not any(char.islower() for char in password):
        password += random.choice(string.ascii_lowercase)
    if not any(char.isdigit() for char in password):
        password += random.choice(string.digits)
    if not any(char in string.punctuation for char in password):
        password += random.choice(string.punctuation)
    
    # Shuffle to randomize the password further
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)

def menu():
    print("1. Load words from dictionary")
    print("2. Generate password")
    print("3. Exit")

#if __name__ == "__main__":
    word_list = []
    
    while True:
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            file_path = input("Enter the dictionary file path: ")
            word_list = load_words(file_path)
            print("Words loaded successfully.")
        
        elif choice == 2:
            if word_list:
                num_words = int(input("Enter the number of words for the password: "))
                password = generate_password(word_list, num_words)
                print("Generated Password:", password)
            else:
                print("Please load the dictionary file first.")
        
        elif choice == 3:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

menu()
