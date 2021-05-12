
def convert_int(answer):
    ones = "0"
    tens = "0"
    hundreds = "0"
    thousands = "0"

    count = -1   

    number = [thousands, hundreds, tens, ones]

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

    print("".join(number).lstrip("0"))

int_to_conv = input("Please input the number you'd like converted in range 1-1000:\n")
convert_int(int_to_conv)