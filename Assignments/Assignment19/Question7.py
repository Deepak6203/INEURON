# 7. Write a python program to sum all the numbers in a list.


""" sum all the numbers in a list """
def add(*params):
    sum = 0
    for num in params:
        sum += num
    print(sum)
    
#input as list
my_list = [10,20,30,40,50,60,70,80,90]
add(*my_list)#function call