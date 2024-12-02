import hashlib
import requests

def hash_password(password):
    """Hashes a password using SHA-1 and returns the hex digest in uppercase."""
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    return sha1

def check_password_pwned(password):
    """Checks if the password is breached using Have I Been Pwned API."""
    sha1_hash = hash_password(password)
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    
    # Request to the API with the prefix of the hash
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
    
    # Check if the suffix exists in the returned data
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)  # Return the breach count
    
    return 0  # Password not found in breach data

def main(file_path):
    """Reads a file of usernames and passwords, checks each password for breaches."""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    username, password = line.strip().split(',')
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

                breach_count = check_password_pwned(password)
                if breach_count > 0:
                    print(f"Username: {username}, Password Status: AT RISK ({breach_count} breaches)")
                else:
                    print(f"Username: {username}, Password Status: SAFE (not found in common breaches)")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

# Example usage
file_path = r"C:\Users\acer\Downloads\dp_prac\credentials.txt"  # Path to your credentials file
main(file_path)
