#  Write a program that takes a list and moves all found 0 items in list to the end.
#  Date: 12/10/21 Dev: Richard C.

#  Could also iterate through array, if 0, store the index in a variable, once done iterating, create a loop to remove all indexes, and for how 
#  ever many times that loop occurs, append a 0

def move_zeros(array):
    #  Iterate through each item in array, if item is 0, remove 0 (default first instance of 0) from new_array, and append a 0 to the end of new_array.
    new_array = array

    for i in range(len(array)):
        if array[i] == 0:
            new_array.remove(0)
            new_array = new_array.append(0)

    return new_array


#  Test
test = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 0]
print(move_zeros(test))