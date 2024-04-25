# Function to encrypt a message
def encrypt(message, key):
    encrypted_message = ''
    key_index = 0
    for char in message:
        key_char = key[key_index % len(key)]
        shifted_char = chr((ord(char) + ord(key_char)) % 127)  # Restricting to printable ASCII characters
        encrypted_message += shifted_char
        key_index += 1
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, key):
    decrypted_message = ''
    key_index = 0
    for char in encrypted_message:
        key_char = key[key_index % len(key)]
        shifted_char = chr((ord(char) - ord(key_char)) % 127)  # Restricting to printable ASCII characters
        decrypted_message += shifted_char
        key_index += 1
    return decrypted_message

# Main function
def main():
    while True:
        print("Options:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            key = input("Enter the encryption key: ")
            encrypted_message = encrypt(message, key)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            encrypted_message = input("Enter the encrypted message to decrypt: ")
            key = input("Enter the decryption key: ")
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main(
