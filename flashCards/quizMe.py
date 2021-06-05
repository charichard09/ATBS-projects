#Write program that reads file "read_to_dict.txt" consisting of questions and answers to dictionaries
#Date: 5-25-21 Developer: Richard Cha

import sys, os, re

def quiz_me():
    #os.path.dirname(sys.argv[0]) will return a string of readFileToDictionaryTest.py's directory path, which we assume read_to_dict.txt is also in
    read_to_dict_fo = open(os.path.dirname(sys.argv[0]) + "/quizQuestions.txt", 'r')

    read_to_dict_text = read_to_dict_fo.read()

    read_to_dict_fo.close()

    #Create a regular expression to look for all current "Questions on x" and print to screen. 
    print("\nCurrent Glossary of Available Questions:")
    available_questions_regex = re.compile(r"Questions\son\s.*")
    available_questions_mo = available_questions_regex.findall(read_to_dict_text)
    print('\n'.join(available_questions_mo))

    #Ask user input of what they'd like to be quizzed on from the options given.
    while True:
        user_topic = input("\nWhat would you like to be quizzed on today? (CH1, Universal Python, etc.)\n")
        if "Questions on " + user_topic in read_to_dict_text:
            break

    #Create a regular expression to isolate text inbetween string "Questions on {topic}" and "Questions on {following topic}"
    quest_ans_regex = re.compile(r"Questions\son\s" + user_topic + r".*Questions\son", re.DOTALL)
    quest_ans_mo = quest_ans_regex.search(read_to_dict_text)

    #Assign all !Q. to a dictionary as keys with respective !A. as values
    questions_regex = re.compile(r"!Q\.\s.*")
    answers_regex = re.compile(r"!A\.\s.*")

    questions_match = questions_regex.findall(quest_ans_mo.group())
    answers_match = answers_regex.findall(quest_ans_mo.group())

    quest_ans_dict = {}

    for i in range(len(questions_match)):
        quest_ans_dict[questions_match[i]] = answers_match[i]

    #Ask a random question from quest_ans_dict (random key), let user input their answer, then print the answer (value) of question (key)
    for j in range(len(quest_ans_dict)):
        user_answer = input('\n' + list(quest_ans_dict.keys())[j] + "\n\n")
        print('\n' + quest_ans_dict[list(quest_ans_dict.keys())[j]] + '\n')

    #Exit prompt to user
    print("\nThat's all the questions. Great job!")

#Add option to be quizzed again
while True:
    quiz_me()
    answer = input("Would you like to be quizzed again, or on another topic? (y/n)\n")
    if answer == 'y':
        continue
    elif answer == 'n':
        break
    else:
        print("     ERROR: invalid input")
        break