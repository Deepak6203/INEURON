# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.



number = int(input("Enter A Number :"))

# use case number = 234 , Output 3
#Operation number%10
number = int(number/10)
answer = (number%10)
print("Answer :",answer)