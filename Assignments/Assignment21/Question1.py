# 1. Write a recursive python function to print first N natural numbers?



def printNumber(n):
  if n > 0:
    printNumber(n - 1)
    print(n, end = ' ')

n = int(input("Enter A No.. : "))
printNumber(n)
