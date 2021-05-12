#This function asks for input of what day is today's workout (A-E), and outputs in order x exercise /w y weight, has user input how many reps with that weight 3 times 
#(if any 2/3 inputs is greater than 12 reps, adds reminder to up weight, if any 2/3 inputs are less than 8 reps, adds reminder to decrease weight), the date,
#and stores this data somewhere.
#Version: 1.0 Date: 03/08/21

import re

def todays_workout():
    
    answer = input("What workout are we doing today? (A-E)\n")
    
    workout_regex = re.compile(answer + r".*?#", re.DOTALL)

    mo1 = workout_regex.search( 

"""A Day

deadlift - 

85

10/10/10







####################################

B Day

deadlift - 

85

10/10/10







####################################

C Day

deadlift - 

85

10/10/10







####################################""")                                                                                            #Replace with search() given file instead of manually inputting string 

    print("\n" + mo1.group())

todays_workout() 