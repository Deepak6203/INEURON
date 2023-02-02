# 1. Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)

number = int(input("Enter A Number :"))

# use case number = 2345 , Output 234
#Operation number/10

number = int(number / 10)
print(number)