# 4. Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.


print("Enter Two Number :")
num1,num2=int(input()),int(input())
print(num1 if num1 > num2 else num2)