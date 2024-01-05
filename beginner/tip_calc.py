#!/usr/bin/python3

print("Welcome to the tip calculator\n")

try:
    bill = float(input("Total Bill: $"))
    people = int(input("People to split the bill: "))

    tip = input("Percentage would you like to give: 10, 12, or 15: ")

    if tip in ['10', '12', '15']:
        t_bill = bill * (1 + int(tip) / 100)
        person = t_bill / people
        print('_' * 50)
        print(f"Each person should pay: ${person:,.2f}")
    else:
        print("Invalid input for tip percentage. Please enter 10, 12, or 15.")

except ValueError:
    print("Invalid input for bill or number of people. Please enter valid numerical values.")

