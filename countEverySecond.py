# Program to test how long it takes to time.sleep(30) seconds and for loop time.sleep(1) second 30 times

import time

counter = 1

# Figure out execution time of 1 loop of a time.sleep() counter
begin_time = time.time()
for i in range(2):
    print(round((time.time() + counter) - time.time()))
    time.sleep(1)
    counter += 1
end_time = time.time() - 2

print(round(end_time - begin_time, 8))
# Hypothesis: To loop correctly 1second everytime, subtract calculated execution time above from 1 second when calling time.sleep() because
# actual execution time + (1 second - calculated execution time) should equal 1 second
# 8-16 Update: sleep method at 0 had 0 execution time, by setting to 1 execution time was discovered and hypothesis seems to be correct.
counter = 1

for i in range(30):
    print(round((time.time() + counter) - time.time()))
    time.sleep(1 - (end_time - begin_time)/2)
    counter += 1
