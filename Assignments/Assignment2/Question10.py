# Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)

from datetime import datetime
dt = datetime.today()
# print(dt)

d1 = dt.strftime("%d-%m-%Y and %I:%m:%p")
print(d1)


# PS D:\IneuronWeb\Assignment2> python Question10.py
# 17-08-2022 and 11:10:PM