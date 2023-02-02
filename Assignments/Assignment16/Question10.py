# 10. Write a python program to change the first item (22) of a list within the following 
# tuple to 222. tuple1 = (11, [22, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)
print("Old Tuple :", tuple1)
tuple1[1][1] = 222
print("New Tuple :", tuple1)
