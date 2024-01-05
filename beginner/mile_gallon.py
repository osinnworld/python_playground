#!/usr/bin/python3
#user input
m = float(input("Enter Miles Driven: "))
g = float(input("Enter Gas Used: "))

#calculation
MPG = m/g

#output
print("________________________________")
print(f"MPG: {MPG:,.2f}")
