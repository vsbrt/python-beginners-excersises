def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
	input_string = raw_input("Enter a string to check whether its a palindrome: ")
	print(is_palindrome(input_string))