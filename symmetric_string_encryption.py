from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a string using the provided key
def encrypt_string(key, text):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Decrypt an encrypted string using the provided key
def decrypt_string(key, encrypted_text):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

# Main function
def main():
    key = generate_key()
    print("Generated Key:", key.decode())

    text = input("Enter a string to encrypt: ")
    encrypted_text = encrypt_string(key, text)
    print("Encrypted Text:", encrypted_text.decode())

    decrypted_text = decrypt_string(key, encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
