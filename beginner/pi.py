#!/usr/bin/python3
"""Pizza Order Program Documentation"""

from dataclasses import dataclass
from typing import Dict, List 

# Config dataclasses avoid dicts and make data more self-documenting
@dataclass
class Topping:
    name: str
    price: int

@dataclass   
class Crust:
    name: str
    price: int

@dataclass
class Size:
    name: str 
    base_price: int

# Validation functions for re-use
def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt).lower() 
        if response in valid_options:
            return response
        print("Invalid input, please try again")

def get_positive_int(prompt):
    while True:
        try: 
            value = int(input(prompt))  
            if value > 0:
                return value
        except ValueError:
            print("Invalid input, please enter a number")

# Main application logic
def print_order_summary(options: List[str]):
    print("Order Summary")
    for option in options:
        print(f"- {option}") 

def calculate_price(options: List[str]):
    return sum([int(price) for extra in options if extra.startswith("Total Price:") for price in extra.split() if price.isdigit()])
        
if __name__ == "__main__":
    
    crusts = [Crust("Thin", 100), Crust("Thick", 150)] 
    sizes =  [Size("Small", 800), Size("Medium", 1000)]
    toppings = [Topping("Pepperoni", 300), Topping("Cheese", 200)]

    order_options = []
    
    crust = get_valid_input("Select crust: ", [c.name for c in crusts])
    order_options.append(f"Crust: {crust} - {[c.price for c in crusts if c.name==crust][0]}")

    size = get_valid_input("Select size: ", [s.name for s in sizes]) 
    base_price = [s.base_price for s in sizes if s.name==size][0]
    order_options.append(f"Size: {size} - {base_price}")

    for t in toppings:
        qty = get_positive_int(f"Select quantity of {t.name}: ")
        order_options.append(f"{t.name}: {qty} x {t.price} = Total Price: {qty*t.price}")

    print_order_summary(order_options)  
    print(f"Total Price: {calculate_price(order_options)}")
