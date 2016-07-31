ip = raw_input("Enter a string: ")				#taking input from the user

def len_str(s):    								#function defined
    if s == '': 
	return 0									#comparing if the input given by user is empty
	
    return 1 + len_str(s[1:])					#if input is non zero, increment up-to length of sting along with spaces and return value
	
print'The lenth of the string is: ',len_str(ip)	#printing output
