# Program that asks the user to input a string to search, then searches all the .txt files in a folder and returns 
# the found string and the file the string was found in.

import re, os, sys

# Have user input a string, then create regex from that string
answer = input("Please enter what you would like to be searched for: \n")

phrase_regex = re.compile(answer, re.IGNORECASE)

# TODO: Assume the text files are in a folder below this program called text2Search, search folder by writing a loop that will iterate through
# the directory of text2Search
directory = os.path.dirname(sys.argv[0]) + "/text2Search/"

assert os.path.exists(directory) == False, "no text2Search directory found"





# TODO: for each iteration, open .txt, save it, search it with regex_obj 
# if regex_obj != NoneType, print regex_obj.group(), print i in iteration

