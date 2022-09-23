#This program uses a regular expression to test a passwords strength. 
#Version: 1.0 Date: 031621

import re

def password_strength(text):
    strong_pw_regex_upper = re.compile(r"[A-Z]+")
    strong_pw_regex_lower = re.compile(r"[a-z]+")
    strong_pw_regex_number = re.compile(r"\d+")
    strong_pw_regex_length = re.compile(r"[A-Za-z0-9~`!@#$%^&*()_+={[}\]|\\:;\"'<,>.?/-]{8,}")

    if None == strong_pw_regex_upper.search(text):
        print("password is missing an uppercase.")
    elif None == strong_pw_regex_lower.search(text):
        print("password is missing a lowercase.")
    elif None == strong_pw_regex_number.search(text):
        print("password is missing a number.")
    elif None == strong_pw_regex_length.search(text):
        print("password must be 8 or more characters.")
    else:
        print("Congratulations. Your password has passed as strong")


password = input("Please input the password you would like to check:\n")
password_strength(password)