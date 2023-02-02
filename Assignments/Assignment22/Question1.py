# 1. Write a recursive python function to calculate sum of first N natural numbers?


def sum_first(n):
    if n > 0:
        sum = n + sum_first(n-1)
        return sum
    else:
        return 0

n=int(input("Enter A Number : "))
print(sum_first(n))
