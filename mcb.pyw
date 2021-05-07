# Multiclipboard. This program when ran from the command line will, depending on the argument "save 'keyword" or "list", save what is currently
# copied on the clipboard to mcb.pyw, or list what is currently saved on mcb.pwy onto clipboard to be pasted.
# Date: 5-6-21 

import sys, pyperclip

#Check command line argument argv[1] for keyword save, list, or error for any other input
def multiclipboard(argument):
    if argument == "save":
    #IF save, then save clipboard content under save "keyword" name 

    elif argument == "list":
    #IF list, then copy all saved keywords values to the clipboard

    else:
        print("     ERROR: A valid argument of either save or list was not provided. Please rerun program.")

# 

multiclipboard(argv[1])