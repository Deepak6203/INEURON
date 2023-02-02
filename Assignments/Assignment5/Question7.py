# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.

number = int(input("Enter A Number :"))

# use case number = 234 , Output 4
#Operation number%10

number = (number%10)
print("New Value Of a number : ")
print(number)