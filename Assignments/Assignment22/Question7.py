# 7. Write a recursive python function to calculate sum of the digits of a given number?


def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(3423))
