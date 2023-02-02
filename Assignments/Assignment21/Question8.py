# 8. Write a recursive python function to print cubes of first N natural numbers


def nCubes(n):
  if n > 0:
    nCubes(n - 1)
    print(n*n*n, end = ' ')

n = int(input("Enter A No.. : "))
nCubes(n)