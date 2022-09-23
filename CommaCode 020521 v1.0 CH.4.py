spam = []

def list_contains(input_list):
    for i in range(len(input_list) - 1):
        print(input_list[i], end=', ')
    print('and, ' + str(input_list[-1]))

print('Please enter all the items of your list. When you are done, enter "done".')
while True:
    item = input()
    if item == 'done':
        break
    spam.append(item)

list_contains(spam)

