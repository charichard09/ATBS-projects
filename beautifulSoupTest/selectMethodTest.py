#Script that tests the soup_object.select() method included in the Beautiful Soup module.

import bs4

#Trying new statement "with open(file.ext) as i"
with open("beautifulSoupTest\\html_example.html") as exampleFile:
    #exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser"), no need to read() exampleFile, 
    # bs4 can directly convert FileObject to BeautifulSoupObject
    exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
    elems = exampleSoup.select("#author")

    print(type(exampleFile))
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)

#Get data from an element's attributes
soup = bs4.BeautifulSoup(open("beautifulSoupTest\\html_example.html"), "html.parser")
spanElem = soup.select("span")[0]
print(str(spanElem))
print(spanElem.get("id"))
print(spanElem.get("some_nonexistent_addr") == None)
print(spanElem.attrs)