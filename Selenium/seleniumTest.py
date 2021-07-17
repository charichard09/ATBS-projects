# Program to test the selenium module
# Date: 07-17-21 Dev: Richard C.

from selenium import webdriver

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("http://inventwithpython.com")