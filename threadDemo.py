# Example program provided by ATBS to showcase multithreading and threading module

import threading, time

print("Start Program.")

def take_a_nap():
    time.sleep(5)
    print("Wake Up!")

thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print("End Program.")