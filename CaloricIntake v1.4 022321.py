
#Write a program that prompts the user if they are inputting daily or weekly calories. If weekly call function weekly, if daily call function daily. 
#Both of which input total calories per given, day or week, adds them, and in the case of week, subtracts them from estimated caloric intake (17500), compares it to weekly caloric intake goal (14500), and prints that in a format to be pasted to a word doc. 
#date: 02/21     version: 1.2      

def weekly_calories():                                                                                                    #creates a function to call whenever user wants to input weekly calories and get a total
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    weekly_caloric_intake = 0

    for day in range(len(week)):                                                                                           #for loop to loop through the range of list week, len() returns int value of how many items in list week
        print('\nPlease enter total caloric intake for ' + week[day])                                                        #makes sure to print the string value located at index "day" in each loop
        try:
            weekly_caloric_intake += int(input())  
        except ValueError:
            print('     Error: Invalid argument. Please try again:')
            weekly_caloric_intake += int(input())
    
    return weekly_caloric_intake                                                                                   #augment operator to add users input to previous inputs to get total weekly caloric intake


def daily_calories():
    
    food = {}
    a = 2

    while True:    
        try:
            item, icalories = input("\nWhat was the name of the item you ate and how many calories was it? (pizza, 750)\n").split(',')            #to check input correction, could also use if icalories.isdecimal() to return true if string stored is a number
        except ValueError:
            print("    Error: Input should be in the form of 'food, calories'\n")
            continue
        
        try:
            icalories = int(icalories)
        except ValueError:
            print("    Error: calories must be of integer value.\n")
            continue

        if item in food:
            item = item + str(a)
            a += 1
        food[item] = icalories
        answer = input("Are there more items you'd like to input? (y/n)\n")
        if answer == "n":
            print("")
            break
        elif answer == "y":
            continue
    
    day = input("What day is it today?\n")
    print("\n" + day.center(27 + 6))
    total = 0
    for i in food:
        print(i.ljust(27, '.'), str(food[i]).rjust(6))
        total += int(food[i])

    return "Total daily caloric intake: ".ljust(27, ',') + str(total).rjust(6)


while True:
    response = input("Are you entering daily or weekly calories?\n")
    response = response.lower()

    if response == "weekly":
        total_cal = weekly_calories()                                                                                 #calls the how_many_calories function, assigns it to total_cal and prints the return value of the total calories consumed in the week
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
    elif response == "daily":
        print(daily_calories())
    else:                                                                                                           #daily function             
        print("    Error: answer must be daily or weekly.\n")
        continue

    print('\nDoes everything look correct? (y/n)')                                                                   #asks the user if eveything looks correct, if yes, exits program, if no, restarts program from the beginning
    answer = input()                                                                                                #could turn into a function, whenever I want to ask the user if info looks correct, and if/if not to restart or continue
    if (answer in ['yes', 'y', 'yeah', 'yup', 'yah']):
        print("thank you")
        break
    elif (answer in ['n', 'no', 'nope', 'nadda', 'nah']):
        continue
    else:
        print('That is not a correct response. Program will now restart.')
        break
