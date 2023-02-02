# 2. Create a generator to produce first n odd natural numbers?


def odd_generator(n):
    value = 1
    while value < n:

        yield value
        value += 2

N = int(input("Enter A Number "))
for value in odd_generator(N):
    print(value)