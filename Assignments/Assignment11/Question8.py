# 8. Write a python script to calculate sum of digits of a given number
 

num = int(input("Enter Number: "))
sum = 0

for i in str(num):
    sum = sum + int(i)

print("Sum Of Digit : ",sum) 


# while num!=0:
# 	digit = int(num%10)
# 	sum += digit
# 	num = num/10