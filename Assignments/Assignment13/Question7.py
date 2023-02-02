# 7. Write a python program to Print all items by referring to their index number
#  (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"] )

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print("Given List ", thislist)

for list in thislist:
	# print(thislist.index(list), " ", list)
	print('Index {0} On Item {1} '.format(thislist.index(list), list))