# 5. Write a python script to add an item to the end of the list
#  (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"])


#Given List
mylist = ["Java", "SQL", "C", "Reactnative"]
print("Old List : ", mylist)
def addItem(mylist=mylist):
    item = str(input("Add Item : "))
    mylist.append(item)# Set the last element

addItem()
print("New List : ", mylist)





# mylist = [1, 2, 3]
# mylist[-1] = 5 # Set the last element
# mylist[-2] = 3 # Set the second to last element
# mylist
# [1, 3, 5]