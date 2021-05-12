
#This program takes a list of lists of strings and prints each inner list as a right-justified column.
#Version: 1.0 Date: 030121

def print_table(table):
    
    #find largest string in each inner list and assign it an index in colWidths[]. Each index will be used to dictate the column width of each printed inner list of similar index (list[0] will have column_width[0]..)
    width_column = 0
    colWidths = [0] * len(table)                                                                                #create a new list, of length equal to "table", containing zeroed values (i.e. [0] * 3 = [0, 0, 0]) 
    for i in range(len(table)):                                                                                 
        for j in table[i]:
            if width_column < len(j):                                                                           #if string j is longer than width_column, assign longer length to width_column
                width_column = len(j)
        colWidths[i] = width_column                                                                             #assign largest width of inner list to i
        width_column = 0                                                                                        #reassign width_column to 0 so next iteration has a fresh comparison of its index 0 compared to the other indexes

    for y in range(len(table[0])):                                                                              #assuming all lists contain equal amt of strings. loop until done printing each string (len(table)) of x inner list.
        for x in range(len(table)):                                                                             #   rjustified by associated colWidth[x]. 
            print(table[x][y].rjust(colWidths[x]), end=" ")
        print("")

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)