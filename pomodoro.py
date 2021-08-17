# Pomodoro technique
# Date: 8-16-2021 Dev: Richard C.

import time, winsound

# TODO: Ask user how long to set first pomo duration. Then ask user if they'd like to add another pomo duration. When no 
# further times are wanted, prompt "press Enter to then begin.""
to_loop = "y"
number = 1
loop_names = []

while to_loop == "y":
    answer = input(f"How long would you like to set pomodoro duration {number}? (in minutes)\n")
    loop_names.append(f"Loop {number}")

    # TODO: instead of using loop_names list, use dictionary to store name and duration together?
    number += 1
    to_loop = input("Would you like to add another pomo duration to this session? (y/n)\n")

print(loop_names)


# TODO: Use time.time() and execution time compensation to go through duration and print timer along the way.

# TODO: When timer hits inputted duration, stop and sound an alarm using winsound.Beep()

# TODO: Ask user to press ENTER when ready for 5 min interval. Reset loop (could also recall as function)

# TODO: In the future, possibly using Shelve variable storage, ask user if theyd like to store time inputs into shelve to be recalled 
# next time script is ran