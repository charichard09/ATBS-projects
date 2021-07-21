# Program to test the selenium module
# Date: 07-17-21 Dev: Richard C.

from selenium import webdriver
import webbrowser

food = input("What food item would you like to look up today?\n")

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.google.com")

try:
    input_elem = browser.find_elements_by_tag_name("input")
    #print("Found href to %s !" % (elem.get_attribute("href")))
    input_elem[0].send_keys(food + " calories")

    # Using submit() method to submit text in input element index 0
    input_elem[0].submit()

    # Can also use click() method on input element index 3 which is the Google Search button 
    #print(input_elem[3].get_attribute("value"))
    #input_elem[3].click()
except:
    print("Was not able to find an element with that name.")

