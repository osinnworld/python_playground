#!/usr/bin/python3

def circle(radius, pi=3.14):
    area = pi * radius**2
    circum = 2 * pi * radius
    return area, circum

def cost_sqm(area_sqm, cost):
    return area_sqm * cost

# Taking inputs for radius and cost per square meter
radius = float(input("Enter radius: "))
cost_per_sqm = float(input("Enter cost per sqm: "))

# Calculating area and cost
a, c = circle(radius)
total_cost = cost_sqm(a, cost_per_sqm)
total_cost = round(total_cost, 2)

print(f"Total cost: {total_cost}, area: {a} and circumference: {c}")

