# 5. Write a recursive python function to print first N even natural numbers


def even(i, N):
    if(i<=N) :
        print(2*i)
        even(i+1, N)
even(1,11)