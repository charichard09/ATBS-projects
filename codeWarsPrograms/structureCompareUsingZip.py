#  Second version of structureCompare.py. Using the zip function (zip will take iterable arguments and return a zip object 
#  containing as many tuples as there are iterable arguments, each index being paired with one another into each seperate 
#  tuple), write a program that will compare two arguments and return True or False if they are similar.

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


original = input("Please enter the original argument: \n")
new_arg = input("Please enter the new argument to compare against the original argument: \n")

print(f"\nIt is {structure_compare(original, new_arg)} that the original argument and new argument are equal.")