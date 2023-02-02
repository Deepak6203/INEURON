# 5. Write a python script to find next prime number of a given number

def nextPrime(num):
    while True:
        num += 1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return(num)
print("Check Next Prime No : ")
num = int(input())
print(nextPrime(num))