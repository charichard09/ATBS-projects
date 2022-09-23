#! python
#This program pastes a copied text, adds "* " to the beginning of each new line, and copies it back to the clipboard for pasting.

import pyperclip

text = pyperclip.paste()                            #paste copied text into text variable
temp_text = text.split("\n")                        #.split method funtion to split string into a list where every new line occurs (creates a list of each line in the copied text)    
copy_this = ""                                      #empty string to concatenate modified strings to

for i in temp_text:                                 #i is that string of that position
    i = "* " + i + "\n"                             #concatenate string of i with the correct formatting "* " at the beginning and "\n" at the end and assign to i
    copy_this += i                                  #add i first to the blank copy_this string, then to itself for each iteration of the for loop

pyperclip.copy(copy_this)                           #copy new copy_this string to clipboard