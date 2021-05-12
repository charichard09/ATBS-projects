#This function is_phone_number takes a string and checks if that string matches the pattern of a phone number and returns True or False.
#Version: 1.0 Date: 030221 

def is_phone_number(text):                                                         #text is checked against patterns of a phone number 
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True                                                                 #If text passes all checks, then it must be a phone number format and returns True

message = "Call me at 415-432-7895 tomorrow. 415-321-5647 is my office."
for i in range(len(message)):       
    chunk = message[i:i+12]                                                     #Cool syntax for each iteration of i, puts slice of 12 characters into chunk to be checked /w is_phone_number()   
    if is_phone_number(chunk):                                                  #i.e. when i is 2, chunk = message[2:14], or chunk = "ll me at 415"  
        print("Phone number found: " + chunk)
print("Done")