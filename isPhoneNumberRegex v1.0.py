#This program takes an input string and returns any phone number it finds in the string using the new regex (regular expression) syntax from the re library
#Version: 1.0 Date: 030321

import re                                                                           #re library gives access to the re.compile(), .search() method function, .group() method function

def is_phone_number(text):
    phone_number_regex = re.compile(r"\d{3}-\d{3}-\d{4}")                           #r for raw string, which treats "\" char as a raw char without needing to escape it.
    mo = phone_number_regex.search(text)                                            #mo is common variable name for Match object, which is what is returned if .search() finds a matching regular expression in passed string
    print("Phone number found: " + mo.group())                                      #group() gives string of Match object

answer = input("Please input a string you would like searched for a phone number:\n")
is_phone_number(answer)