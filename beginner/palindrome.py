#!/usr/bin/python3

def check_palindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l-1-i]:
            return False
    return True

word = input("Enter string: ")

print('_'*40)

if check_palindrome(word):
    print("String is a palindrome")
else:
    print("String is NOT a palindrome")

