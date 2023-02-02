# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.


print("Enter Age ")
Age = int(input())

match Age:
    case Age if Age < 10:
        print("Kid")

    case Age if Age < 20:
        print("Teen")

    case Age if Age < 40:
        print("Young")

    case Age if Age < 60:
        print("Experienced")

    case Age if Age >= 60 and Age <= 100:
        print("Senior Citizen")
    case _:
        print("Invalied Input ")
