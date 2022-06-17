#  Write a function that when passed 2 arguments will compare both arguments by structure (not actual values) of 
#  it's items, and return True if equal or False if not equal.

def same_structure_as(original,other):
    #  Possible for loop to loop through original
    pass


original_argument = input("Please enter the original argument: \n")
new_argument = input("Please enter the new argument to compare against the original argument: \n")

print(f"\nIt is {print(same_structure_as(original_argument, new_argument))} that the original argument and new argument are equal.")

#  Test: [1,[1,1]],[2,[2,2]] = True, [1,[1,1]],[[2,2],2] = False, [ [ [ ], [ ] ] ], [ [ 1, 1 ] ] = False