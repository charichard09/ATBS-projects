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
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}

search_page = requests.get(browser.current_url, headers=headers)
search_page.raise_for_status()

browser.close()

# use .text method on search_page request object to return text of request object to then be made into bs object
bs4_search = bs4.BeautifulSoup(search_page.text, "html.parser")

#to see html doc: print(bs4_search.prettify())

#.jss120 is .jss65, different from selenium chrome assumed because fake user is imitating older chrome?
result_names = bs4_search.select(".jss65")
result_calories = bs4_search.select(".jss70")

print(len(result_names))
print(result_names[0].getText() + result_calories[0].getText())

# TODO: retry, quit, or if an option is selected, return calorie value of item


# Ask the user what to look up and call function
#answer = input("What would you like to search?\n")
#get_calories(answer)