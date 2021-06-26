# Program that will take a command line argument, open a browser and search the argument, then open the top search results in new tabs
# Date: 06-25-21 Dev: Richard C.

import requests, sys, webbrowser, bs4

# Get search keyword from command line arguments

print("Googling...")

# Create a response object from hyperlink google search + .join on all arguments 1 or more
res = requests.get("http://google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve the search results page

#TODO: Opens a browser tab for each result

