def reverse(input_String):
 
	stringLength = int(len(input_String))
 
	reverse_strin = ""
 
	for i in range(0,stringLength):
		reverse_strin = reverse_strin+input_String[-i-1]
	
print (str(reverse_strin))
 
print ("Enter the string to reverse")
 
reverse_strin = input()

reverse(reverse_strin)