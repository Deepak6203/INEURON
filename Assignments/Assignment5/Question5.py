# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.


number = int(input("Enter A Number :"))

# use case number = 234 , Output 2
#Operation number%10
number = int(number/100)
print("New Value Of a number : ")
print(number)