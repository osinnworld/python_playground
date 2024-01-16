#!/usr/bin/python3

user_input = input('Enter range of numbers, e.g., (1-100): ')
user_range = user_input.split('-')

# Ensure the input is valid
if len(user_range) != 2:
    print("Invalid input. Please provide a range in the format (start-end).")
else:
    first = int(user_range[0])
    last = int(user_range[1])

    total_even = 0

    for i in range(first, last + 1):
        if i % 2 == 0:
            total_even += i

    print(f"Total Even Numbers within {first}-{last}: {total_even}")

