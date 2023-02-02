# 6. Write a python program to divide the tuple into four variables.
# tuple1=(100, 200, 300, 400)


tuple1=(100, 200, 300, 400)

print(tuple1)
n1, n2, n3, n4 = tuple1
#unpack a tuple in variables
print("SUM : ",n1 + n2 + n3 + n4) 
# #the number of variables must be equal to the number of items of the tuple
# n1, n2, n3, n4 ,n5 = tuple1 #Output Error
