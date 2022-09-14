#  Write a function that will apply the Collatz sequence to any number given by a user. 
#  The Collatz sequence is a recursion type sequence that with any number, depending on it being odd or even, will 
#  do 3 * number + 1 or number // 2 respectively, take the value of that expression and reapply the same condition,
#  until reaching the final number 1.

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 != 0:
            number = 3 * number + 1
            print(number)


collatz(int(input("Please enter any integer: \n")))