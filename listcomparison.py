L1 = ['a','b','c']
L2 = ['b','d']
common_elements = []
#common_elements is a list where elemnts are in both L1&L2
L3=[]
#L3 is a list which represents the elements presnt in L1 and not in L2"

# using for loop to compare the elements in lists
for i in L1:
	a=i
	# using the if loop to check the elements in L1 is L2 or not
	if a in L2:
	   # appending the value to a list
	   common_elements.append(a)
	else:
	   L3.append(a)

print(common_elements)
print(L3)
