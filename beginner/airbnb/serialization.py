#!/usr/bin/python3

import json

# Data to be serialized
data = {
    "name": input("Enter name: "),
    "age": input("Enter age: "),
    "course": ["Maths", "History", "Computer Science"]
}

# Convert to JSON formatted string
json_string = json.dumps(data)
print(json_string)

# Save to a file
filename = "data.json"  # Specify the filename
with open(filename, "a") as json_file:
    json_file.write(json_string + '\n')  # Add a newline character after each JSON string

