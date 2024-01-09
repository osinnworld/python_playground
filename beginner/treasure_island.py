#!/usr/bin/python3
# Treasure Island Game with Inventory System, Point System, and Save/Load Features

message = """
-----------------------------------------
     Welcome to Treasure Island.
Your mission is to find the treasure.
You find yourself on an island with two paths.
Choose wisely to reach the treasure!
-----------------------------------------
"""

inventory = []
points = 0
c_location = "start"

def disp_inv():
    print("\nInventory: ", inventory)

def add_inv(item):
    inventory.append(item)
    print(f"\nYou picked up a {item}.")

def up_location(new_location):
    global c_location
    c_location = new_location

def mv_location(location):
    up_location(location)
    print(f"\nYou have moved to {location}.")

def use_key():
    if "key" in inventory:
        print("\nYou unlocked the door.")
        return True
    else:
        print("\nYou don't have the key.")
        return False

def use_map():
    if "map" in inventory:
        print("\nYou used the map to navigate the maze successfully.")
        return True
    else:
        print("\nYou don't have a map.")
        return False

def earn_points(earned_points):
    global points
    points += earned_points
    print(f"\nYou earned {earned_points} points. Total Points: {points}")

def save_game():
    with open("save_game.txt", "w") as file:
        file.write(f"{c_location},{points}")
    print("\nGame saved.")

def load_game():
    global c_location, points
    try:
        with open("save_game.txt", "r") as file:
            data = file.readline().split(',')
            c_location = data[0]
            points = int(data[1])
        print("\nGame loaded.")
    except FileNotFoundError:
        print("\nNo saved game found.")

def start_game():
    print(message + "\n")

def continue_game():
    print("\nOptions:")
    print("1. Continue the game")
    print("2. Save and Quit")
    print("3. Load Game\n")
    choice = input("Choose an option (1/2/3): ")
    return choice

def left_path():
    global c_location
    print("\nYou chose the left path. As you walk, you encounter a river.")
    c2 = input("Do you want to 'swim' across or 'wait' for a boat? ")

    if c2.lower() == 'wait':
        print("\nA boat arrives and takes you to the other side of the river.")
        mv_location("door_room")
        earn_points(10)

    else:
        print("\nYou decide to swim across the river.")
        print("Uh-oh! You're attacked by a school of hungry trout. Game Over!!")
        c_location = "game_over"

def right_path():
    global c_location
    print("\nYou chose the right path and fall into a deep hole.")
    add_inv("key")
    mv_location("hole_room")

def hole_room():
    global c_location
    print("You find a key and a ladder. What do you want to do?")
    c4 = input("Type 'take key' or 'climb ladder': ")

    if c4.lower() == 'take key':
        add_inv("key")
        earn_points(5)
        print("\nYou took the key. You find a locked door.")
        c5 = input("Do you want to 'unlock' the door or 'climb ladder': ")

        if c5.lower() == 'unlock':
            if use_key():
                mv_location("mirror_room")
                earn_points(10)

        elif c5.lower() == 'climb ladder':
            mv_location("troll_bridge")

        else:
            print("\nInvalid choice. Please enter 'unlock' or 'climb ladder'.")

    elif c4.lower() == 'climb ladder':
        print("\nYou climbed the ladder. You find a dark cave with two paths - 'left' or 'right'.")
        mv_location("cave_room")

    else:
        print("\nInvalid choice. Please enter 'take key' or 'climb ladder'.")


def color_door_room():
    global c_location
    print("\nYou find another door - 'green' or 'purple'.")
    c7 = input("Which door do you choose: ")

    if c7.lower() == 'green':
        earn_points(35)
        print("\nYou opened the green door and found the treasure! You Win!!")
        c_location = "game_over"

    elif c7.lower() == 'purple':
        print("\nYou entered a room with a riddle. Solve it to proceed.")
        riddle_answer = input("What has a heart that doesn't beat? ")

        if riddle_answer.lower() == 'artichoke':
            earn_points(25)
            print("\nCorrect! You may proceed. You find the treasure. You Win!!")
            c_location = "game_over"

        else:
            print("\nIncorrect! The room closes in on you. Game Over!!")
            c_location = "game_over"

    else:
        print("\nInvalid choice. Please enter 'green' or 'purple'.")
        c_location = "game_over"

def door_room():
    global c_location
    print("\nYou find three doors in front of you - one 'yellow', one 'red', and one 'blue'.")
    c3 = input("Which door do you choose: ")

    if c3.lower() == 'yellow':
        earn_points(50)
        print("\nCongratulations! You found the treasure! You Win!!")
        c_location = "game_over"

    elif c3.lower() == 'red':
        print("\nOh no! The door bursts into flames. You got burned. Game Over!!")
        c_location = "game_over"

    elif c3.lower() == 'blue':
        print("\nA pack of beasts is waiting behind the door. You got eaten. Game Over!!")
        c_location = "game_over"

    else:
        print("\nYou hesitated and a trapdoor opens beneath you. You fall. Game Over!!")
        c_location = "game_over"

def game_over():
    global c_location
    print("\nGame Over. Better luck next time!")
    c_location = "game_over"

def main():
    start_game()

    while True:
        choice = continue_game()

        if choice == '1':
            if c_location == "start":
                c1 = input("Left or Right: ")

                if c1.lower() == 'left':
                    left_path()

                elif c1.lower() == 'right':
                    right_path()

                else:
                    print("\nInvalid choice. Please enter 'left' or 'right'.")

            elif c_location == "hole_room":
                hole_room()

            elif c_location == "mirror_room":
                mirror_room()

            elif c_location == "troll_bridge":
                troll_bridge()

            elif c_location == "cave_room":
                cave_room()

            elif c_location == "dragon_door_room":
                dragon_door_room()

            elif c_location == "color_door_room":
                color_door_room()

            elif c_location == "door_room":
                door_room()

            elif c_location == "game_over":
                game_over()
                break

        elif choice == '2':
            save_game()
            break

        elif choice == '3':
            load_game()

        else:
            print("\nInvalid choice. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()

                                               
