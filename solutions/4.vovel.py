import re																#regular expressions operations

input_str = raw_input("Please enter a single alphabet only: ")			#taking input from user
if not re.match("^[a-z]*$", input_str):									#checking input for only alphabet
    print "Error! Only letters a-z allowed!, no numbers ad special characters"
    sys.exit()
elif len(input_str) > 1:												#limiting input to single alphabet
    print "Error! Only 1 character allowed!"
    sys.exit()

if input_str in ('a', 'e', 'i', 'o', 'u'):								#Checking if input is vowel or constant
        print "The given alphabet is vowel"
		
else:
        print "The given alphabet is consonant"