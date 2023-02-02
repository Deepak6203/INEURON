# 8. Write a recursive python function to print binary of a given decimal number.?


def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')
 
dec = int(input("Enter an integer: "))
binary(dec)