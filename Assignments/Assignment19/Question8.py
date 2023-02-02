# 8. Write a python program to multiply all the numbers in a list.


""" multiply all the numbers in a list """
def add(*params):
    sum = 1
    for num in params:
        sum *= num
    print(sum)
    
#input as list
my_list = [1,2,3,4]
add(*my_list)#function call