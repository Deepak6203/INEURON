# 2. Write a python script to calculate sum of squares of first N natural numbers

print("Calculate Sum Of Squares Of N Natural Number :\n")
Num = int(input("Enter A Number"))
sum=0
for i in range(1,Num+1):
    sum += i*i
print("Squares Are :",sum)