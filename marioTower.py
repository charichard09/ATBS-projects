#Program that will print a pyramid of inputted height.
#Note: This program works with the understanding when each iteration replaces list index length[x] with '#', that index will remain '#' 
#in memory. Recall with lists any assignment statements don't truly assign a list to a variable but assign an address of a list to a variable.
#Thus removing the need to add multiple inner '#' blocks since changing them once will keep them changed.
#Date: 05-12-21

height = int(input("Please enter the height of the tower: "))

#Create empty list to represent left, center, and right of each pyramid layer
length = ([' '] * height) + [' '] + ([' '] * height)

#Declare initial index of inner left and right pyramid columns
block_left = height - 1
block_right = height + 1
print(''.join(length))

#For each new layer, -1 index from inner left column and +1 index from inner right column and assign '#' block, repeating for 
#height.
for i in range(height, 0, -1):
    length[block_left] = '#'
    length[block_right] = '#'
    print(''.join(length))
    block_left -= 1
    block_right += 1



    

