# A function that will ask the user for a food and return the caloric intake of that food using Selenium
# and requests/beautifulsoup
# Date: 07-21-2021 Dev: Richard C.

from selenium import webdriver
import requests, bs4

def calories(food):
    
    PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
    browser = webdriver.Chrome(PATH)

    # TODO: ask the user what food they would like looked up

    # TODO: search the food using myfitnesspal food search

    # TODO: print the top 1-5 options and ask the user to select 1 or none

    # TODO: retry, quit, or if an option is selected, return calorie value of item