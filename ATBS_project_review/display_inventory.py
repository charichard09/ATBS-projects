#  Create a function that when passed a dictionary containing a video game inventory, will print all its
#  items and a total number of items. The keys will be strings of the items, and the values will be how many.
#  Date: 09-23-22  Dev: Richard Cha

def display_inventory(inventory):
    total = 0
    print("Inventory:\n")
    for inventory_item in inventory.items():
        name, amount = inventory_item
        print(f"{amount} {name}")
        total += amount
    print(f"Total number of items: {total}")

stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

display_inventory(stuff)