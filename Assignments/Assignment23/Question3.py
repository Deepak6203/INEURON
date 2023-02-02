# 3. Create a generator to produce first n even natural numbers

def even_generator(n):
    value = 2
    while value < n:

        yield value
        value += 2


N = int(input("Enter A Number : "))
for value in even_generator(N+1):
    print(value)