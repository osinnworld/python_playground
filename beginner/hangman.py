#!/usr/bin/python3
import random

word_list = ["baboon", "camel", "pencil", "apple"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for i in chosen_word:
	if i == guess:
		print("right")
	else:
		print("wrong")
