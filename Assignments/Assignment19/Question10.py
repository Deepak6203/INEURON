# 10. Write a python program to create a function to check whether 
# a given number is even or odd.


def evenOdd(num):
    if num%2 == 0:
        return(" Even No.. ")
    return(" Odd No.. ")
    
num = int(input("Enter A No Check Even/Odd : "))
print(evenOdd(num))