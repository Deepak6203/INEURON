# 4. Create a generator to produce squares of first N natural numbers


def nNO_generator(n):
    value = 1
    while value < n:

        yield value
        value += 1

N = int(input("Enter A Number "))
for value in nNO_generator(N+1):
    print(value)