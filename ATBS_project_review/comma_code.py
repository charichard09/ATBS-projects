# Write a function that takes a list as an argument and returns a string of all the list's items
# seperated by a comma and an "and" before the final item. 
# Date: 9-17-22 Dev: Richard Cha

import sys

def comma_code(list_to_split):
    string_of_items = ""
    
    if len(list_to_split) == 2:
        string_of_items = list_to_split[0]

    if len(list_to_split) > 2:
        for i in len(list_to_split) - 1:
            string_of_items += i + ", "
    
    if len(list_to_split) > 1:
        string_of_items = string_of_items + "and " + list_to_split[-1]
    
    return string_of_items

#  TODO: Solve problem from input() and passing command line arguments (i.e. argv[1]) both being of string value.
#  How to pass a list as a user input?
comma_code(sys.argv[1])