#!/usr/bin/python3
#user enter amount of a purchase, no. of instalments
p = float(input("enter amount of purchase: "))
n = int(input("enter no. of instalments: "))

#calculation
a = p * 1.05
i = a/n

#display
print("________________________________")
print(f"""Total Amount of Purchase: {a:,.2f}
 Instalments Cost: {i:,.2f}""")
