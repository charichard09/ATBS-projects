#This program runs a basic password manager program.
#version: 1.0    date:022421

import pyperclip, sys

PASSWORDS = {"email": "U\sFPPN%3VGWp&4E",
            "blog": "S*-%qAZReMu=5e7M",
            "luggage": "12345"}

if len(sys.argv) < 2:
    print("Usage: Python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]                                   #first command line if arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no account named " + account)