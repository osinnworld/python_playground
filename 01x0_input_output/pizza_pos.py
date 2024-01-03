#!/usr/bin/python3

topping_prices = {
    1: {'name': 'pepperoni', 'price': 300},
    2: {'name': 'extra_cheese', 'price': 400},
    3: {'name': 'mushrooms', 'price': 200},
    4: {'name': 'onions', 'price': 150},
    5: {'name': 'bell_peppers', 'price': 250},
    6: {'name': 'italian_sausage', 'price': 350},
    7: {'name': 'black_olives', 'price': 200},
    8: {'name': 'pineapple', 'price': 300}
}

while True:
    bill = 0

    size = input(f"\n:) Pizza Size(S/M/L) (Type 'EXIT' to end): ")

    if size.lower() == 'exit':
        break

    if size.lower() not in ['s', 'm', 'l']:
        print(":( Error: Invalid Input")
        continue

    if size.lower() == 's':
        bill += 800
        print(f"Small Pizza: KES{bill:,.2f}")
    elif size.lower() == 'm':
        bill += 1000
        print(f"Medium Pizza: KES{bill:,.2f}")
    elif size.lower() == 'l':
        bill += 1500
        print(f"Large Pizza: KES{bill:,.2f}")

    toppings = {}
    while True:
        print("\nAvailable Toppings:")
        for key, value in topping_prices.items():
            print(f"{key}. {value['name'].replace('_', ' ').title()} - KES{value['price']:.2f}")

        topping_choice = input("\nEnter the number of a topping (Type 'DONE' when finished): ")
        if topping_choice.lower() == 'done':
            break
        elif topping_choice.isdigit() and 1 <= int(topping_choice) <= len(topping_prices):
            quantity = int(input("Enter the quantity: "))
            toppings[topping_choice] = quantity
        else:
            print(":( Error: Invalid Topping")

    for topping_choice, quantity in toppings.items():
        topping_info = topping_prices[int(topping_choice)]
        topping_name = topping_info['name']
        topping_price = topping_info['price'] * quantity
        bill += topping_price
        print(f"Add {quantity} {topping_name.replace('_', ' ').title()}: KES{topping_price:,.2f}")

    print("________________________________")
    print(f"Total: KES{bill:,.2f}")

