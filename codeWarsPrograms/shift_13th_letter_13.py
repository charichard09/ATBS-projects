# Program (called ROT13 on Codewars) that will iterate through a string and replace every 13th letter with the letter 13 places away from it in 
# the alphabet. Will ignore any symbols or numbers.
# Date: 10/27/21 Dev: Richard C.

import re

def rot13(message):

    # Create variable list for double alphabet "abcdefghijklmnopqrstuvwxyzabcdefghijklm" to find letter +13 away, define other variables 
    alphabet13 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    counter = 0

    # convert message into list and assign to answer so on every "13th letter message/alphabet+13 match conversion" event, answer is mutable and
    # can be changed, then once finished, re-join answer into string and return as final answer
    answer = list(message)


    # Make a while loop if counter < 13; continue, for each loop, iterate through each index of string and if value at index is
    # in the alphabet, increment counter
    for i in range(len(message)):
        if message[i].isalpha() == True:
            counter +=1

        # Once counter == 13; counter = 0; replace current index of string to letter 13 letters from current index character 
        if counter == 13:
            counter = 0
            # Iterate and search for index char in alphabet variable, once index char i == j in alphabet string, get index of j,
            # replace i with index of j+13; continue
            for j in range(len(alphabet13)):
                if message[i] == alphabet13[j]:
                    answer[i] = alphabet13[j+13]      # for index i where the 13th char was found, change index i of temp to letter in alpha +13
                    break

                    # ERROR: IndexError     no breaking out of for loop means message[i] == alphabet13[j] will first correctly match similar 
                    # indexes and return correct letter swap, then will continue the for loop matching character message[i] a second time with 
                    # the repeated alphabet in alphabet13, but this time adding 13 to alphabet13 brings it out of index range.
                    # Problem solved by breaking out of loop on first match.
    answer = "".join(answer)          # re-join temp into a string and reassign to answer
    print(answer)

# Test rot13
rot13("""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
""")




    # First idea using regular expressions

    # TODO: Create regex for simple aphabetical character

    # TODO: Problem: Any character at index[13] of the alphabet + 13 will exceed the alphabet.
    # Possible solution: create a string of 2 alphabets (i.e. new_string = "a-z" * 2)

    # TODO: Iterate through given string, each time checking regex_match_object to character. If match, possibly use regex_obj.sub() method?