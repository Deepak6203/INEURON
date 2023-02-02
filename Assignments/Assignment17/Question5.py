# 5. Write a python program to add items from another set to the current set. 
# thisset = {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}



thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print("First Set : ", thisset)
print("Second Set : ", secondset)

thisset.update(secondset)
print("Updated Sat : ", thisset)