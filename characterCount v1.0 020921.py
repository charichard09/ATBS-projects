# Program that counts how many times a character shows up in a given message

print('Please enter a message: ')
message = input()

count = {}                                              #assign dictionary variable a blank dictionary
for character in message:                               #for loop through character variable (initially 0) through message variable (all of user inputed characters) 
    count.setdefault(character, 0)                      #setdefault function checks dictionary count (initially {}) for the "key character" in message[character]. If there is no "key character" (i.e. 'H'), key 'H' will be added to count with default value 0.
    count[character] += 1                               #If "key character" is in dictionary count, returns value of "key character". Add +1 to the value of index count["key" character]. repeat for loop character+1 for next string position

print(count)                                            #print final dictionary count
