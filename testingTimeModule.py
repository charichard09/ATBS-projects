# Simple given program from Automate The Boring Stuff to test time.time() function 

import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 10000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The result is %s digits long." % len(str(prod)))
print(f"Took {endTime - startTime} to calculate.")