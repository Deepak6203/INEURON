# 3. Write a python script to calculate sum of cubes of first N natural numbers


print("Calculate Sum Of Cube Of N Natural Number :\n")
Num = int(input("Enter A Number"))
sum=0
for i in range(1,Num+1):
    sum += i*i*i
print("Sum Of Cube Are :",sum)