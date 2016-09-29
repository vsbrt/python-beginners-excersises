'''def is_member(valueToCheck, listToBeChecked):
 
	for i in range(len(listToBeChecked)):
 
 if valueToCheck == listToBeChecked[i]:
  return True
 else:
  return False

	List = ['aa','bb','cc','dd','ee','ffgg','hhii','jjkkll']
 
	#print("The list is: " +str(List))

	itemToCheck = input("Enter the item to check in the printed list")
 
if is_member(itemToCheck,List) == True:
 print ("The item is present in the list")
else:
 print ("The item is not present in the list")
 
&nbsp;'''


def is_member(x, a):

	a = ['aa','bb','cc','dd','ee','ffgg','hhii','jjkkll']
	print("Predefined list: " +str(list))
	
    if len(a) == 0:
        return False
    return x == a[0] or is_member(x, a[1:])


if __name__ == "__main__":
    print is_member(1, [1, 2])
    print is_member('a', ['a'])
    print is_member('b', [1, 2, 'a'])