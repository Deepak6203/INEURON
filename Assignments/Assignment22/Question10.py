# 10. Write a recursive python function to find the Nth term of the Fibonacci series.?


def nThFibonacci(n):
   if n <= 2:
      return n - 1
   else:
      return nThFibonacci(n - 1) + nThFibonacci(n - 2)

print(nThFibonacci(8))