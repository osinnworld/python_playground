#!/usr/bin/python3

# user input
heights = input("Enter Heights: ").split()
# Convert each height from string to integer
heights = [int(height) for height in heights]

# calculation
total_height = 0
num_students = len(heights)

for height in heights:
    total_height += height

average_height = total_height / num_students

# display
print(f"\nTotal Height: {total_height}")
print(f"Number of Students: {num_students}")
print(f"Average Height: {average_height}")

