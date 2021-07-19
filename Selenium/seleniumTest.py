# Program to test the selenium module
# Date: 07-17-21 Dev: Richard C.

from selenium import webdriver
import webbrowser

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("http://inventwithpython.com")

try:
    link_elem = browser.find_element_by_link_text("Buy on Amazon")
    #print("Found href to %s !" % (elem.get_attribute("href")))
    link_elem.click()
except:
    print("Was not able to find an element with that name.")

#webbrowser.open(elem.get_attribute("href"))
#elem.click()