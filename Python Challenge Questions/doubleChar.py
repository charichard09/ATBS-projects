#This script doubles every character in a string and returns the string back to the user.

def double_char(text):
    double_text = ""
    for i in text:
        if i.isalnum():                                                                          #Checks if i is a number or alphabet, then doubles if True and skips if False. 
            double_text += i + i
        else:                                                                                    #if i isn't alpha numerical, concatenates a singular i character
            double_text += i

    return print(double_text)

answer = input("What string would you like doubled?\n")
double_char(answer)