# Program that will read and write to a file stored in the home directory regardless of operating system

from pathlib import Path
import os

print("The current directory is: " + os.getcwd())
os.chdir(Path.home())
print("The path has now been changed to the home directory of: " + os.getcwd())

