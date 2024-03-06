#!/usr/bin/python3
products = ['Phone', 'Tablet', 'Laptop', 'Journal']

# Displaying products
print(f"Current list of items: {products}")

# Function to add an item to the products list
def add_item():
    return input("Enter item to add: ").capitalize()

# Function to remove an item from the products list
def remove_item():
    item_to_remove = input("Enter product to remove: ").lower()
    removed = False
    for product in products[:]:  # Using a copy of the list to avoid modifying it while iterating
        if product.lower() == item_to_remove:
            products.remove(product)
            removed = True
    if removed:
        print(f"Removed {item_to_remove} from the list.")
        print(f"New list of items: {products}")
    else:
        print(f"{item_to_remove} not found in the list.")

# Asking the user whether to add or remove an item
action = input("Do you want to add or remove an item? (add/remove): ").lower()

# Performing the chosen action
if action == "add":
    new_item = add_item()
    products.append(new_item)
    print(f"Updated list of items: {products}")
elif action == "remove":
    remove_item()
else:
    print("Invalid action. Please choose 'add' or 'remove'.")

