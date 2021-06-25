# Program that walks a folder tree and copies all files of a certain extension (.jpeg, .txt, .html) to a new folder names "backup"

import os, shutil, sys

# TODO: Print "What extension type will we be copying today?" 
# extension = input("")

extension = input("This is a program that will backup any file type to a new folder. \nWhat extension type will we be backing up today?\n")

# TODO: Get cwd and print "The current directory is _____" 
# Ask user "Would you like to search the current directory? (y/n)"
# if 'n' have user input the absolute address of the directory to be searched and copied
# if 'y' continue forward

directory = os.path.dirname(sys.argv[0])
answer = input("The current directory is \n" + directory + "\nWould you like the search the current directory? (y/n)\n")

if answer == 'n':
    directory = input("Please enter the absolute path to the correct directory:\n")

# TODO: # create new folder using mkdir() called "backup"
# Walk the directory and print all files and folders
# iterate through directories, if extension in file name is true, copy it to new folder

if os.path.isdir(f"{directory}/backup"):
    print(f"Copied files will be put in {directory}/backup")
elif not os.path.isdir(f"{directory}/backup"):
    os.mkdir(f"{directory}/backup")
    print(f"Copied files will be put in {directory}/backup")

assert os.path.isdir(f"{directory}/backup"), "Something went wrong. Backup folder not created."

