#  Script that takes any string of a written out number between zero and one million, and converts it to an integer of that number.
#  Must be able to handle "and" i.e. "one hundred and three"
#  Date: 03-15-22 Dev: Richard C.


def parse_int(int_word):
    #  Hypothesis: Figure out common patterns in written out numbers one through one million to simplify converting that string to int
    #  When solving for the final int number, anytime "and x" is found, the value of x comprises the final int number position
    #  i.e. "ten thousand and twenty" == 10x where x is 20
    
    print(f"The number we are parsing is: {int_word}")

    #  Remove any hyphen characters and replace with ' '
    int_word = int_word.replace('-', ' ')

    #  Assign number to be stored and returned, and string broken into a list, to variables
    number = []
    int_word_seperated = int_word.split(" ")

    #  Make two dictionaries, one where keys are the strings of unique numbers and values are the int value of that number, and another 
    #  where keys are place value words and values are the length of given place value

    written_numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0, "ten":10,
    "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
    "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}
    place_value = {"hundred":100, "thousand":1000, "million":1000000}

    #  Use string.split(" ") to break string into a list of individual parts

    for word in int_word_seperated:
        #  convert word to value and place into new list

        #  First item is always the first position of the number so we start building the new number with the first item
        #  This will also always be an int
        if int_word_seperated.index(word) == 0:
            number.append(written_numbers[word])
            continue

        #  Check condition if item 1 in int_

        #  TODO: Figure out how to handle words like and, thousand, etc. that aren't unique numbers
        #  Hypothesis: If I see "and", I can add the left and right side together. If I see a place value i.e. 100, I can multiply the left
        #  value and place value to get the correct number.
        if word in written_numbers:
            number.append(written_numbers[word])
        elif word in place_value:
            for place_number in range(place_value[word]):
                number.append(0)

    #  TODO: loop through new list of split string, for each item converting its string to its int equivalent, and putting into new string. If 
    #        string_of_number split is larger than 1 item, handle 2nd item as hundreds place indicator and create space accordingly
    #        for every increase in range, note that many hunreds places

     
    return number  # number


#  Test
test = ["one", "twenty", "fifty-six", "two hundred and forty-six", "fifty-five million six hundred seventy eight thousand two hundred and one", 
"seven hundred eighty-three thousand nine hundred and nineteen"]

for string_of_number in test:
    print(parse_int(string_of_number))