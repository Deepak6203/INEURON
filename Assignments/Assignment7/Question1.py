# 1. Write a python script to display the number of days in a given month number.




# month = int(input("Enter Month No "))
# if month in (1,3,5,7,8,10,12):
#     print("31 Days ")
# elif month in (4,6,9,11):
#     print("30 Days ")
# elif month == 2:
#     print("28 Or 29 Days ")
# else:
#     print("Invalid Month No ")


month = int(input("Enter Month Number :"))

match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 Days")
    case month if month in (4,6,9,11):
        print("30 Days")
    case 2:
        print("28 Or 29 Days")
    case _:
        print("Invalid Month Number ")
print()