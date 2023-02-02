# 9. Write a recursive python function to print first N multiples of a given number.


def nMulti(n):
  if n > 0:
    nMulti(n - 1)
    print(n*n, end = ' ')

n = int(input("Enter A No.. : "))
nMulti(n)
