#This is a practice program to test the limits of try: except: and try: except Exception as err:
#Version 1.0 Date: 032821

import re

def pst_to_est():
    time_regex = re.compile(r"(\d+):\d\d\s(am|pm)", re.IGNORECASE)
    time = input("What time is it? (hour:minutes am/pm, i.e. 3:30 am)\n")
    mo1 = time_regex.match(time)
    if mo1 == None:
        raise Exception("Time must be in hour:minutes am/pm format, i.e. 4:30 pm.")
    print(time + " pst to est is " + str((int(mo1.group(1)) + 3)) + mo1.group(2))
while True:
    try:
        pst_to_est()
    except Exception as err:
        print("An exception has occured: " + str(err))
        continue
    break

#The difference between try and except: and try and except Exception as error: is that when an exception has occured in just except (errorCode): the program goes directly to executing 
#the code under the except (errorCode): syntax, whereas with try and except Exception as error: when the "raise Exception("string attribute")" syntax raises an error, it has attributes
#like the "string attribute" attached to the error object that can be called upon directly after the except Exception as error: occurs, where error is a variable that has stored 
#the expections attributes.