def reverse(inputString):
 
	stringLength = int(len(inputString))
 
	reversedString = ""
 
	for i in range(0,stringLength):
		reversedString = reversedString+inputString[-i-1]
	
	print (str(reversedString))
 
print ("Enter the string to reverse")
 
reverse_strin = input()

reverse(reverse_strin)