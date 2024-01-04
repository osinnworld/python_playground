#!/usr/bin/python3

# Number analyzer program

while True:
    # User input
    ui = input("\nEnter a number (type 'exit' to end): ")

    #check if user wants to exit
    if ui.lower() == 'exit':
        break

    try:
        n1 = float(ui)
        n = round(n1)

        #sorting
        print("________________________________________")

        if n > 0:
            print("Positive")
        elif n < 0:
            print("Negative")
        else:
            print("Zero")

        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except value_err:
        print("Invalid input. Please enter a valid number")

print("Program Terminated")

