# Program to test the selenium module
# Date: 07-17-21 Dev: Richard C.

from selenium import webdriver
import webbrowser

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.google.com")

try:
    input_elem = browser.find_elements_by_tag_name("input")
    #print("Found href to %s !" % (elem.get_attribute("href")))
    input_elem[0].send_keys("Pokemon Cards")
    print(input_elem[3].get_attribute("value"))
    input_elem[3].click()
except:
    print("Was not able to find an element with that name.")

