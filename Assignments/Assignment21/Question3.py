# 3. Write a recursive python function to print first N odd natural numbers


def odd(N, count=1):
    if(count <= N):
        print(2*count-1)
        odd(N,count+1)

odd(9)
