# 7. Write a python script to count digits in a given number

num = int(input("Enter A Number : "))
cout=0
while(0<num):
    num = int(num/10)
    print(num)
    cout += 1
print("Total Digits :",cout)

