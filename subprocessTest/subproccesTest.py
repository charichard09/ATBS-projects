# Program to test subprocess module

import subprocess

p_open_obj = subprocess.Popen([r"C:\Windows\System32\notepad.exe", r"C:\Users\chari\Documents\hello.txt"])
print(p_open_obj.poll() == None) # if .poll() == None, program is still running, else return terminate code 0 or 1
print(p_open_obj.wait()) # .wait() will wait until program closes, then return 0
print(p_open_obj.poll()) # return 0 if program terminated correctly after wait