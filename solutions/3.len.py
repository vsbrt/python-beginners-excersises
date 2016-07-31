ip = raw_input("Enter a string: ")

def string_length(s):    
    if s == '': return 0
    return 1 + string_length(s[1:])
	
print'The lenth of the string is: ',string_length(ip)

'''def len_str(a):
	i=0
	
	for letter in a:
		i+=1
		return i

print'The lenth of the string is: ',len_str(ip)'''