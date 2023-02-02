# 5. Write a python program to check if all items in the tuple are the same.


x = (True, True, True)
result = all(x)
print(result)


x2 = (True, True, False)
result = all(x2)
print(result)


## output
# True
# False