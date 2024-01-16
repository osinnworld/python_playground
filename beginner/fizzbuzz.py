#!/usr/bin/python3

user = input("enter range: e.g 1-100: ").split('-')

if len(user) != 2:
	print("Invalid Input")
else:
	first = int(user[0])
	last = int(user[1])
	for i in range(first, last + 1):
		if i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		elif i % 3 == 0 and 1 % 5 == 0:
			print(FizzBuzz)
		else:
			print(i)
