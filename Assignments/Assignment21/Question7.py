# 7. Write a recursive python function to print squares of first N natural numbers

def nsqure(n):
  if n > 0:
    nsqure(n - 1)
    print(n*n, end = ' ')

n = int(input("Enter A No.. : "))
nsqure(n)
