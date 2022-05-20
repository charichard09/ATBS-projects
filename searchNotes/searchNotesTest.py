#  Test to see what happens when opening and reading one of my notes saved as .odt OpenDocument Text files in My Documents folder


#  Try to read Chapter 1.odt file
with open(r"C:\\Users\\chari\\Documents\\Chapter 1.odt", "r") as chapter_1_notes:
    try:
        chapter_1_read = chapter_1_notes.read()
        print(chapter_1_read)
    except UnicodeDecodeError:
        print("UnicodeDecodeError raised")

#  Try to read readMe.txt file
with open(r"C:\\Users\\chari\\Documents\\readMe.txt", "r") as read_me:
    read_me_read = read_me.read()
    print(read_me_read)

#  TODO: Try to read readMeODT.odt file with no predefined software format
with open(r"C:\\Users\\chari\\Documents\\readMeODT.odt", "r") as read_me_ODT:
    try:
        read_me_ODT_read = read_me_ODT.read()
    except UnicodeDecodeError:
        print("UnicodeDecodeError raised")

#  Discovered Python raises a UnicodeDecodeError possibly having trouble opening .odt file format.