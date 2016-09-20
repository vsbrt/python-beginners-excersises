def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)
 
input_string = raw_input("Enter the string to be reversed: ")
print(reverse(input_string))