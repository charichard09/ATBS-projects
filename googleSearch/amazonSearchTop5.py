# Program that will open the first 5 matches found on Amazon.com of the keyword/s provided by the user
# Date: 07-02-21 Dev: Richard C.

import requests, bs4, webbrowser

amazon_site = "http://www.amazon.com/"

search_this = input("What would you like to search for? \n")

# Create search URL using Amazons base search url is "http://www.amazon.com/s?k=" and download its html
search_res_obj = requests.get(amazon_site + "s?k=" + search_this.replace(' ', '+'))
search_res_obj.raise_for_status()

search_bs_obj = bs4.BeautifulSoup(search_res_obj.text, "html.parser")

#TODO: Search search_bs_obj for all CSS selector matches top 5 non "sponsored" results
for i in len(1, 6):
    print(search_bs_obj.select(f"div[data-cel-widget='search_result_{i}']"))



#webbrowser.open(search_this)
