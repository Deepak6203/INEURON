# 5. Write a python script to print table of user’s choice


n = int(input("Enter A Number "))

for i in range(1,11,1):
    print("{} * {} = {}".format(i, n, i*n))