# Multiclipboard. Saves and loads pieces of test to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
# Date: 5-10-21 

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.
#sys.argv[1] is the second argument in the command line. The first being the name of the file being executed.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    #if argv[1] is save then argv[2] must be the keyword, thus save clipboard content (value) to keyword (key) into mcbShelf
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO: List keywords or load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()