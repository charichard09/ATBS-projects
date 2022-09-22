#  Given a previouse list of lists image,
#  print the image below, where x is the length of each nested list, and y is how many lists exist.
#  ..00.00..
#  .0000000.
#  .0000000.
#  ..00000..
#  ...000...
#  ....0....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#  Knowing that when the image is turned to its side clockwise that there will be a total of 6 rows,
#  declare a new list that contains each row of the new image. Use this new list to build each row from grid,
#  adding each character to a row one at a time.
image = ["", "", "", "", "", ""]

#  Using a for loop to work with one nested list of grid at a time, then a nested for loop 
#  to take each item of the nested list, add each item to its place in image list. It works out that
#  when shifting grid clockwise to create image, each index of the nested grid will go into the respective
#  index of image, i.e. grid[0][3] will be the character for image[3], etc. etc.
#  The formula for this being: grid[column][row_index] = image[row_index]

for column in grid:
    for row_index, row_char in enumerate(column):
        image[row_index] = row_char + image[row_index]

#  Use image.join("\n") and print to get final image
print("\n".join(image))


