#  Write a function that when passed 2 arguments will compare both arguments by structure (not actual values) of 
#  it's items, and return True if equal or False if not equal.

def same_structure_as(original,other):
    #  Testing will pass non lists as arguments. Check arguments are list type.
    if type(original) != type(other) != list:
        return bool(False)
    
    #  Compare lengths of original and other, if they are not equal, can immediately return False. 
    #  Doing this also prevents an IndexError if original is lengthier than other, and 
    #  prevent handling original being shorter than other.
    if len(original) != len(other):
        return bool(False)
    
    #  To avoid comparing values, use type() to convert the values to their respective data types
    #  TODO: Fix [1, '[',']'] == ['[',']', 1] == True. Instructions don't care that items are int
    #  or string. This equals True because both arguments are of 1 list, 2 items.
    for count, structure in enumerate(original):
        #  if structure is a list, check inner items against one another
        if isinstance(structure, list) and isinstance(other[count], list):
            if len(structure) != len(other[count]):
                return bool(False)
            for count_nested, structure_nested in enumerate(structure):
                if type(structure_nested) == type(other[count][count_nested]):
                    continue
                else:
                    return bool(False)
            continue  
        elif isinstance(structure, list) or isinstance(other[count], list):
            #  if one item is a list and the other is not, return false
            return bool(False)
        else:
            #  Python normally treats returning False as a function failure and ends the function. 
            #  To return the boolean value False you use the bool() function.
            continue
        
    return bool(True)  

#  TODO: Need to fix input() inputing a string of list argument. We want the actual list itself. 
original_argument = input("Please enter the original argument: \n")
new_argument = input("Please enter the new argument to compare against the original argument: \n")

print(f"\nIt is {same_structure_as(original_argument, new_argument)} that the original argument and new argument are equal.")

#  Test: [1,[1,1]],[2,[2,2]] = True, [1,[1,1]],[[2,2],2] = False, [ [ [ ], [ ] ] ], [ [ 1, 1 ] ] = False
#  Test 2: [1,[1,1]], [2,[2]] = False