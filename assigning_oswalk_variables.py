#  Simple script to test what happens when trying to assign 3 variables to the output of os.walk()
#  Date: 12-18-21 Developer: Richard Cha

import os, sys

#  os.walk outputs a tuple of 3 items. I intended to assign those 3 items to 3 variables respectively. What 
#  ends up happening is dir_path, dir_name, and file_name are unintentionally assigned a tuple instead. This is because
#  os.walk() will return as many tuples as there are folders, including the current working directory. If there is only 1 list or tuple, 
#  Python will automatically assign the items to variables, but if there is more than 1 list or tuple, Python will automatically assign the 
#  lists or tuples to variables. I can iterate through each tuple returned from os.walk() with a "for dir_path, dir_name, file_name in os.walk():" 
dir_path, dir_name, file_name = os.walk(os.path.dirname(sys.argv[0]) + "/text2Search")

print(dir_path, dir_name, file_name)

dir_path1, dir_name1, file_name1 = dir_path

print(dir_path1, dir_name1, file_name1)
