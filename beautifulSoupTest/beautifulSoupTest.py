#This program gets a request object from a website, then passes it to the bs4 BeautifulSoup module to 
#create a BeautifulSoup object to allow easy html parsing of websites

import requests, bs4

reso = requests.get("http://nostarch.com")
#Always raise_for_status a get request to raise an exception if download of website did not succeed
reso.raise_for_status()
no_starch_BSO = bs4.BeautifulSoup(reso.text)
type(no_starch_BSO)
