#!/usr/bin/python3

# program title
title = "This is a Love Calculator"
print(f"/******{title:^30}******/")

# user input
male = input("Male Name: ")
female = input("Female Name: ")

c = (male + female).lower()

true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']

t = sum(true.count(c))
l = sum(love.count(c))

# display
print(f"Your love is: {t}{l} %")

