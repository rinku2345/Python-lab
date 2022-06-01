# Python program to find the
# maximum of two numbers


def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = 2
b = 4
print(maximum(a, b))

#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])