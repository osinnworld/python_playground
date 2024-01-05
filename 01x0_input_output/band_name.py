#!/usr/bin/python3
print("# Welcome to the band name generator")

b = input("Your City: ")
c = input("Do you have a pet? (Type Y or N): ")

result = ""
if c.lower() == 'y':
    p = input("Name of Pet: ")
    result = b + p
    print(f"Your Band Name: {result}")
elif c.lower() == 'n':
    l = input("Your Middle Name: ")
    result = b + l
    print(f"Your Band Name: {result}")
else:
    print("Invalid input. Try again")
