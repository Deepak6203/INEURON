# 2. Write a python program to create a function that takes a number
#  as a parameter and checks if the number is prime or not


def isprime(n):

    if n < 2: return False

    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

n = int(input("Enter A Number Check Prime Or/Not : "))
print(isprime(n))


