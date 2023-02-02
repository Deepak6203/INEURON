# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]


thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print("\nFirst Set : ", thisset)
print("Second Set : ", mylist)

thisset.update(mylist)
print(thisset)