# 8. Write a python program to sort the list alphanumerically – 
# thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
print("This List :", thislist)

def sortList(lst=thislist):
	lst.sort()#lst.sort(key = str)
	return lst
print("Sorted List : ",sortList())




