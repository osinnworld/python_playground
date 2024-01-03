#!/usr/bin/python3
from prettytable import PrettyTable

toppings = {
    1: {'name': 'pepperoni', 'price': 300},
    2: {'name': 'extra_cheese', 'price': 400},
    3: {'name': 'mushrooms', 'price': 200},
    4: {'name': 'onions', 'price': 150},
    5: {'name': 'bell_peppers', 'price': 250},
    6: {'name': 'italian_sausage', 'price': 350},
    7: {'name': 'black_olives', 'price': 200},
    8: {'name': 'pineapple', 'price': 300}
}

crusts = {
    'thin': 100,
    'thick': 150,
    'stuffed': 200,
    'gluten_free': 120
}

sizes = {
    's': 800,
    'm': 1000,
    'l': 1500
}

total = 0

def get_input(prompt):
    while True:
        choice = input(f"\n{prompt} Pizza Size(S/M/L) ('exit' to end): ")
        if choice.lower() == 'exit' or choice.lower() in ['s', 'm', 'l']:
            return choice.lower()
        else:
            print("Error: Invalid Input")

def display_error():
    print("Error: Invalid Input")

while True:
    bill = 0
    options = []

    size = get_input("Choose a")

    if size == 'exit':
        break

    crust = input("\nSelect crust:\n1. Thin\n2. Thick\n3. Stuffed\n4. Gluten-free\nEnter number: ")
    if crust.isdigit() and 1 <= int(crust) <= len(crusts):
        c = list(crusts.keys())[int(crust) - 1]
        bill += crusts[c]
        options.append(f"Crust: {c.replace('_', ' ').title()} - KES{crusts[c]:,.2f}")
    else:
        display_error()
        continue

    size_price = sizes[size]
    options.append(f"Size: {size.upper()} - KES{size_price:,.2f}")

    toppings_table = PrettyTable(['Topping Number', 'Topping Name', 'Price'])
    for key, value in toppings.items():
        toppings_table.add_row([key, value['name'].replace('_', ' ').title(), f"KES{value['price']:.2f}"])

    print("\nAvailable Toppings:")
    print(toppings_table)

    selected_toppings = {}
    while True:
        topping_choice = input("\nEnter topping number ('done' when finished): ")
        if topping_choice.lower() == 'done':
            break
        elif topping_choice.isdigit() and 1 <= int(topping_choice) <= len(toppings):
            qty = int(input("Enter quantity: "))
            topping_info = toppings[int(topping_choice)]
            topping_name = topping_info['name']
            topping_price = topping_info['price'] * qty
            bill += topping_price
            selected_toppings[topping_name] = qty
            options.append(f"{topping_name.replace('_', ' ').title()} - KES{topping_price:,.2f} x {qty}")
        else:
            display_error()

    print("\nOrder Summary:")
    for option in options:
        print(option)
    print("________________________________")
    print(f"Total for this pizza: KES{bill:,.2f}")

    upgrade = input(f"\nUpgrade size? (Y/N): ")
    if upgrade.lower() == 'y':
        old_size_price = sizes[size]
        new_size = get_input(f"\nSelect new size (S/M/L): ")
        if new_size in sizes and sizes[new_size] > old_size_price:
            add_cost = sizes[new_size] - old_size_price
            bill += add_cost
            options.append(f"Size Upgrade ({size.upper()} to {new_size.upper()}) - Additional Cost: KES{add_cost:,.2f}")
            print(f"Size upgraded from {size.upper()} to {new_size.upper()} with an additional cost of KES{add_cost:,.2f}")

    total += bill
    print(f"Running Total: KES{total:,.2f}")

print("\nThank you for ordering!")

