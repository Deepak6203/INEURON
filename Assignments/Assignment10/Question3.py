#3. Write a python script to print first M multiples of N.



m = int(input("Enter A Number (M) "))
n = int(input("Enter A Multiples Of (N) "))

for i in range(1,m+1,1):
    print(i*n)

