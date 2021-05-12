#Script that can either create new flash cards, or review previous flash cards.
#Date: 05-11-2021 

def create_Flash_Cards():
    #TODO: Create new flashcard function
    print("place holder")

def review_Flash_Cards():
    #TODO: Create script to extract old flash cards and test.
    print("place holder")

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