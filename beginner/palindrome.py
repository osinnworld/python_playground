#!/usr/bin/python3
word = input("Enter string: ")

# looping through the letters
l = len(word)
palindrome_flag = True

for i in range(l):
    if word[i] != word[l-1-i]:
        palindrome_flag = False
        break

print('_'*30)

if palindrome_flag:
    print("string is a palindrome")
else:
    print("string is NOT a palindrome")
