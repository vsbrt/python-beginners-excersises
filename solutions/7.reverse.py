def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)
 
'''string = input("Enter the string to reverse ")

reverse(string)'''


print reverse("I am testing")