import itertools
import string

def brute_force(password):
    characters = string.ascii_lowercase  # Characters to try (you can add more)

    attempts = 0
    for length in range(1, len(password) + 1):  # Try different lengths
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(f"Trying: {guess}")
            if guess == password:
                print(f"Password found: {guess}")
                print(f"Total attempts: {attempts}")
                return guess
    print("Password not found.")
    return None

# Get the target password from the user
password = input("Enter the password to brute force: ")
brute_force(password)

