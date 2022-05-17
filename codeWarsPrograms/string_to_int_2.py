#  Second attempt at converting a string of a number to the int equivalent of that number.

def parse_int(int_word):

    print(f"The number we are parsing is: {int_word}")

    #  Remove any hyphen characters and "and" string and replace with ' '
    int_word = int_word.replace('-', ' ')
    int_word = int_word.replace("and", ' ')

    #  Assign number to be stored and returned, and string broken into a list, to variables
    number = 0
    million_place_value = []
    million_calculated_flag = 0
    thousand_place_value = []
    thousand_calculated_flag = 0
    int_word_seperated = int_word.split(" ")

    #  Make two dictionaries, one where keys are the strings of unique numbers and values are the int value of that number, and another 
    #  where keys are place value words and values are the length of given place value

    written_numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0, "ten":10,
    "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
    "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}
    place_value = {"hundred":100, "thousand":1000, "million":1000000}

    print(int_word_seperated)
    
    for word in int_word_seperated:
        #  If million is in the string, find the integer at place value million, multiply by 1000000, and store in million_place_value
        if "million" in int_word_seperated and not million_calculated_flag:   
            if word != "million":
                million_place_value.append(written_numbers[word])
            else:
                #  add values to get million place value

                #  Calculate for hundred if word hundred exists
                if "hundred" in million_place_value:
                    million_place_value.remove("hundred")
                    million_place_value[0] = million_place_value[0] * 100
                
                #  Add together the hundreds/tens/ones place values then multiply by 1 million
                print(million_place_value)
                for i in million_place_value:
                    number = number + i
                number = number * 1000000
                million_calculated_flag = 1
                continue

        #  TODO: If thousand is in the string, find the integer at place value thousand, multiply by 1000, and store in thousand_place_value
        if "thousand" in int_word_seperated and not thousand_calculated_flag:
            if word != "thousand":
              

        #  find the integer at the ones, tens, hundreds place value, then add million_place_value + thousand_place_value + this result to
        #  get final number
        
    
    return number

#  Test
test = ["one", "twenty", "fifty-six", "two hundred and forty-six", "fifty-five million six hundred seventy eight thousand two hundred and one", 
"seven hundred eighty-three thousand nine hundred and nineteen"]

for string_of_number in test:
    print(parse_int(string_of_number))