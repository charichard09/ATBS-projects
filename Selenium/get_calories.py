# A function that will ask the user for a food and return the caloric intake of that food using Selenium
# and requests/beautifulsoup
# Date: 07-21-2021 Dev: Richard C.

from selenium import webdriver
import requests, bs4

#def get_calories(food):
    
answer = input("What would you like to search?\n")

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# TODO: search the food using myfitnesspal food search
browser.get("https://www.myfitnesspal.com/food/search")
search_box = browser.find_element_by_tag_name("input")
search_box.send_keys(answer)
search_box.submit()

# TODO: print the top 1-5 options and ask the user to select 1 or none
print(browser.current_url)

# Need to imitate fake browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',}

search_page = requests.get(browser.current_url, headers=headers)
search_page.raise_for_status()

print(search_page.encoding)
search_page.encoding = "utf-8"
# use .text method on search_page request object to return text of request object to then be made into bs object
bs4_search = bs4.BeautifulSoup(search_page.text, "html.parser")

#to see html doc: print(bs4_search.prettify())

#.jss120 is .jss65 when requests.get() downloads html
result_names = bs4_search.select(".jss65")
result_calories = bs4_search.select(".jss70")

calories = result_calories[0].getText()

#calories = calories.decode('utf-8')
print(calories)

print(len(result_names))
print(result_names[0].getText() + '\n' + calories)

# TODO: retry, quit, or if an option is selected, return calorie value of item


# Ask the user what to look up and call function
#answer = input("What would you like to search?\n")
#get_calories(answer)