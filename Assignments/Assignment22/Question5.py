# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers?


def sumNCubes(n):
    return sum(i**3 for i in range(1,n+1))

def main():
    number = int(input("What number do you want to find the sum of cubes for : "))
    print ("The result of the sums is : ", sumNCubes(number))

main()
sumNCubes(5)