#!/usr/bin/python3
# Treasure Island Game

message = """
-----------------------------------------
     Welcome to Treasure Island.
Your mission is to find the treasure.
You find yourself on an island with two paths.
Choose wisely to reach the treasure!
-----------------------------------------
"""

print(message + "\n")

c1 = input("Left or Right: ")

if c1.lower() == 'left':
    print("\nYou chose the left path. As you walk, you encounter a river.")
    c2 = input("Do you want to 'swim' across or 'wait' for a boat? ")
    if c2.lower() == 'wait':
        print("\nA boat arrives and takes you to the other side of the river.")
        print("You find three doors in front of you - one 'yellow', one 'red', and one 'blue'.")
        c3 = input("Which door do you choose: ")
        if c3.lower() == 'yellow':
            print("\nCongratulations! You found the treasure! You Win!!")
        elif c3.lower() == 'red':
            print("\nOh no! The door bursts into flames. You got burned. Game Over!!")
        elif c3.lower() == 'blue':
            print("\nA pack of beasts is waiting behind the door. You got eaten. Game Over!!")
        else:
            print("\nYou hesitated and a trapdoor opens beneath you. You fall. Game Over!!")
    else:
        ms2 = """
------------------
You decide to swim across the river.
Uh-oh! You're attacked by a school of hungry trout.
Game Over!!
------------------
"""
        print(ms2)
else:
    print("\nYou chose the right path and fall into a deep hole.")
    print("You find a key and a ladder. What do you want to do?")
    c4 = input("Type 'take key' or 'climb ladder': ")

    if c4.lower() == 'take key':
        print("\nYou took the key. You find a locked door.")
        c5 = input("Do you want to 'unlock' the door or 'climb ladder': ")

        if c5.lower() == 'unlock':
            print("\nThe door opens to a room with a giant mirror. You see a code written on the mirror.")
            c6 = input("Do you want to 'memorize' the code or 'ignore' it: ")

            if c6.lower() == 'memorize':
                print("\nYou memorized the code. Continuing your journey.")
                print("You find another door - 'green' or 'purple'.")
                c7 = input("Which door do you choose: ")

                if c7.lower() == 'green':
                    print("\nYou opened the green door and found the treasure! You Win!!")
                elif c7.lower() == 'purple':
                    print("\nYou entered a room with a riddle. Solve it to proceed.")
                    riddle_answer = input("What has a heart that doesn't beat? ")
                    
                    if riddle_answer.lower() == 'artichoke':
                        print("\nCorrect! You may proceed. You find the treasure. You Win!!")
                    else:
                        print("\nIncorrect! The room closes in on you. Game Over!!")

                else:
                    print("\nYou hesitated and a trapdoor opens beneath you. You fall. Game Over!!")

            else:
                print("\nYou ignored the code and opened the door without entering the code.")
                print("The room is filled with poisonous gas. Game Over!!")

        else:
            print("\nYou climbed the ladder instead of unlocking the door.")
            print("You find a bridge with a troll guarding it. Solve a riddle to pass.")
            troll_riddle = input("What has keys but can't open locks? ")

            if troll_riddle.lower() == 'piano':
                print("\nThe troll lets you pass. Continuing your journey.")
                print("You find another door - 'orange' or 'brown'.")
                c8 = input("Which door do you choose: ")

                if c8.lower() == 'orange':
                    print("\nYou opened the orange door and found the treasure! You Win!!")
                elif c8.lower() == 'brown':
                    print("\nYou entered a room with a maze. Navigate through the maze to find the treasure.")
                    maze_choice = input("Navigate 'left' or 'right': ")

                    if maze_choice.lower() == 'right':
                        print("\nCongratulations! You successfully navigated the maze and found the treasure. You Win!!")
                    else:
                        print("\nYou got lost in the maze. Game Over!!")

                else:
                    print("\nYou hesitated and a trapdoor opens beneath you. You fall. Game Over!!")

            else:
                print("\nThe troll is not satisfied with your answer. Game Over!!")

    elif c4.lower() == 'climb ladder':
        print("\nYou climbed the ladder. You find a dark cave with two paths - 'left' or 'right'.")
        c9 = input("Which path do you choose: ")

        if c9.lower() == 'left':
            print("\nYou chose the left path and find a magical portal.")
            print("The portal transports you to the treasure room. You Win!!")
        elif c9.lower() == 'right':
            print("\nYou chose the right path and encounter a dragon.")
            print("You can try to 'fight' the dragon or 'run' away: ")
            dragon_choice = input()

            if dragon_choice.lower() == 'fight':
                print("\nYou fought the dragon bravely but got burnt. Game Over!!")
            elif dragon_choice.lower() == 'run':
                print("\nYou ran away from the dragon successfully.")
                print("You find a door - 'silver' or 'gold'.")
                c10 = input("Which door do you choose: ")

                if c10.lower() == 'silver':
                    print("\nYou opened the silver door and found the treasure! You Win!!")
                elif c10.lower() == 'gold':
                    print("\nYou entered a room with a maze. Navigate through the maze to find the treasure.")
                    maze_choice = input("Navigate 'left' or 'right': ")

                    if maze_choice.lower() == 'right':
                        print("\nCongratulations! You successfully navigated the maze and found the treasure. You Win!!")
                    else:
                        print("\nYou got lost in the maze. Game Over!!")

                else:
                    print("\nYou hesitated and a trapdoor opens beneath you. You fall. Game Over!!")

            else:
                print("\nYou hesitated and the dragon attacked you. Game Over!!")

        else:
            print("\nYou hesitated and fell into a pit. Game Over!!")

    else:
        print("\nYou hesitated and the ladder broke. Game Over!!")


