# 5. Write a python script to print first N odd natural numbers in reverse order


n = int(input("Enter A Number "))
i = 1

while i <= n:
    print(2*n-2*i+1,end=' ')
    # print(i)
    i += 1





# for i in range(1,n+1):
#     print(2*n-2*i+1,end=' ')