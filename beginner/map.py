#!/usr/bin/python3

t = int(input("Enter Table Size: "))
l1 = ['_,' * t]

l2 = l1 * t

print('\n'.join(map(str, l2)))


