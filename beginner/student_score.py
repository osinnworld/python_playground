#!/usr/bin/python3

# input a list of student scores
ss = input("Enter Student Scores: ").split()
scores = [int(score) for score in ss]

# initialize max_score with the first score in the list
max_score = scores[0]

# find the highest score
for score in scores:
    if score > max_score:
        max_score = score

# display the highest score
print(f"The highest score in the class is: {max_score}")

