from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Secret key generated and saved as 'secret.key'")

# Function to load the saved key
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("❌ 'secret.key' not found. Please generate a key first.")
        return None

# Function to encrypt a file
def encrypt_file(filename, key):
    try:
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(filename + ".enc", "wb") as encrypted_file:
            encrypted_file.write(encrypted)
        print(f"🔐 Encrypted: {filename} ➝ {filename}.enc")
    except Exception as e:
        print(f"❌ Error encrypting file: {e}")

# Function to decrypt a file
def decrypt_file(encrypted_filename, key):
    try:
        fernet = Fernet(key)
        with open(encrypted_filename, "rb") as file:
            encrypted_data = file.read()
        decrypted = fernet.decrypt(encrypted_data)
        original_filename = encrypted_filename.replace(".enc", "")
        with open(original_filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        print(f"🔓 Decrypted: {encrypted_filename} ➝ {original_filename}")
    except Exception as e:
        print(f"❌ Error decrypting file: {e}")

# Main menu loop
if __name__ == "__main__":
    print("""
==== Advanced Encryption Tool ====
1. Generate Key
2. Encrypt a File
3. Decrypt a File
4. Exit
""")

    choice = input("Select an option: ")

    if choice == '1':
        generate_key()

    elif choice == '2':
        key = load_key()
        if key:
            filename = input("Enter file name to encrypt (e.g. test.txt): ")
            encrypt_file(filename, key)

    elif choice == '3':
        key = load_key()
        if key:
            filename = input("Enter .enc file to decrypt: ")
            decrypt_file(filename, key)

    elif choice == '4':
        print("👋 Exiting.")

    else:
        print("⚠ Invalid choice")

    input("\nPress Enter to exit...")