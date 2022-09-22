# Program that will walk the cwd and print a list of all folders and files in the directory
# Date: 06-15-21 Developer: Richard Cha

import os, sys

for dir_path, dir_name, file_name in os.walk(os.path.dirname(sys.argv[0]) + "/text2Search", topdown=False):
    print("This folder " + dir_path + " contains files:\n" + '\n'.join(file_name))
    if len(file_name) == 0:
        print("None found\n")
    print("\nAnd has folders: \n" + '\n'.join(dir_name))
    if len(dir_name) == 0:
        print("None found\n")