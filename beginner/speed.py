#!/usr/bin/python3

def speed(distance, time):
    return distance / time

d = float(input("Enter distance (in km): "))
t = float(input("Enter time (in hours): "))

result_speed = speed(distance=d, time=t)
print("Speed:", result_speed, "km/h")

