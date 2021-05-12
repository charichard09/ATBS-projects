
#Write a program that has the user input total calories per day, per week, adds them, subtracts them from estimated caloric intake (17500), compares it to weekly caloric intake goal (14500), and prints that in a format to be pasted to a word doc.   
#date: 02/21     version: 1.2      

def how_many_calories():                                                                                                    #creates a function to call whenever user wants to input weekly calories and get a total
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    weekly_caloric_intake = 0

    for day in range(len(week)):                                                                                           #for loop to loop through the range of list week, len() returns int value of how many items in list week
        print('\nPlease enter total caloric intake for ' + week[day])                                                        #makes sure to print the string value located at index "day" in each loop
        try:
            weekly_caloric_intake += int(input())  
        except ValueError:
            print('     Error: Invalid argument. Please try again:')
            weekly_caloric_intake += int(input())
    
    return weekly_caloric_intake                                                                             #augment operator to add users input to previous inputs to get total weekly caloric intake

#Could also do: (note: this method uses the sum() but does reassign the list week to the numbers inputed, thus later down the road may be confusing to the user if calling back the week variable)          
#
# for day in range(len(week)):
#   print('Please enter total caloric intake for ' + week[day])
#   week[day] = int(input())
#
#weekly_caloric_intake = sum(week)                                                                                      #the sum() sums the values in a list

#This method executes the program utilizing a function, I was hoping using global variable week in the function call locally wouldn't affect the global variable, but it does 
# 
# def calculate_weekly_calories():                                                                                       
#    for day in range(len(week)):
#        print('Please enter total caloric intake for ' + week[day])
#        week[day] = int(input())
#    return sum(week)
#
#weekly_caloric_intake = calculate_weekly_calories()

while True:
    total_cal = how_many_calories()                                                                                 #calls the how_many_calories function, assigns it to total_cal and prints the return value of the total calories consumed in the week
    print('\nWhat is this the week of? (i.e. month/day - month/day')
    date = input()
    print('\nWeekly caloric intake for the week of ' + date + ' is:\n' + str(total_cal) +
        '\nOut of a 17500 estimated caloric intake' +
        '\nI want to be -3500 calories. This week I am ' + (str(total_cal - 17500)) + ' calories', end= '')
    if (total_cal - 17500) > -3500:
        print(' under my goal. Try again this week! I know you can do it!\n')
    elif (total_cal - 17500) < -3500:
        print(' over my goal. Great Job!\n') 
    elif (total_cal - 17500) == -3500:
        print('. right on the money! Wow!\n')
    print('\nDoes everything look correct? (y/n')                                                                  #asks the user if eveything looks correct, if yes, exits program, if no, restarts program from the beginning
    answer = input()                                                                                                #could turn into a function, whenever I want to ask the user if info looks correct, and if/if not to restart or continue
    if (answer in ['yes', 'y', 'yeah', 'yup', 'yah']):
        break
    elif (answer in ['n', 'no', 'nope', 'nadda', 'nah']):
        continue
    else:
        print('That is not a correct response. Program will now restart.')
        break