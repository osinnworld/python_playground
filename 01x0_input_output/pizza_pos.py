#!/usr/bin/python3
from prettytable import PrettyTable

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

crust_prices = {
    'thin_crust': 100,
    'thick_crust': 150,
    'stuffed_crust': 200,
    'gluten_free_crust': 120
}

total_order_price = 0

while True:
    bill = 0
    selected_options = []

    size = input(f"\n:) Pizza Size(S/M/L) (Type 'EXIT' to end): ")

    if size.lower() == 'exit':
        break

    if size.lower() not in ['s', 'm', 'l']:
        print(":( Error: Invalid Input")
        continue

    crust = input("\nSelect crust option:\n1. Thin Crust\n2. Thick Crust\n3. Stuffed Crust\n4. Gluten-free Crust\nEnter the number: ")
    if crust.isdigit() and 1 <= int(crust) <= len(crust_prices):
        crust_option = list(crust_prices.keys())[int(crust) - 1]
        bill += crust_prices[crust_option]
        selected_options.append(f"Selected Crust: {crust_option.replace('_', ' ').title()} - KES{crust_prices[crust_option]:,.2f}")
    else:
        print(":( Error: Invalid Crust Option")
        continue

    if size.lower() == 's':
        bill += 800
        selected_options.append("Pizza Size: Small - KES800.00")
    elif size.lower() == 'm':
        bill += 1000
        selected_options.append("Pizza Size: Medium - KES1000.00")
    elif size.lower() == 'l':
        bill += 1500
        selected_options.append("Pizza Size: Large - KES1500.00")

    toppings_table = PrettyTable(['Topping Number', 'Topping Name', 'Price'])
    for key, value in topping_prices.items():
        toppings_table.add_row([key, value['name'].replace('_', ' ').title(), f"KES{value['price']:.2f}"])

    print("\nAvailable Toppings:")
    print(toppings_table)

    toppings = {}
    while True:
        topping_choice = input("\nEnter the number of a topping (Type 'DONE' when finished): ")
        if topping_choice.lower() == 'done':
            break
        elif topping_choice.isdigit() and 1 <= int(topping_choice) <= len(topping_prices):
            quantity = int(input("Enter the quantity: "))
            topping_info = topping_prices[int(topping_choice)]
            topping_name = topping_info['name']
            topping_price = topping_info['price'] * quantity
            bill += topping_price
            toppings[topping_name] = quantity
            selected_options.append(f"{topping_name.replace('_', ' ').title()} - KES{topping_price:,.2f} x {quantity}")
        else:
            print(":( Error: Invalid Topping")

    print("\nYour Order Summary:")
    for option in selected_options:
        print(option)
    print("________________________________")
    print(f"Total for this pizza: KES{bill:,.2f}")

    total_order_price += bill
    print(f"Running Total: KES{total_order_price:,.2f}")

print("\nThank you for ordering!")

