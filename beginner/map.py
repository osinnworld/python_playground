#!/usr/bin/python3

import string

t = int(input("Enter Board Size: "))

letters = string.ascii_uppercase[:t] 

board = []
for _ in range(t):
    board.append(['_'] * t)

print(f"Please enter a letter between {letters[0]} and {letters[-1]} and a number between 1 and {t}")

input_x = input(f"Enter the X coordinate ({letters[0]}-{letters[-1]}): ").upper()
input_y = int(input(f"Enter the Y coordinate (1-{t}): ")) - 1

if input_x not in letters or input_y < 0 or input_y >= t:
    print("Invalid input")
else:
    board[input_y][letters.index(input_x)] = "X"
    print('\n'.join([' '.join(row) for row in board]))
