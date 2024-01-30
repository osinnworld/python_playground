#!/usr/bin/python3

from functions import decrypt, encrypt

# Main program
option = input("Type 'E' for encrypt or 'D' for decrypt: ").upper()

if option == 'E':
    message = input("Enter message to encrypt: ")
    shift = int(input("Enter shift: "))
    encrypted_msg = encrypt(message, shift)
    print("Encrypted message:", encrypted_msg)
elif option == 'D':
    message = input("Enter message to decrypt: ")
    shift = int(input("Enter shift: "))
    decrypted_msg = decrypt(message, shift)
    print("Decrypted message:", decrypted_msg)
else:
    print("Invalid input")

