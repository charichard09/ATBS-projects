# A function that will ask the user for a food and return the caloric intake of that food using Selenium
# and requests/beautifulsoup
# Date: 07-21-2021 Dev: Richard C.

from selenium import webdriver
import requests, bs4, os, sys, subprocess

#def get_calories(food):
    
answer = input("What would you like to search?\n")

PATH = r"C:\Users\chari\Documents\Python Programs\ATBS Scripts and Projects\Selenium\chromedriver.exe"
browser = webdriver.Chrome(PATH)

# Search the food using myfitnesspal food search
browser.get("https://www.myfitnesspal.com/food/search")
search_box = browser.find_element_by_tag_name("input")
search_box.send_keys(answer)
search_box.submit()

print("website: " + browser.current_url)

# Need to imitate fake browser user info
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',}

# Download webpage of searched results
search_page = requests.get(browser.current_url, headers=headers)
search_page.raise_for_status()

# Print default encoding and then assign encoding to utf-8
print("converting " + search_page.encoding + " to utf-8\n")
search_page.encoding = "utf-8"

# use .text method on search_page request object to return text of request object to then be parsed into bs object
bs4_search = bs4.BeautifulSoup(search_page.text, "html.parser")

# See html doc with statement print(bs4_search.prettify())
# .jss120 is .jss65 when requests.get() downloads html
result_names = bs4_search.select(".jss65")
result_calories = bs4_search.select(".jss70")

# Print top 5 matches 
print(f"Found {len(result_names)} matches.\nNow showing top 5 matches...\n")

for i in range(5):
    try:
        print(result_names[i].getText() + '\n' + result_calories[i].getText() + "\n")
    except IndexError:
        break

browser.close()

# TODO: retry, ask for next 5 results, or end
answer = input("Would you like to retry (r), get the next 5 search results (n), or end (e)? \n")

if answer == 'r':
    subprocess.Popen(["C:\\Users\\chari\\Documents\\Python Programs\\ATBS_Scripts_and_Projects_envs\\beautifulSoupTest_env\\Scripts\\python.exe", "Selenium\\get_calories.py"])

# TODO: if an option is selected, ask "1 serving is {x}, how many estimated servings did we have?" 
# calculate {x}:servings ration and return {y}:calories ratio, return calorie value of item

# turn get_calories into function, ask the user what to look up and call function
# answer = input("What would you like to search?\n")
# get_calories(answer)