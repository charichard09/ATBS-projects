# Given two arrays of string values, return a sorted array of all strings in a1 that 
# are substrings of strings in a2

def in_array(array1, array2):

# TODO: for every word iterated through in array1, check it against every word iterated through in array2. if that word is seen, store array1 
# into new array 'r'
    r = []

    for text in array1:
        for word in array2:
            if text in word:
                r.append(text)

# TODO: using the sorted function, sort array 'r'
    r = sorted(set(r))
    
    return r

# Codewars test:
a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

#   r = ['arp', 'live', 'strong']         
#   a1 = ["arp", "mice", "bull"] 
#   a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#   r = ['arp']

print(in_array(a1, a2))