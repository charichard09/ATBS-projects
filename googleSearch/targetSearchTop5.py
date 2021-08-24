# Program that will open the first 5 matches found on Target.com of the keyword/s provided by the user
# Date: 07-02-21 Dev: Richard C.

import requests, bs4, webbrowser

target_site = "https://www.target.com/"

search_this = input("What would you like to search for? \n")

# Create search URL using Amazons base search url is "http://www.target.com/s?searchTerm=" and download its html
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}

search_res_obj = requests.get(target_site + "s?searchTerm=" + search_this.replace(' ', '+'), headers=headers)
search_res_obj.raise_for_status()

search_bs_obj = bs4.BeautifulSoup(search_res_obj.text, "html.parser")
target_tag_matches = search_bs_obj.select("div[data-test='product-list-containter'] ul li")
    #"div .h-display-flex a")

print(len(target_tag_matches))

for i in range(len(target_tag_matches)):
    print(target_tag_matches[i])

#TODO: Search search_bs_obj for all CSS selector matches top 5 non "sponsored" results
#for i in range(1, 6):
#   print(search_bs_obj.select(f"div[data-cel-widget='search_result_{i}']"))



#webbrowser.open(search_this)
