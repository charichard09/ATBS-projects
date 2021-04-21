import traceback

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

try:
    raise Exception("This is the error message.")
except:
    #open or create errorLog.txt >> open and assign file object to errorLog
    errorLog = open("errorLog.txt", "w")
    logging.debug("errorLog is type: " + str(type(errorLog)))
    #write error traceback to errorLog.txt
    errorLog.write(traceback.format_exc())
    errorLog.close()
    print("The traceback error has been logged to errorLog.txt")