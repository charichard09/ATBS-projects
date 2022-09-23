
print('Hello World', 'Hello Galaxy', end='. ', sep='. ')
print('This is a new line, but end= removes the automatic new line.')
print('While sep= adds the period between World and Hello.')

dozen = 12


def how_many_left(amount):
    total = dozen - amount
    return total


print('\nHow many eggs are missing from the dozen?')
eggs = input()
print('You have ' + str(how_many_left(int(eggs))) + ' left.')

print('\nIt takes 3 eggs to make an omelet. You can make ', end='')


def omelets():
    make = (how_many_left(int(eggs))) / 3
    return int(make)


print(str(omelets()) + ' omelet(s).')
