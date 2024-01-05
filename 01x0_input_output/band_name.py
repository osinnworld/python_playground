#!/usr/bin/python3

import random

print("# Welcome to the band name generator")

b = input("Your City: ")
c = input("Do you have a pet? (Type Y or N): ")

result = ""

if c.lower() == 'y':
    p = input("Name of Pet: ")
    result = b + p
else:
    l = input("Your Middle Name: ")
    result = b + l

# Additional customization options
color = input("Your Favorite Color: ")
food = input("Your Favorite Food: ")
hobby = input("Your Hobby: ")

# Incorporate additional customization
result += color + food + hobby

# Random words
options = ["Groovy", "Electric", "Funky", "Galactic", "Cosmic", "Revolution", "Echo", "Sonic"]
random_wd = random.choice(options)

# Mix random words
result += random_wd

print(f"Your Band Name: {result}")

