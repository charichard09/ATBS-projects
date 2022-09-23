#This is a practice program for Raising Exceptions that takes a symbol, a height, and a width >> prints a box of said dimensions with the symbol >> intentionally raises an Exception on the third input
#Version 1.0 Date: 032821

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must consist of 1 character")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    
    print(symbol * width)                                                  #print base of box
    for i in range(height -2):                                             #print middle of box
        print(symbol + (" " * (width - 2) + symbol))
    print(symbol * width)                                                  #print top of box

for sym, w, h in (("*", 4, 4), ("0", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as error:
        print("An exception has occured: " + str(error))
