#  Write a function that when passed 2 arguments will compare both arguments by structure (not actual values) of 
#  it's items, and return True if equal or False if not equal.

def same_structure_as(original,other):
    #  Compare lengths of original and other, if they are not equal, can immediately return False. 
    #  Doing this also prevents an IndexError if original is lengthier than other, and 
    #  prevent handling original being shorter than other.
    if len(original) != len(other):
        return bool(False)

    #  To avoid comparing values, use type() to convert the values to their respective data types
    for count, structure in enumerate(original):
        if type(other[count]) == type(structure):
            continue
        else:
            #  Python normally treats returning False as a function failure and ends the function. 
            #  To return the boolean value False you use the bool() function.
            return bool(False)
        
    return bool(True)

original_argument = input("Please enter the original argument: \n")
new_argument = input("Please enter the new argument to compare against the original argument: \n")

print(f"\nIt is {same_structure_as(original_argument, new_argument)} that the original argument and new argument are equal.")

#  Test: [1,[1,1]],[2,[2,2]] = True, [1,[1,1]],[[2,2],2] = False, [ [ [ ], [ ] ] ], [ [ 1, 1 ] ] = False