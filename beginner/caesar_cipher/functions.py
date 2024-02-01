#!/usr/bin/python3

import string

alphabet = string.ascii_letters + string.punctuation + string.digits

# Caesar cipher function
def caesar(msg, shift, direction):
    n_alpha = ""
    for i in msg:
        pos = alphabet.find(i)
        if i in alphabet:
            if direction.lower() == "e":
                n_pos = (pos + shift) % len(alphabet)
                n_alpha += alphabet[n_pos]
            elif direction.lower() == "d":
                n_pos = (pos - shift) % len(alphabet)
                n_alpha += alphabet[n_pos]
            else:
                print("Invalid Input")
        else:
            n_alpha += i
    return n_alpha
