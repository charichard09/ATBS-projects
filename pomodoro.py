# Pomodoro technique
# Date: 8-16-2021 Dev: Richard C.

import time, winsound, datetime

# TODO: Ask user how long to set first pomo duration. Then ask user if they'd like to add another pomo duration. When no 
# further times are wanted, prompt "press Enter to begin."
to_loop = "y"
number = 1
loop_names = {"Break": 300, "Loop 0": 2}
freq = 440 # Hz
duration = 500 # milliseconds

while to_loop == "y":
    # Get pomo duration in minutes, convert to seconds, save into dictionary
    answer = 60 * int(input(f"How long would you like to set pomodoro duration {number}? (in minutes, break time is auto added)\n"))

    # Check if answer is int
    if isinstance(answer, int):
        loop_names[f"Loop {number}"] = answer
    else:
        continue

    number += 1
    to_loop = input("Would you like to add another pomo duration to this session? (y/n)\n")

print(loop_names)
input("Press Enter to begin.\n")

# TODO: Use time.time() and execution time compensation to go through duration and print timer along the way.
for i in range(number + 1):
    #figure out compensation needed for execution time by running 1 loop
    if i == 0:
        start_time = time.time()
        if f"Loop {i}" in loop_names:
            for j in range(loop_names[f"Loop {i}"]):
                print(datetime.datetime.now())
                time.sleep(1)
        compensation_time = ((time.time() - 2) - start_time) / 2
        continue

    if f"Loop {i}" in loop_names:
        for j in range(loop_names[f"Loop {i}"]):
            print(datetime.datetime.now())              # temporary to see if time is correct
            time.sleep(1 - compensation_time)

    # TODO: When timer hits inputted duration, stop and sound an alarm using winsound.Beep()
    for amt_beeps in range(4):
        winsound.Beep(freq, duration)

    # TODO: Ask user to press ENTER when ready for 5 min interval. Reset loop (could also recall as function)
    input("Pomodoro time is done. Press Enter to start Break.\n")

    for k in range(loop_names["Break"]):
        time.sleep(1 - compensation_time)
    
    for amt_beep in range(4):
        winsound.Beep(freq, duration)

    input("Break is over. Press Enter to start next loop or end.\n")

# TODO: In the future, possibly using Shelve variable storage, ask user if theyd like to store time inputs into shelve to be recalled 
# next time script is ran