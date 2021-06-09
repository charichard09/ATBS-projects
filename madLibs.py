#Program that reads a text file and replaces the words ADJECTIVE, NOUN, ADVERB, or VERB with a prompted user input,
#then create a new file with the new words in place of the old words and print to screen.
#Date: 6-8-2021 #Dev: Richard Cha

import os, sys

#TODO: open file as r+ and read to variable
mad_libs_fo = open(os.path.dirname(sys.argv[0]) + "/madLibs.txt")

mad_libs_text = mad_libs_fo.read()

mad_libs_fo.close()

print(mad_libs_text)

#TODO: create regex for ADJECTIVE, NOUN, ADVERB, VERB

#TODO: split read string, iterate through list of all words and everytime 1 of 4 words comes up, 
#prompt user to replace said word with input word, replace, continue
# file_read.split(' '),

#TODO: rejoin list with ' '.join(split_string) and print to screen




