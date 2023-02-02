# 5. Write a python program to create a function to find the Min of three numbers


def min(num1, num2, num3):    
    smallest = num1
    if num1 < num2 and num1 < num3 :
        smallest = num1
    elif num2 < num3 :
        smallest = num2
    else :
        smallest = num3
    print(smallest, "Is The Smallest Number..")

num1 = int(input('Enter 1 Number  : '))
num2 = int(input('Enter 2 Number  : '))
num3 = int(input('Enter 3 Number  : '))
min(num1, num2, num3)