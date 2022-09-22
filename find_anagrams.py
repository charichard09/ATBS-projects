#  Anagrams are words that contain the same characters and number of characters in any order (i.e. "abba" and "baab")
#  Write a function that finds all the anagrams of a given word from a list, and returns those words in a list.
#  Date:  12-18-21    Dev: Richard Cha

def anagrams(word, words):
    unique_word_letters = {}
    unique_words_letters = {}
    unique_character = ""
    found_anagrams = []

    #  if word is empty, return []
    if len(word) == 0:
        return found_anagrams

    #  iterate through word and use count() function on each unique character and save in a dictionary. 
    #  for i in word:; i = unique_character; word.count(unique_character)
    for letter in word:
        if unique_character != letter:
            unique_character = letter
            unique_word_letters[unique_character] = word.count(unique_character)

    #  iterate through the list words, for each iteration, count how many of each character is in the word and save to dictionary.
    for word_in_list in words:
        unique_character = ""
        for letter in word_in_list:
            if unique_character != letter:
                unique_character = letter
                unique_words_letters[unique_character] = word_in_list.count(unique_character)

        #  compare both dictionaries, if they match, word is an anagram so save to a new list.
        if unique_word_letters == unique_words_letters:
            found_anagrams.append(word_in_list)
        
        unique_words_letters = {}


    return found_anagrams


#  Test: answer should be ["aabb", "bbaa"]
print(anagrams("ab", ["ab", "ba"]))