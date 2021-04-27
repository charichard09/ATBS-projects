#Script that changes cwd to directory of script, downloads a websites html code, and saves it to a file inside cwd.

import requests, os, sys

#Check to see if example.html exists, if not, download example.html from url provided in ATBS pg.245
os.chdir(sys.path[0])
if not os.path.exists("example.html"):    
    example_ro = requests.get("http://nostarch.com/automatestuff/")
    example_ro.raise_for_status()
    file_example = open("example.html", "wb")
    for chunk in example_ro.iter_content(10000):
        file_example.write(chunk)
    file_example.close()