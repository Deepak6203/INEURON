# 6. Write a python script to print first N prime numbers

numr=int(input("Enter range:"))

print("Prime Numbers:",end=' ')
for n in range(1,numr):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end=' ')