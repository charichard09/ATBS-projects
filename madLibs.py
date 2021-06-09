#Program that reads a text file and replaces the words ADJECTIVE, NOUN, ADVERB, or VERB with a prompted user input,
#then create a new file with the new words in place of the old words and print to screen.
#Date: 6-8-2021 #Dev: Richard Cha

import os, sys

#open file as r+ and read to variable
mad_libs_fo = open(os.path.dirname(sys.argv[0]) + "/madLibs.txt", 'r+')

mad_libs_text = mad_libs_fo.read()

mad_libs_fo.close()

#split read string, iterate through list of all words and everytime any of 4 words comes up, 
#prompt user to replace said word with input word, replace, continue
mad_libs_list = mad_libs_text.split(' ')

#TODO: split() method will split words with punctuation causing the program to not recognize words
#Find out way to remove punctuation
for i in range(len(mad_libs_list)):
    if mad_libs_list[i] in ["ADJECTIVE", "VERB", "NOUN", "ADVERB"]:
        answer = input("Please enter a " + mad_libs_list[i].lower() + ":\n")
        mad_libs_list[i] = answer

#rejoin list with ' '.join(split_string) and print to screen
print(' '.join(mad_libs_list))



