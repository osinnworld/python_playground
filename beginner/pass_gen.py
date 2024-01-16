#!/usr/bin/python3

import string
from random import shuffle

chars = list(string.punctuation)
alphapets = list(string.ascii_letters)
digits = list(string.digits)

p1 = chars + alphapets + digits
shuffle(p1)
l = int(input("Enter Length of password: "))
password = ''.join(p1[:l])

print(password)
