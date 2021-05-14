#Program that will print a pyramid of inputted height.
#Date: 05-12-21

height = int(input("Please enter the height of the tower: "))

length = ([' '] * height) + [' '] + ([' '] * height)
block_left = height - 1
block_right = height + 1
print(''.join(length))

for i in range(height, 0, -1):
    length[block_left] = '#'
    length[block_right] = '#'
    print(''.join(length))
    block_left -= 1
    block_right += 1



    

