#This program adds two numbers and prints the binary representation of that number

def add_binary(a, b):
    binary = []
    sum = (a + b)
    while sum >= 1:
        binary.insert(0, str(sum % 2))
        sum = int(sum / 2)
	    
    return "".join(binary)

print(add_binary(4, 5))