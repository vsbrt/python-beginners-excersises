def is_member(valueToCheck, listToBeChecked):
 
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
 
&nbsp;