#This program finds the factorial of a number given. It utilizes the debugging tool Logging and the logging module to timestamp instances of the code where logging.debug() are so the programmer can confirm 
#correct values of variables, areas of code have been executed, etc. 
#Version 1.0 Date: 4/3/2021

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

#Comment in or out to enable or disable logging
#logging.disable(logging.CRITICAL)

logging.debug("Start of program")

def factorial(n):
    logging.debug("Start of factorial(%s%%)" % (n))
    if not n.isdigit():
        raise Exception("       ERROR: You must enter a whole number.")
    total = 1
    for i in range(1, int(n) + 1):
        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug("End of factorial(%s%%)" % (n))
    return total

answer = input("What number would you like factorialed?\n")

#Raise Exception error if answer is not an int
try:
    print(factorial(answer))
except Exception as error:
    print(error)

logging.debug("End of Program.")

