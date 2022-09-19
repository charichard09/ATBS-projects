# Write a function that takes a list as an argument and returns a string of all the list's items
# seperated by a comma and an "and" before the final item. 
# Date: 9-17-22 Dev: Richard Cha

import ast

def comma_code(list_to_split):
    string_of_items = ""
    
    if len(list_to_split) == 2:
        string_of_items = list_to_split[0] + " "
    elif len(list_to_split) > 2:
        for i in range(len(list_to_split) - 1):
            string_of_items += list_to_split[i] + ", "
    else:
        string_of_items = list_to_split[0]
    
    if len(list_to_split) > 1:
        string_of_items = string_of_items + "and " + list_to_split[-1]
    
    return string_of_items

#  Using ast.literal_eval to evaluate whether what Type the input is and not just a string
print(comma_code(ast.literal_eval(input("Please enter the list you'd like to combine:\n"))))
