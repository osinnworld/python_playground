#!/usr/bin/python3

# Vowel Counter

# User input
sentence = input("Enter a sentence: ")

# Initialize vowel count
vowel_count = 0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a vowel (case-insensitive)
    if char.lower() in "aeiou":
        vowel_count += 1

# Display the result
print(f"The number of vowels in the sentence is: {vowel_count}")

