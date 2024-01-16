#!/usr/bin/python3

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end = False
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
length = len(word)


lives = 6


print(f'Pssst, the solution is {word}.')


display = ["_" for i in range(length)]

while not end:
    guess = input("Guess a letter: ").lower()

    correct_guess = False
    for index in range(length):
        letter = word[index]
        if letter == guess:
            display[index] = letter
            correct_guess = True

    if not correct_guess:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")
        if lives == 0:
            end = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end = True
        print("You win.")

    print(stages[lives])

