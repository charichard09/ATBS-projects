# Program (called ROT13 on Codewars) that will iterate through a string a replace any letter with the letter 13 places away from it in 
# the alphabet. Will ignore any symbols or numbers.
# Date: 10/27/21 Dev: Richard C.

import re

# TODO: Create regex for simple aphabetical character

# TODO: Problem: Any character at index[13] of the alphabet + 13 will exceed the alphabet.
# Possible solution: create a string of 2 alphabets (i.e. new_string = "a-z" * 2)

# TODO: Iterate through given string, each time checking regex_match_object to character. If match, possibly use regex_obj.sub() method?