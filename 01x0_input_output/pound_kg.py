#!/usr/bin/python3
#user input
mass = float(input("Enter Mass in Pounds: "))

#pound to kg converter
KG = 0.454
kgs = mass * KG

#display
print(f"""
KG: {kgs:,.2f}""")
