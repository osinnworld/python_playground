#!/usr/bin/python3

import string

# Function to encrypt the message
def encrypt(msg, shift):
    alphabet = string.ascii_letters + string.punctuation + string.digits
    n_alpha = ''
    for char in msg:
        if char in alphabet:
            pos = alphabet.index(char)
            n_pos = (pos + shift) % len(alphabet)
            n_alpha += alphabet[n_pos]
        else:
            n_alpha += char
    return n_alpha

# Function to decrypt the message
def decrypt(msg, shift):
    alphabet = string.ascii_letters + string.punctuation + string.digits
    n_alpha = ''
    for char in msg:
        if char in alphabet:
            pos = alphabet.index(char)
            n_pos = (pos - shift) % len(alphabet)
            n_alpha += alphabet[n_pos]
        else:
            n_alpha += char
    return n_alpha

