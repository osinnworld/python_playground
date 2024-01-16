#!/usr/bin/python3

# user input
user_input = input("Enter any number: ")

reversed_no = ''
for digit in user_input:
    reversed_no = digit + reversed_no

print(f"Reversed Number is: {int(reversed_no)}")

