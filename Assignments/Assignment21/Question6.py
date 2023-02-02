# 6. Write a recursive python function to print first N even natural numbers in reverse
# order

def reverseeven(n):
    if n>0:
        print(2*n,end=" ")
        reverseeven(n-1)
reverseeven(7)