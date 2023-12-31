#!/usr/bin/python3
import time

def animate_text(text, delay=0.2):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# User input section
name = input("Enter name: ")
address = input("Enter address: ")
city = input("Enter city: ")
state = input("Enter state: ")
ZIP = input("Enter ZIP: ")
tel = input("Enter telephone number: ")
college = input("Enter college major: ")

# Animated print
print()
animate_text(f"Name: {name.upper()}\n")
animate_text(f"Address: {address.upper()}     City: {city.upper()}    State: {state.upper()}  ZIP: {ZIP}\n")
animate_text(f"Telephone Number: {tel}\n")
animate_text(f"College Major: {college.upper()}\n")

