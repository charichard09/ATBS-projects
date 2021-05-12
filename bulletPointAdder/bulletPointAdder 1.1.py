#! python
#This program pastes a copied text, adds "* " to the beginning of each new line, and copies it back to the clipboard for pasting.
#version 1.1: removed the need to declare blank variable, and keep adding each modified line in .split list to created blank variable
#with the .join method function, which joins a list of strings into a single string (syntax: joinedBy.join(list)) 

import pyperclip

text = pyperclip.paste()                            #paste copied text into text variable
temp_text = text.split("\n")                        #.split method funtion to split string into a list where every new line occurs (creates a list of each line in the copied text)    

for i in range(len(temp_text)):                     #i is that string of that position
    temp_text[i] = "* " + temp_text[i]              #concatenate string of i with the correct formatting "* " at the beginning and "\n" at the end and assign to i
    
text = "\n".join(temp_text)

pyperclip.copy(text)                           #copy new copy_this string to clipboard