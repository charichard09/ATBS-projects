#This program searches through text that has been copied to the computers clipboard for any email addresses and phone numbers.
#Version: 1.0 Date: 031421

import pyperclip
import re

copied_text = pyperclip.paste()    #paste/assign copied text to be searched to a variable

def is_phone_email(text):
    phone_regex = re.compile(r"(\d\d\d|\(\d\d\d\))(\s|-|\.)?(\d\d\d)(\s|-|\.)?(\d\d\d\d)")    #create 2 regex for an email and a phone number
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}")

    mo_phone = phone_regex.findall(text)    #findall() through text for both regex'
    mo_email = email_regex.findall(text)    #format tuple into single string to print
    
    #include message if none is found
    if mo_phone == []: 
        print("No phone number found.".center(40))
    else:
        print("Phone numbers found:".center(40))
        for i in range(len(mo_phone)):
            print("".join(mo_phone[i]).center(40))
        
    if mo_email == []:
        print("\n" + "No email found.".center(40))
    else:
        print("\n" + "Emails found:".center(40))
        for i in range(len(mo_email)):
            print(mo_email[i].center(40))

is_phone_email(copied_text)     #call is_phone_email(copied_text)