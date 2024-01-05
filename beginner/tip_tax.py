#!/usr/bin/python3

# User input for food charge
m = float(input("Enter Food Charge: "))

# Calculation
t = m * 0.18
tax = m * 0.07
a = m + t + tax

# Output
print("___________________________________")
print(f"Total Tip: {t:,.2f}\nTotal Tax: {tax:,.2f}\nTotal Charge: {a:.2f}")

