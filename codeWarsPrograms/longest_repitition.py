# Program that will take a string as an argument and return the longest consecutive single character found and how many times it was found.
# i.e. string "aaaabbaafff" would return ('a', 4)

def longest_repetition(chars):

    if chars == '':
        return print(str('', 0))

    char_count = {}

    # set(chars) will eval to 1 of each possible char, then iterate for each character
    for i in set(chars):
	    j = 1
	
	    # for every iteration, check if i + i is in the string {char}. Once i + i is not in string {char}, assign character i as i - 1,
        # which is the highest consecutive amount of characters found in string {char}, to char_count key=i value=j-1
	    while i * j in chars:
		    j += 1
	
	    char_count[i] = j - 1
    
    # Using sorted function, sort dictionary items in char_count from highest to lowest, then return highest being answer[0]
    answer = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    
    return print(answer[0])

    # Check if chars is blank, return ()'', 0)
    #    if chars == '':
       # return ('', 0)
    
    # Iterate through string
    #    char_count = {}
    
    #    for i in chars:
    #        char_count[i] = 1 + char_count.setdefault(i, 0)
        
def longest_repetition2(chars):
    # define a current max_count, max_char variable pair
    # define a count, char, pair

    max_count, max_char = 0, ''
    count, char = 0, ''

    # iterate through each letter of chars, for every new char, if the 
    # same char, count + 1 and move to next char, if not same char,
    # check if count is higher than max_count saved(first iteration where max_count
    # is 0, count will always be higher and will auto assign first iterated char and count), if yes store assign 
    # max_count to new count and max_char to new char, if not, continue to next char iteration, return max_char and max_count

    for i in chars:
        # If i (i.e. 'a') != char (i.e. 'b'), reassign char to i and count back to 0
        if i != char:
            char = i
            count = 0
        
        # If i (i.e. 'a') == char (i.e. 'a'), increase count by 1
        count += 1
        
        # If at any time count > max_count, assign max_count = count and max_char to char
        if count > max_count:
            max_count, max_char = count, char

    return print(f"{max_char}, {str(max_count)}")

# Test program
tests = [
    ["aaaabb", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
]
for i in range(len(tests)):
    longest_repetition2(tests[i][0])
    print("Answer should be " + str(tests[i][1]))