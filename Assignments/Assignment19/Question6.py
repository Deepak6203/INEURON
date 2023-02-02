# 6. Write a python program to create a function that finds a maximum of four numbers


def maxFourNo(*args):
    if(num1 > num2 and num1 > num4) :
        print("User 1's number  is greater")  
    elif(num2 > num3) :
        print("User 2's number  is greater")
    elif(num3 > num4) :
        print("User 3's number  is greater")
    elif(num4 > num2) :
        print("User 4's number  is greater")
    else :
        print("done")


num1 = int(input("Enter number 1: ")) #user 1
num2 = int(input("Enter number 2: ")) #user 2
num3 = int(input("Enter number 3: ")) #user 3
num4 = int(input("Enter number 4: ")) #user 4

allNum = {num1, num2, num3, num4}
print("All numbers: ",allNum)
maxFourNo(allNum)