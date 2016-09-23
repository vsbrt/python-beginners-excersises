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


if __name__ == "__main__":
	input_string = input("enter numbers separated by comas:")
	print(sum(input_string))
	print(multiply(input_string))