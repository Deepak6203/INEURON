# 2. Write a recursive python function to calculate sum of first N odd natural numbers?


def sum_of_odd(n):
    if n>0:
        x=(n*2)-1
        return x+sum_of_odd(n-1)
    else:
        return 0

n=int(input("Enter A Number : "))
print(sum_of_odd(n))