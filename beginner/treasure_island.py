#!/usr/bin/python3
# Treasure Island Game

message = """
-----------------------------------------
     Welcome to Treasure Island.
Your mission is to find the treasure.
-----------------------------------------
"""

print(message + "\n")

c1 = input("left or right: ")

if c1.lower() == 'left':
    c2 = input("swim or wait: ")
    if c2.lower() == 'wait':
        c3 = input("which door (yellow, red, blue): ")
        if c3.lower() == 'yellow':
            print("You Win!!")
        elif c3.lower() == 'red':
            print("Burned by fire. Game Over!!")
        elif c3.lower() == 'blue':
            print("Eaten by beasts. Game Over!!")
        else:
            print("Game Over!!")
    else:
        ms2 = """
------------------
Attacked by trout.
  Game Over!!
------------------
"""
        print(ms2)
else:
    ms1 = """
-----------------
Fall into a hole.
   Game over!!
-----------------
"""
    print(ms1)

