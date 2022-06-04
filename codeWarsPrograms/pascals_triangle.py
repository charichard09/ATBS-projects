#  Program that mimics Pascal's Triangle formula. In Pascal's Triangle, each cell is the sum of the number, or numbers, directly above it.
#  Given an integer for number of rows (1 <= numRows <= 30), return the values for each cell in each row from top to bottom  
#  (i.e. numRows = 5, return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]) 


def pascals_triangle(num_rows):
    #  Theory 1: A basic approach could be to create a dictionary that contains keys row_1 - row_30, and values 
    #  list_row_1 - list_row_30 respectively. When asked how many rows for Pascal's Triangle, print in reverse order the 
    #  value list_row_n at key row_n, until row_n == 1.

    #  Theory 2: loop as many times as numRows. Start solving for each row every loop, with index_new[0] always being [1]. 
    #  For every loop starting from index_new[1], index_new[n] = index_new[n] + index_new[n-1]
    row = [[1]]
    new_row = [1]

    #  Loop and calculate each item in new_row. Once finished looping num_rows, concatenate new_row to row.
    for i in range(1, num_rows):
        #  Doing row[-1] will mean we are always creating new_row using the last item appended to row
        for j in range(len(row[-1])):
            try:
                new_row.append(row[-1][j] + row[-1][j+1])
            except IndexError:
                new_row.append(row[-1][j])
        
        row.append(new_row)
        new_row = [1]
    
    return row


number_rows = input("Please enter a number between 1 and 30 for how many rows to calculate Pascal's Triangle:\n")
print(pascals_triangle(int(number_rows)))
