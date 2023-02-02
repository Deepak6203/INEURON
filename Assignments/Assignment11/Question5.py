# 5. Write a python script to calculate sum of first N even natural numbers

print("Calculate Sum Of First N Even Natural Number :\n")
Num = int(input("Enter A Number : "))
sum=0
for i in range(1,Num+1):
    if i%2 == 0:
        sum += i
print("Even Sum Are : ",sum)