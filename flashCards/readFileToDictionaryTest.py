#Write program to find out what happens when you "file_object.read()" a file already containing quotes ("")
#i.e. what happens when reading flashCards test.txt

import sys, os

#os.path.dirname(sys.argv[0]) will return a string of readFileToDictionaryTest.py's directory path, which we assume read_to_dict.txt is also in
read_to_dict_fo = open(os.path.dirname(sys.argv[0]) + "/read_to_dict.txt", 'r')

read_to_dict_text = read_to_dict_fo.read()

read_to_dict_fo.close()

print(read_to_dict_text)

#TODO: Create a regular expression to isolate text inbetween string "Questions on {topic}" and "Questions on {following topic}"

questions_answers = read_to_dict_text.split('\n')

quest_ans_dict = {}

for i in range(len(questions_answers)):
    if ':' in questions_answers[i]:
        temp_dict = questions_answers[i].split(':')
        quest_ans_dict[temp_dict[0]] = temp_dict[1]

#Ask a random question from quest_ans_dict (random key), let user input their answer, then print the answer (value) of question (key)
for j in range(len(quest_ans_dict)):
    user_answer = input(list(quest_ans_dict.keys())[j] + "\n\n")
    print('\n' + quest_ans_dict[list(quest_ans_dict.keys())[j]] + '\n')

#Exit prompt to user
print("That's all the questions. Great job!")
