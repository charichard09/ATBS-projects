#Script that can either create new flash cards, or review previous flash cards.
#Date: 05-11-2021 

def create_Flash_Cards():
    #TODO: Create new flashcard function
    chapt_topic = input("What chapter or topic will we be adding these flash cards to?\n")

    #Either create heading "Questions on X" or find end of "Questions on X" to append more questions:answer flash cards
    while True:
        question = input("\nWhat is the question:\n")
        answer = input("\nWhat is the answer:\n")

        #open flashCards.txt and write "question:answer" underneath "Questions on X"

        yes_no = input("Would you like to add another Question/Answer?\n")
        if yes_no == "yes":
            continue
        if yes_no == "no":
            break

    

def review_Flash_Cards():
    #TODO: Create script to extract old flash cards and test.
    chapter = input("""What chapter would you like to be quizzed on?
    
    Please type "Questions on (CH.1 - CH.X, HTML, General).\n\n""")

    #create regular expression "Questions on CH.X and everything underneath until stopping at Questions on" 

    #search for CH.X in file and read lines stopping at "Questions on" which marks beginning of next topic

    #IDEA: Can do dictionary[question] = answer to add read questions:answer's from file. 
    #Then iterate through dictionary.keys() and dictionary[i] where i is "i in dictionary.keys():"

while True:
    answer = input("""What would you like to do?
                  
                  1. Create new flash cards.
                  2. Review old flash cards.
                  
Please enter the corresponding number: """)

    if answer == '1':
        create_Flash_Cards()
        break
    elif answer == '2':
        review_Flash_Cards()
        break
    else:
        print("\n         ERROR: Input must be one of the options provided.\n")
        continue