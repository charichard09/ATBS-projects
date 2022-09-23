#Character Picture Grid
#This program takes list variable grid and outputs
#..00.00..
#.0000000.
#.0000000.
#..00000..
#...000...
#....0....

import copy

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'], 
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

new_y = []                                                              #declare new_y list variable to insert each grid[x] position into, taking "y" axis and putting them into the "x" axis individually
x = 0                                                                   #x is assigned to 0 to make sure for loop starts from index 0 of each list in grid
while x <= (len(grid[0]) - 1):                                          #while loop to loop through the amount of lists (or "y" axis) in grid. -1 because 0 through any whole number is that number +1 if you start from a 0 iteration (i.e. 0-6 is actually 7 iterations)
        for y in grid:                                                  #       In this case we are looping through a list which starts its indexes at 0.
                new_y.insert(0, y[x])                                   #for loop to loop through how many items are in grid, each loop taking the y[x] index and inserting it into index 0 of declared new_y blank list to get a full "x" axis 
        
        print(new_y)                                                    #print new_y list, then reassign new_y to a blank list. Augment operater x = 1 + itself so that when the while loop returns to the top, the loop will begin taking the 
        new_y = []                                                      #       next index of each item in grid.
        x += 1
        