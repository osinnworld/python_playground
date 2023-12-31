#!/usr/bin/python3
#user input
sales = float(input("Enter Projected Amount of Total Sales: "))

#profit
PROFIT = 0.23
total_profit = sales * PROFIT

#display profit
print(f"""\nTotal Profit: {total_profit:,.2f}""")
