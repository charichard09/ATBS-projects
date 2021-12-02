# Program (called ROT13 on Codewars) that will iterate through a string and replace any letter with the letter 13 places away from it in 
# the alphabet. Will ignore any symbols or numbers.
# Date: 10/27/21 Dev: Richard C.

import re

# TODO: Create variable for double alphabet "abcdefghijklmnopqrstuvwxyzabcdefghijklm" to find letter +13 away 

# TODO: Make while loop if counter < 13; continue, for each loop, iterate through each index of string and if value at index is
# in the alphabet, increment counter, else continue

# TODO: Once counter < 13; counter = 0; replace current index of string to letter 13 letters from current index character 

# TODO: Iterate and search for index char in alphabet variable, once index char i == j in alphabet string, get index of j,
# replace i with index of j+13; continue




# First idea using regular expressions

# TODO: Create regex for simple aphabetical character

# TODO: Problem: Any character at index[13] of the alphabet + 13 will exceed the alphabet.
# Possible solution: create a string of 2 alphabets (i.e. new_string = "a-z" * 2)

# TODO: Iterate through given string, each time checking regex_match_object to character. If match, possibly use regex_obj.sub() method?