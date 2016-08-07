def translate(string):
	vowels = 'aeiou'														#Defined vowels
	return ''.join(l + 'o' + l if l not in vowels else l for l in string)	#comparing string for vowels and consonants and adding an 'o' in between every consonant   

input_str = raw_input("Please enter a word to be translated: ")				#taking input from user
print(translate(input_str))