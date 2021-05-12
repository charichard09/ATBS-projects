#Defines a function that when called prints a fortune based on a random number 
#generated each time
#
#Version: 1.0 Date: 1/28/21
import random                   #imports "random" module allowing access to functions in random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = get_answer(r)
print("Your fortune for today reads: \n" + fortune + "\n" + "Thank you for playing. Please press any key to exit.")
input()                     #input() is used to keeps output on screen until the user presses any key