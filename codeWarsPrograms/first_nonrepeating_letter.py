#  Write a program that when given a string will return the first nonrepeating letter of that string
#  Date: 1-15-22 Dev: Richard C.

def first_non_repeating_letter(word):
    #  take string and iterate through each character, if character hasn't occurred, store character in dictionary and using count(), 
    #  attach the value of count
    character_occurence = {}

    for letter in word:
        if letter not in character_occurence:
            character_occurence[letter] = word.count(i)

    #  iterate through dictionary, on first instance of value 1, return as first nonrepeating letter of string
    for key_letter in character_occurence:
        if character_occurence[key_letter] == 1:
            return key_letter

#  Test
test_strings = ["stress", "a", "moonmen", "abba", "", "~><#~><", "sTreSS"] 
for i in test_strings:
    print(first_non_repeating_letter(i))