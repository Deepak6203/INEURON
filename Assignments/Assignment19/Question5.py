# 5. Write a python program to create a function which expects a list as an argument.


""" Method 1 Using String """
def myFun(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
myFun(fruits)

""" Method 2 Using No.. """
# def add(*params):
#     sum = 0
#     for num in params:
#         sum += num
#     print(sum)
    
# #input as list
# my_list = [1,2,3,4,5,6,7,8,9]
# add(*my_list)#function call