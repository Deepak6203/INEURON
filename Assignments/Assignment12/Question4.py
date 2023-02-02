# 4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)

min = int(input(" Enter the Min No : "))
max = int(input(" Enter the Max No : "))

for Num in range (min, max + 1):
    count = 0
    for i in range(2, (Num//2 + 1)):
        if(Num % i == 0):
            count = count + 1
            break

    if (count == 0 and Num != 1):
        print(" %d" %Num, end = '  ')