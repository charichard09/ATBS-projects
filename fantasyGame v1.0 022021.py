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
    for i in range(len(added_items)):                                                                       #I learned: "for i in added_items" i which I thought is 0 is actually added_items[0] (which is a string)
        inventory.setdefault(added_items[i], 0)                                                             #which inititall gave me errors on this line because you cannnot find the index of a list added_items[i] 
        inventory[added_items[i]] += 1                                                                      #if it is a string. List indexes are only represented by integers. If I then wanted to for loop through the
    print("\nUpdated inventory: ")                                                                            #length of the list I had to conver list to the integer of length of the list using len(added_items)
    for k, l in inventory.items():                                                                          #thus being i in range int
        print(k, l, sep=" ")

add_to_inventory(starter_set, dragon_loot)




