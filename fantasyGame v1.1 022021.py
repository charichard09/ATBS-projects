#Create a fantasy video game /w dictionary keys of "string" items and "values" of int how many many they have. Then write a function named display_inventory() that displays the inventory in a list /w a total inventory at the bottom.

starter_set = {"rope": 1, "torch": 6, "gold": 42, "dagger": 1, "arrows": 12}                                     #all players start out /w 1 rope, 6 torches, 42 gold, 1 dagger, and 12 arrows.

def display_inventory(inventory):
    print("Starting Inventory:")
    item_total = 0
    for i, j in inventory.items():
        print(i, j, sep=" ")
        item_total += j
    return "Total number of items: " + str(item_total)

display_inventory(starter_set)

#Write a function named add_to_inventory(inventory, added_items), where the inventory is a dictionary parameter of the players current inventory, and the added_items is a list parameter to be added to the players inventory

dragon_loot = ["gold", "dagger", "gold", "gold", "ruby"]

def add_to_inventory(inventory, added_items):
    for i in added_items:                                                                                   
        inventory.setdefault(i, 0)                                                                          
        inventory[i] += 1                                                                                   
    print("\nUpdated inventory: ")                                                                          
    for k, l in inventory.items():                                                                          
        print(k, l, sep=" ")
#v1.1 update: understanding "for i in added_items" i isn't an int but represents added_items[0]
#   I can then change arguments of inventory.setdefault(added_items[i], 0) to just i                    
#   which == inventory.setdefault("gold", 0)
#   i.e. in the first for loop iteration i = 0 = "gold" in add_items list

add_to_inventory(starter_set, dragon_loot) 
