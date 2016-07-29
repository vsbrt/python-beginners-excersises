a = input("Enter the first number to be compared: ")
b = input("Enter the second number to be compared: ")
c = input("Enter the third number to be compared: ")

def max_three(a,b,c):

	if (a>b) and (a>c):
		print'The max numer is: ',a
	
	elif (b>a) and (b>c):
		print'The max number is: ',b
	
	elif (c>a) and (c>b):
		print'The max number is: ',c
		
max_three(a,b,c)