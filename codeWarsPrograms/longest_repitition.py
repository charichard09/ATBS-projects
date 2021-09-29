# Program that will take a string as an argument and return the longest consecutive single character found and how many times it was found.
# i.e. string "aaaabbaafff" would return ('a', 4)

def longest_repetition(chars):

    if chars == '':
        return ('', 0)

    char_count = {}

    for i in set(chars):
	    j = 1
	
	    # Check highest consecutive times char i shows up by increasing i by i each time
	    while i * j in chars:
		    j += 1
	
	    char_count[i] = j - 1
    
    answer = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    
    return answer[0]

    # Check if chars is blank, return ()'', 0)
    #    if chars == '':
       # return ('', 0)
    
    # Iterate through string
    #    char_count = {}
    
    #    for i in chars:
    #        char_count[i] = 1 + char_count.setdefault(i, 0)

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
longest_repetition(tests)
        
        
#    answer = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    
#    return answer[0]