# Simple alarm clock using time and datetime modules
# Date: 8-18-2021 Dev: Richard C.

import time, datetime, winsound

timer = datetime.datetime.strptime((datetime.datetime.now().strftime("%Y-%m-%d")) + " " + input("Please enter what time to set alarm (8:00am)\n"), "%Y-%m-%d %I:%M%p")

print(timer)
print(datetime.datetime.now())

while datetime.datetime.now() < timer:
    time.sleep(1)

freq = 440 # hertz
duration = 500 #milliseconds

for i in range(3):
    winsound.Beep(freq, duration)


