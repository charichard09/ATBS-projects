#Script that tests the soup_object.select() method included in the Beautiful Soup module.

import bs4

exampleFile = open("beautifulSoupTest\\html_example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")

print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)