# Program that will take a command line argument, open a browser and search the argument, then open the top search results in new tabs
# Date: 06-25-21 Dev: Richard C.

import requests, sys, webbrowser, bs4

# Get search keyword from command line arguments

print("Googling...")

# Create a response object from hyperlink google search + .join on all arguments 1 or more
res = requests.get("http://google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve the search results page
webpage_BSO = bs4.BeautifulSoup(res.text, "html.parser")

# Opens a browser tab for each result
webpage_tagO = webpage_BSO.select("div .g a")

print(str(webpage_tagO[0]))

num_open = min(5, len(webpage_tagO))
for i in range(num_open):
    webbrowser.open("http://google.com" + webpage_tagO[i].get('href'))