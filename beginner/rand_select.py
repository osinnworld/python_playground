#!/usr/bin/python3
import random

names = []

while True:
	name = input("Names Please (type '=' to stop) ")
	if name == "=":
		break
	names.append(name)

if names:
	sel_name = random.choice(names)
	print("_"*40)
	print(f"{sel_name} is going to buy meal today.")
else:
	print("No names entered. Exiting the program")
