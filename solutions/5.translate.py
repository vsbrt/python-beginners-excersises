'''
def double_mult(s):
	vowels = 'aeiou'
    return ''.join(l for l if l in vowels else l + 'o' + lin input_str)        

def translate(input_str):
	input_str = raw_input("Please enter word to be Translated: ")
	double_mult(input_str)
	
'''

def translate(s):
	vowels = 'aeiou'
	return ''.join(l + 'o' + l if l not in vowels else l for l in s)
  #consonants = 'bcdfghjklmnpqrstvwxz'
  #return ''.join(l + 'o' + l if l in consonants else l for l in s)

input_str = raw_input("Please enter a word to be translated: ")
print(translate(input_str))