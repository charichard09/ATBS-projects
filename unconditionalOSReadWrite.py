# Program that will read and write to a file stored in the home directory regardless of operating system

from pathlib import Path
import os

print("The current directory is: " + os.getcwd())
os.chdir(Path.home())
print("The path has now been changed to the home directory of: " + os.getcwd())

# Using with open() to open, but could also have used file_obj_variable = open()
with open(Path(os.getcwd()) / "unconditional_OS.txt", "w+") as file_obj_variable:
    file_obj_variable.write("Hello World!")

    # Content not printing solved: without seek(), read() was reading from the end of where write("Hello World!") left off.
    # Use seek(byte_position) to set file position back to byte 0, then read again.
    file_obj_variable.seek(0)

    content = file_obj_variable.read()
    print(content)