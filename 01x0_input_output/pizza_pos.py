#!/usr/bin/python3

while True:
    bill = 0

    size = input("\n:) Pizza Size(S/M/L)? (type 'EXIT' to end): ")

    if size.lower() == 'exit':
        break

    if size.lower() not in ['s', 'm', 'l']:
        print("Invalid input, please try again.")
    else:
        if size.lower() == 's':
            bill += 800
            print(f"Small Pizza: KES{bill:,.2f}")

        elif size.lower() == 'm':
            bill += 1000
            print(f"Medium Pizza: KES{bill:,.2f}")

        elif size.lower() == 'l':
            bill += 1500
            print(f"Large Pizza: KES{bill:,.2f}")

        add_pp = input("\nDo you want pepperoni(Y/N)? ")
        if add_pp.lower() == 'y':
            bill += 300
            print("Add Pepperoni: KES300")
        elif add_pp.lower() == 'n':
            pass
        else:
            continue

        add_ch = input("\nDo you want extra cheese(Y/N)? ")
        if add_ch.lower() == 'y':
            bill += 400
            print("Add Extra Cheese: KES400")
        elif add_ch.lower() == 'n':
            pass
        else:   
            continue

        print("________________________________")
        print(f"Total: KES{bill:,.2f}")
    
