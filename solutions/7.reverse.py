def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)
 
reverse_strin = input("Enter the string to reverse ")

reverse(reverse_strin)


print reverse("I am testing")