#This program counts how long a string is.

answer = input("What is the sentence you would like me to count?\n")
j = 0
for i in answer:
    j += 1

print("This string is " + str(j) + " characters long")