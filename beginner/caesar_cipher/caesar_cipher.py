#!/usr/bin/python3

from functions import caesar

more = True  # Initialize more to True
while more:
    direction = input("\nType 'E' for encrypt or 'D' for decrypt: ").upper()
    message = input("Enter message to encrypt: ")
    shift = int(input("Enter shift: "))
    new_msg = caesar(msg=message, shift=shift, direction=direction)

    print(f"New message: {new_msg}")

    more = input("Continue: y/n:  ").lower()

    if more == 'n':
        break  # Exit the loop if the user chooses to stop
    elif more != 'y':
        print("Invalid input")

