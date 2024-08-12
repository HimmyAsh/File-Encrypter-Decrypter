import os
from cryptography.fernet import Fernet

# Generate encryption key
def generate_key():
    return Fernet.generate_key()

# Save the encryption key 
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt the file 
def encrypt_file(input_file, encrypted_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(encrypted_file, 'wb') as file:
        file.write(encrypted_data)

    # Delete the original file after encryption
    os.remove(input_file)

# Decrypt file to restore original content
def decrypt_file(encrypted_file, decrypted_file, key):
    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(decrypted_file, 'wb') as file:
        file.write(decrypted_data)

# Main function to handle user input and operations
def main():
    key_file = 'encryption_key.key'
    
    # Check if the key already exists
    if os.path.exists(key_file):
        key = load_key(key_file)
    else:
        key = generate_key()
        save_key(key, key_file)
    
    encrypted_file = 'encrypted_file.txt'
    
    if not os.path.exists(encrypted_file):
        # Get the input file from the user
        input_file = input('What is the file you want to encrypt?: ')
        
        # Encrypt the file
        encrypt_file(input_file, encrypted_file, key)
        print(f"File '{input_file}' encrypted to '{encrypted_file}' and the original file has been removed.")
    else:
        print(f"An encrypted file '{encrypted_file}' already exists.")
    
    # Ask the user if they want to decrypt the file to restore the original content
    user_input = input("Do you want to decrypt the file to restore the original content? (yes/no): ").strip().lower()

    if user_input == 'yes':
        decrypted_file = input('Enter the name for the restored file (e.g., original_file.txt): ')
        decrypt_file(encrypted_file, decrypted_file, key)
        print(f"File '{encrypted_file}' decrypted and restored as '{decrypted_file}'")
        os.remove(encrypted_file)
        
    else:
        print("Decryption skipped. The original file remains encrypted.")

if __name__ == "__main__":
    main()
