# Program that will download current and previous img's of a webcomic from webside xkcd.com and save it to the hard drive.
# Date: 7-10-21 Dev: Richard C.copying ATBS

import requests, os, bs4

url = "http://xkcd.com"
os.makedirs("xkcd", exist_ok=True)

for i in range(0, 6):

    # Download the page.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find an image.")
    else:
        comic_url = "http:" + comic_elem[0].get("src")
        # Download the image.
        print("Downloading the image %s..." % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd.
    image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select("a[rel='prev']")
    url = "http://xkcd.com" + prev_link[0].get("href")

print("Done.")