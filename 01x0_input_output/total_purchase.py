#!/usr/bin/python3
#user price of item
n = []
n.append(float(input("Item No.1: ")))
n.append(float(input("Item No.2: ")))
n.append(float(input("Item No.3: ")))
n.append(float(input("Item No.4: ")))
n.append(float(input("Item No.5: ")))

#subtotal sale
subtotal = sum(n)
tax = 0.16 * subtotal
total = subtotal+tax
print("__________________________________")
#display
print(f"\nSubtotal of Sale: {subtotal:,.2f} \nSales Tax: {tax:,.2f} \nTotal: {total:,.2f}")
