#  Script that takes any string of a written out number between zero and one million, and converts it to an integer of that number.
#  Must be able to handle "and" i.e. "one hundred and three"
#  Date: 03-15-22 Dev: Richard C.


def parse_int(string):
    #  TODO: Figure out common patterns in written out numbers one through one million to simplify converting that string to int
    #  When solving for the final int number, anytime "and x" is found, the value of x comprises the final int number position
    #  i.e. "ten thousand and twenty" == 10x where x is 20
    # 
    #     

    #  TODO: make a dictionary where keys are the strings of a number, and values are the int value of that key/string

    #  TODO: Use string.split(" ") to break string into a list of individual parts

    #  TODO: loop through new list of split string, for each item converting its string to its int equivalent, and putting into new string. If 
    #        string_of_number split is larger than 1 item, handle 2nd item as hundreds place indicator and create space accordingly
    #        for every increase in range, note that many hunreds places

     
    return # number


#  Test
test = ["one", "twenty", "two hundred and forty-six", "seven hundred eighty-three thousand nine hundred and nineteen"]

for string_of_number in test:
    print(parse_int(string_of_number))