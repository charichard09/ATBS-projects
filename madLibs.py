#Program that reads a text file and replaces the words ADJECTIVE, NOUN, ADVERB, or VERB with a prompted user input,
#then create a new file with the new words in place of the old words and print to screen.
#Date: 6-8-2021 #Dev: Richard Cha

import os, sys, copy, re

#open file as r+ and read to variable
mad_libs_fo = open(os.path.dirname(sys.argv[0]) + "/madLibs.txt", 'r+')

mad_libs_text = mad_libs_fo.read()

mad_libs_fo.close()

#split read string, iterate through list of all words and everytime any of 4 words comes up, 
#prompt user to replace said word with input word, replace, continue
mad_libs_list = mad_libs_text.split(' ')

#split() method will split words with punctuation causing the program to not recognize words
#Find out way to remove punctuation
#Solution: remove punctation from words in mad_libs_list using regex and re.sub()
ml_list_no_punc = copy.copy(mad_libs_list)

#\W will match any character that is NOT a "word" character. That includes digits, letters, and spaces.
punctuation_regex = re.compile(r"\W")

for j in range(len(ml_list_no_punc)):
    ml_list_no_punc[j] = punctuation_regex.sub('', ml_list_no_punc[j])


for i in range(len(mad_libs_list)):
    if ml_list_no_punc[i] in ["ADJECTIVE", "VERB", "NOUN", "ADVERB"]:
        answer = input("Please enter a " + ml_list_no_punc[i].lower() + ":\n")
        #Reattach punctation if punctation was found in original string containing ADJ, VER, NOU, ADV
        if punctuation_regex.search(mad_libs_list[i]) != None:
            punctuation_mo = punctuation_regex.search(mad_libs_list[i]) 
            mad_libs_list[i] = answer + punctuation_mo.group()
        else:
            mad_libs_list[i] = answer 

#rejoin list with ' '.join(split_string) and print to screen
print(' '.join(mad_libs_list))



