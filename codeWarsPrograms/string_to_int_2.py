#  Second attempt at converting a string of a number to the int equivalent of that number.

def parse_int(int_word):

    print(f"The number we are parsing is: {int_word}")

    #  Remove any hyphen characters and "and" string and replace with ' '
    int_word = int_word.replace("-", " ")
    int_word = int_word.replace(" and", "")

    #  Assign number to be stored and returned, and string broken into a list, to variables
    number = 0
    million_place_value_split = []
    million_place_value = 0
    million_calculated_flag = 0
    thousand_place_value_split = []
    thousand_place_value = 0
    thousand_calculated_flag = 0
    hundreds_place_value_split = []
    hundreds_place_value = 0
    int_word_seperated = int_word.split(" ")

    #  Make two dictionaries, one where keys are the strings of unique numbers and values are the int value of that number, and another 
    #  where keys are place value words and values are the length of given place value

    written_numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0, "ten":10,
    "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
    "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}
    place_value = {"hundred":100, "thousand":1000, "million":1000000}

    print(f"This is the number seperated in a list: {int_word_seperated}")
    
    for word in int_word_seperated:
        #  If million is in the string, find the integer at place value million, multiply by 1000000, and store in million_place_value_split
        if "million" in int_word_seperated and not million_calculated_flag:   
            if word != "million":
                if word in written_numbers:
                    million_place_value_split.append(written_numbers[word])
                    continue
                elif word == "hundred":
                    million_place_value_split.append("hundred")
                    continue
                else:
                    #  TODO: Find and convert print to actually raise error code
                    print("ERROR: word not found in either written numbers or place value")
            else:
                #  add values to get million place value

                #  Calculate for hundred if word hundred exists
                if "hundred" in million_place_value_split:
                    million_place_value_split.remove("hundred")
                    million_place_value_split[0] = million_place_value_split[0] * 100
                
                #  Add together the hundreds/tens/ones place values then multiply by 1 million
                for i in million_place_value_split:
                    million_place_value = million_place_value + i
                million_place_value = million_place_value * 1000000
                million_calculated_flag = 1
                continue

        #  If thousand is in the string, find the integer at place value thousand, multiply by 1000, and store in thousand_place_value.
        #  Test: If "million" was calculated, word would still start this if loop at the index where "thousand" place value would begin
        if "thousand" in int_word_seperated and not thousand_calculated_flag:
            if word != "thousand":
                if word in written_numbers:
                    thousand_place_value_split.append(written_numbers[word])
                    continue
                elif word == "hundred":
                    thousand_place_value_split.append("hundred")
                    continue
                else:
                    print("ERROR: word not found in either written numbers or place value")
            else:
                if "hundred" in thousand_place_value_split:
                    thousand_place_value_split.remove("hundred")
                    thousand_place_value_split[0] = thousand_place_value_split[0] * 100
                
                for j in thousand_place_value_split:
                    thousand_place_value = thousand_place_value + j
                thousand_place_value = thousand_place_value * 1000
                thousand_calculated_flag = 1
                continue
        
        #  TODO: find the integer at the ones, tens, hundreds place value, then add million_place_value + thousand_place_value + this result to
        #  get final number
        if word == "hundred":
            hundreds_place_value_split.append("hundred")
            continue
        elif word in written_numbers:
            hundreds_place_value_split.append(written_numbers[word])
            continue
        
    if "hundred" in hundreds_place_value_split:
        hundreds_place_value_split.remove("hundred")
        hundreds_place_value[0] = hundreds_place_value_split[0] * 100
        
    #  Check hundreds_place_value_split
    print(hundreds_place_value_split)
    for k in hundreds_place_value_split:
        hundreds_place_value = k + hundreds_place_value
    
    number = million_place_value + thousand_place_value + hundreds_place_value

    
    return number

#  Test
test = ["one", "twenty", "fifty-six", "two hundred and forty-six", "fifty-five million six hundred seventy eight thousand two hundred and one", 
"seven hundred eighty-three thousand nine hundred and nineteen"]

for string_of_number in test:
    print(parse_int(string_of_number))