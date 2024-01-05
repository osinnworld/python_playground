#!/usr/bin/python3

print(":) Welcome to the tip calculator\n")

bill = float(input("Total Bill: $"))
people = int(input("People to split the bill: "))

tip = input("Percentage would you like to give: 10, 12, or 15: ")


if tip == '10':
	t_bill = bill*1.10
elif tip == '12':
	t_bill = bill*1.12
elif tip == '15':
	t_bill = bill*1.15
else:
	print("invalid input\n")

person = t_bill/people
print(f"Each person should pay: ${person:,.2f}")	
