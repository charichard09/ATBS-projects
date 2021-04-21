import requests
import traceback

#get website and store in variable res as response object
res = requests.get("https://automatetheboringstuff.com/does_not_exist")

#raise_for_status() method function on res response object to confirm download went smoothly
try:
    res.raise_for_status()
except Exception as err:
    print("There was a problem: %s" % (err))
#open errorLog.txt and save traceback to errorLog.txt
    error_log_FO = open("errorLog.txt", "w")

    error_log_FO.write(traceback.format_exc())

    error_log_FO.close()

type(res)

#res.status code returns the status code for the response object res. That status code can be 200 for "OK" or the familiar 404 for "Not Found"
#requests.codes.ok() returns 200, so if res.status_code == requests.codes.ok is True then website was scraped
res.status_code == requests.codes.ok

len(res.text)

#print(res.text[:250])
