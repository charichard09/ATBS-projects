#  Write a program that takes a list and moves all found 0 items in list to the end using List Comprehension
#  Date: 1/8/21 Dev: Richard C.


def move_zeros(array):
    new_array = [non_zero for non_zero in array if non_zero != 0]
    for i in range(array.count(0)):
        new_array.append(0)

    return new_array


#  Test
test = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 0]
print(move_zeros(test))