# Program that asks the user to input a string to search, then searches all the .txt files in a folder and returns 
# the found string and the file the string was found in.

import re, os, sys

# Have user input a string, then create regex from that string
answer = input("Please enter what you would like to be searched for: \n")

phrase_regex = re.compile(answer, re.IGNORECASE)

# Assume the text files are in a folder below this program called text2Search, search folder by writing a loop that will iterate through
# the directory of text2Search
directory = os.path.dirname(sys.argv[0]) + "/text2Search"

assert os.path.exists(directory) != False, "no text2Search directory found"

for dir_path, dir_name, file_name in os.walk(directory):
    print(str(dir_path) + '\n' + str(dir_name) + '\n' + str(file_name))
    for file in file_name:
    
    # TODO: for each iteration, open dir_path + file in file_name (which gives the absolute path of file), read it, search it with regex_obj 
    # if regex_obj != NoneType, print regex_obj.group(), print i in iteration       
        with open(dir_path + '/' + file, 'r') as file_obj:
            file_text = file_obj.read()
            answer_mo = phrase_regex.search(file_text)
            if answer_mo != None:
                print(answer + " was found in " + file)
                
            
            
