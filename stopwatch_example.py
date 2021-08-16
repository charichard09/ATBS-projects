# Example from ATBS that uses the time module to make a stopwatch program
# Date: 08-16-21 Dev: Richard C.

import time

# Display the programs instructions
input("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.\n")
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap #{lap_num}: {total_time} ({lap_time})", end='')
        lap_num += 1
        last_time = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handl the Ctrl-C exception to keep its error message from displaying.
    print("\nDone.")
