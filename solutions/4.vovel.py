import re															#regual expressions operations

input_str = raw_input("Please enter a single alphabet only: ")		#taking input from user
if not re.match("^[a-z]*$", input_str):								#checking input for only alphabet
    print "Error! Only letters a-z allowed!"
    sys.exit()
elif len(input_str) > 1:											#limiting input to single alphabet
    print "Error! Only 1 character allowed!"
    sys.exit()

