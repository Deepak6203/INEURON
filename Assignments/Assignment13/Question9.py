# 9. Write a Python script to create a list of city names taken from the user

citylist = []
cityes = int(input("Enter Number Of The City : "))
for city in range(cityes):
   print("Enter City Name : {}".format(city+1),end=" ")
   cityelm = input()
   citylist.append(cityelm) # adding the element
print("\nThe entered list is: \n",citylist)