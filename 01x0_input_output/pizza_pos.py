#!/usr/bin/python3

bill = 0

size = input("Pizza Size(S/M/L)?")

if size.lower() not in ['s', 'm', 'l']:
    print("Invalid input, please try again.")
else:
    if size.lower() == 's':
        bill += 100
        print(f"Small Pizza: KES{bill:,.2f}")

    elif size.lower() == 'm':
        bill += 200
        print(f"Medium Pizza: KES{bill:,.2f}")

    elif size.lower() == 'l':
        bill += 300
        print(f"Large Pizza: KES{bill:,.2f}")

    add_pp = input("\nDo you want pepperoni(Y/N)? ")

    if add_pp.lower() == 'y':
        bill += 200
        print("Add Pepperoni: KES200")

    elif add_pp.lower() == 'n':
        pass

    else:
        print("Invalid input, please try again")

    print("________________________________")
    print(f"Total: KES{bill:,.2f}")
    
