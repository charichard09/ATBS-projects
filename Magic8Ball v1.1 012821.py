#This is the same as Magic 8 Ball program but using the list data type to simplify the code and no function def or call

import random

answer = ['It is certain', 'It is decidedly so', 'Yes', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']

fortune = answer[random.randint(0, (len(answer) - 1))]
print('Your fortune today reads: \n' + fortune + '\nThank you for playing. Please press any key to exit')
input()

