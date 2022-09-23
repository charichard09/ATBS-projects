
#Write a program that has the user input total calories per day, per week, adds them, subtracts them from estimated caloric intake (17500), compares it to weekly caloric intake goal (14500), and prints that in a format to be pasted to a word doc.
#date: 01/18/21     version: 1.0     
#date: 01/25/21     version: 1.1      

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_caloric_intake = 0

for day in range(len(week)):
    print('Please enter total caloric intake for ' + week[day])
    weekly_caloric_intake += int(input())

print('What is this the week of? (i.e. month/day - month/day')
date = input()
print('\nWeekly caloric intake for the week of ' + date + ' is:')
print(weekly_caloric_intake)
print('Out of a 17500 estimated caloric intake')
print('I want to be -3500 calories. This week I am ' + (str(weekly_caloric_intake - 17500)) + ' calories', end= '')
if (weekly_caloric_intake - 17500) > -3500:
    print(' under my goal. Try again this week! I know you can do it!\n')
elif (weekly_caloric_intake - 17500) < -3500:
    print(' over my goal. Great Job!\n') 
elif (weekly_caloric_intake - 17500) == -3500:
    print(' right on the money! Wow!\n')
    