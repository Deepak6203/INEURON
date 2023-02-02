# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}


thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Initial Set : ", thisset)
x = thisset.pop()# pop method remove last item
print("Pop Items", x)
print("Final Set : ", thisset)