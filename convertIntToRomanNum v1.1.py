#This program converts any integer between 1-1000 into its roman numeral equivalent.
#Version: 1.1 Date: 030121 Update: removed declaration and assignment of [thousands, hundreds, tens, ones] to number and replaced with "number = [0] * len(answer)
#                                  which more simply represents an empty list to store the place values of inputted answer. Also removed need for lstrip("0") since
#                                  new synax gives a perfect sized list to fit given answer rather than the before empty [0, 0, 0, 0] list.

def convert_int(answer):

    count = -1                                                                                                                              #Count is used to go backwards through the given answer, converting the 1's, 10's, 100's, then 1000's place

    number = [0] * len(answer)                                                                                                              #Create a list equal to the size of answer to store each int to roman numeral place value conversion

    roman_ones = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX", "0": ""}
    roman_tens = {"1": "X", "2": "XX", "3": "XXX", "4":"XL", "5": "LV", "6": "LX", "7": "LXX", "8": "LXXX", "9": "XC", "0": ""}
    roman_hundreds = {"1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC", "9": "CM", "0": ""}
    roman_thousands = "M"

    for i in range(len(answer)):
        if i == 0:
            number[count] = roman_ones[answer[count]]
        elif i == 1:
            number[count] = roman_tens[answer[count]]
        elif i == 2:
            number[count] = roman_hundreds[answer[count]]
        elif i == 3:
            number[count] = roman_thousands
        count += -1

    print("".join(number))                                                                                                      #In order: join number list of strings by "" character

int_to_conv = input("Please input the number you'd like converted in range 1-1000:\n")
convert_int(int_to_conv)