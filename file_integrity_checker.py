import hashlib
import os
import json

def get_file_hash(filename):
    sha256 = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_and_store(directory, hash_file='hashes.json'):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(oot, file)
            file_hash = get_file_hash(path)
            if file_hash:
                hashes[path] = file_hash
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(" Initial hashes saved.")

def check_integrity(hash_file='hashes.json'):
    with open(hash_file, 'r') as f:
        saved_hashes = json.load(f)
    
    for filepath, old_hash in saved_hashes.items():
        current_hash = get_file_hash(filepath)
        if current_hash is None:
            print(f"⚠ File deleted: {filepath}")
        elif current_hash != old_hash:
            print(f" File modified: {filepath}")
        else:
            print(f"✔ Unchanged: {filepath}")

if __name__ == "__main__":
    print("1. Scan and store hashes")
    print("2. Check file integrity")
    choice = input("Choose option (1 or 2): ")

    folder = input("Enter folder path to monitor: ").strip()

    if choice == '1':
        scan_and_store(folder)
    elif choice == '2':
        check_integrity()
    else:
        print("Invalid choice.")