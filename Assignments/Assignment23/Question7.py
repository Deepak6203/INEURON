# 7. Create an endless iterator using generator method to produce terms of Fibonacci series?



def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
a = int(input('Give Number : '))
print(list(fib(a)))