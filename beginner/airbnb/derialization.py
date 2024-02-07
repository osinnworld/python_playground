#!/usr/bin/python3

import json

# Load from the file
with open("data.json", "r") as json_file:
    # Iterate over each line in the file
    for line in json_file:
        # Load the JSON data into a Python dictionary
        data = json.loads(line)

        # Print each dictionary separately
        print(data)

