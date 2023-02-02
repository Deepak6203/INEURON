# 1. Write a python script to store multiple items in a single variable 
# ( Items are “Java” ,“Python”,  “SQL”,  “C” ) using tuple

# #Empty List
# list1 = ()
# tuples = list(list1)
# tuples.insert(0, "Java")
# tuples.insert(1, "“Python”")
# tuples.insert(2, "SQL")
# tuples.insert(3, "C")
# tuplst = tuple(tuples)
# print("Type Of Items :",type(tuplst))
# print(tuple(tuples))


list1 = []
items = int(input(" How Many Items Store : \n"))
for item in range(items):
    itm = str(input("Enter Item : "))
    list1.append(itm)

print("Type Items :", type(list1))
print(list1)
print("Type Items :", type(tuple(list1)))
print(tuple(list1))