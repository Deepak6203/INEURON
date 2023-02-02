# 5. Create a generator to produce first n terms of Fibonacci series?


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a = int(input('Give Any Number : '))
print(list(fib(a)))
