# 7. Write a Python script to remove all non int values from a list.

mylist = ["Ram", "Aman", 2, 5, "Deepak", 9, "Amit", "Suman", "Sunil"]
print("Old List : ",mylist)
no_integers = [x for x in mylist if not isinstance(x, int)]
print("\nNew List : ", no_integers)
