#  Test file to test code snippets
#  Dev: Richard C.

#  Create a  that function that accepts a grade input, and using dictionary comprehension to create a grading chart, prints the score 
#  Date: 1-12-22
import string

def what_is_your_grade(grade): 
    #scoring_chart = {i:score - 10 for i in string.ascii_uppercase[0:6]}
    scoring_chart = {string.ascii_uppercase[0:6][i-1]:f"{109 - i*10} - {100 - i*10}" for i in range(1, 7)}


    return f"You scored between {scoring_chart[grade]}"


print(what_is_your_grade(input("What was your grade?")))


#  Convert any variation of yes or no to 1 or 0 to test 1 being True and 0 being False
def convert_to_int(word):
    pass
    yes_possibilities = ["yes", "y", "1", "True", "true"]
    no_possibilities = ["no", "n", "0", "False", "false"]

    if word in yes_possibilities:
        return 1
    elif word in no_possibilities:
        return 0
    else:
        print(f"{word} is not a possible answer. Program will now end.")    


#  if convert_to_int(input("Would you like to continue?")):
#     print("Program has continued.")
#  else:
#     print("Program has stopped.")