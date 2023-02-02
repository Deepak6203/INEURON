# 10. Write a Python script to create a list, where each element of the list 
# is a digit of a given number.



given_list = [56, 72, 875, 9, 173, 14, 546, 537, 923, 123]
#original list
print("\nThe original list is : " , given_list)
given_ele = 7
# extracting all elements with Given digit 7 using
# in operator after string conversion using str()
res = [ele for ele in given_list if str(given_ele) in str(ele)]
# result
print("Elements with Given digit  : " + str(res))
