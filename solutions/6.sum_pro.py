numbers = input("Please enter a number: ")

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(numbers)

def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
print(numbers)