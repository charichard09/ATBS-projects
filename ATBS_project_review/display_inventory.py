#  Create a function that when passed a dictionary containing a video game inventory, will print all its
#  items and a total number of items. The keys will be strings of the items, and the values will be how many.
#  Write a second function that will take another inventory as "loot" and add it to the "inventory".
#  Date: 09-23-22  Dev: Richard Cha

def display_inventory(inventory):
    total = 0

    print("Inventory:\n")

    for inventory_item in inventory.items():
        name, amount = inventory_item
        print(f"{amount} {name}")
        total += amount

    print(f"Total number of items: {total}\n")

def add_to_inventory(inventory, loot):
    #  Use if "item" in condition to check if item exists in player inventory. If item exists, use get() to add 
    # drop amount to item amount. If item does not exist, setdefault should add it to dictionary.
    for drop_item in loot.items():
        name, amount = drop_item
        if name in inventory:
            inventory[name] = inventory[name] + amount
        else:
            #  Could also do inventory[name] = amount
            inventory.setdefault(name, amount)
    
    display_inventory(inventory)


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragon_drops = {"gold coin": 50, "dagger": 1, "ruby": 3}

display_inventory(stuff)
add_to_inventory(stuff, dragon_drops)