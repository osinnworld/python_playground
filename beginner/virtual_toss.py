#!/usr/bin/python3
# This is a virtual coin toss program
import random

coin = input("Head or Tail: ")
toss = random.choice(['head', 'tail'])

print(f"Randomly produced: {toss}")

if coin.lower() == toss:
    print(f"{toss.capitalize()}, You Win!")
else:
    print(f"{toss.capitalize()}, You Lose!")

