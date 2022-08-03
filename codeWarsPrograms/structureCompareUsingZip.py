#  Second version of structureCompare.py. Using the zip function (zip will take iterable arguments and return a zip object 
#  containing as many tuples as there are items to zip together in given iterable arguments), 
#  write a program that will compare two arguments and their items and return True or False if they are similar.
#  Patch 1.0: Finished coding but returning wrong answer
#  Patch 1.1 Date 7/10/22:  Remembered using the input function will always save user input as a String Type. 
#  By using input to have the user give arguments as arguments for structure compare function, I have to 
#  convert the input from String Type to List Type
#  New problem: by using list function on input, I can no longer check against edge cases that want to check 
#  non List Types such as 2, because the list function will automatically convert it to a list giving me 
#  and incorrect comparison. 
#  Proposal: Look up and implement the ability to pass command line arguments directly into arguments for 
#  structure_compare function. 
#  Patch 1.2 Date 7/12/22: Learned about ast.literal_eval function that will evaluate a string to its literal type 
#  depending on it's syntax. I can use this on input to take the string and convert it into the correct type.
#  note: ast.literal_eval has its limits and should be studied more, but serves it purpose in this context.

# import Abstract Syntax Trees module to allow use of the ast.literal_eval function
import ast 

def structure_compare(original, new_arg):
    if isinstance(original, list) and isinstance(new_arg, list) and len(original) == len(new_arg):
        for original_index, new_arg_index in zip(original, new_arg):
            if type(original_index) == type(new_arg_index):
                continue
            else:
                return bool(False)
        return bool(True)
    else:
        return bool(False)


original_struc = ast.literal_eval(input("Please enter the original argument: \n"))
new_arg_struc = ast.literal_eval(input("Please enter the new argument to compare against the original argument: \n"))

print(f"\nIt is {structure_compare(original_struc, new_arg_struc)} that the original argument and new argument are equal.")