#!/usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = ["rock", "paper", "scissors"]

computer = random.choice(options)
player = input("Enter your choice (rock, paper, scissors): ").lower()

print(f"\nPlayer ({player}):")
if player == "rock":
    print(rock)
elif player == "paper":
    print(paper)  
elif player == "scissors":
    print(scissors)

print(f"\nComputer ({computer}):")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
else:
    print(scissors)
    
if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("Player wins!")
elif player == "paper" and computer == "rock":
    print("Player wins!")
elif player == "scissors" and computer == "paper":
    print("Player wins!")
else:
    print("Computer wins!")
