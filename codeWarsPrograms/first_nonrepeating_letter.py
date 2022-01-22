#  Write a program that when given a string will return the first nonrepeating letter of that string
#  Date: 1-15-22 Dev: Richard C.

def first_non_repeating_letter(word):
    pass
    #  take string and iterate through each character, if character hasn't occurred, store character in dictionary and using count(), 
    #  attach the value of count
    character_occurrence = {}
    word_ignorecase = word.lower()
    upper_true = 0

    for i in range(len(word_ignorecase)):
        if word_ignorecase[i] not in character_occurrence:
            character_occurrence[word_ignorecase[i]] = word_ignorecase.count(word_ignorecase[i])

            #  Add upper case check
            if word[i].isupper():
                upper_true = 1

    #  iterate through dictionary, on first instance of value 1, return as first nonrepeating letter of string
    for key_letter in character_occurrence:
        if character_occurrence[key_letter] == 1:
            if upper_true:
                return key_letter.upper()
    
    #  if no key:value equals 1, return "" aka nothing found
    return ""


#  Second attempt to shorten code
def locate_non_repeat(characs):
    character_occurrence = {}
    for symbol in characs:
        if symbol not in character_occurrence:
            if symbol.isalpha():  
                character_occurrence[symbol] = characs.count(symbol.lower()) + characs.count(symbol.upper())
            else:
                character_occurrence[symbol] = characs.count(symbol)


#  Test
test_strings = ["stress", "a", "moonmen", "abba", "", "~><#~><", "sTreSS"] 
for i in test_strings:
    print(locate_non_repeat(i))
