# 4. Write a recursive python function to calculate sum of squares of first N natural numbers


def rsum(n):
    if n <= 1:
        return n
    else:
        return n + rsum(n-1)

num = int(input("Enter a number: "))
total=rsum(num)
print("The sum is",total)

