#  Anagrams are words that contain the same characters and number of characters in any order (i.e. "abba" and "baab")
#  Write a function that finds all the anagrams of a given word from a list, and returns those words in a list.
#  Date:  12-18-21    Dev: Richard Cha

def anagrams(word, words):
    #  TODO: if word is empty, return []


    #  TODO: iterate through word and use count() function on each unique character and save in a dictionary. 
    #  for i in word:; i = unique_character; word.count(unique_character)


    #  TODO: iterate through the list words, for each iteration, count how many of each character is in the word and save to dictionary.


        #  TODO: compare both dictionaries, if they match, word is an anagram so save to a new list.


    return words


#  Test: answer should be ["aabb", "bbaa"]
anagrams("abba", ["aabb", "abcd", "bbaa", "dada"])