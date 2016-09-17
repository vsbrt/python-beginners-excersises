'''numbers = input("Please enter a number: ")'''

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

if _name_ == "_main_":	
	print sum([1, 2, 3, 4])
	print multiply([1, 2, 3, 4])

'''print sum(numbers)	
print multiply(numbers)'''