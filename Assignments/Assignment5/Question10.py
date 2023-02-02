# 10. Write a python script to use IS operator to display if both variables are the same
# object or not

list_1 = [0,1,3,4,5,2]
list_2 = [0,1,3,4,5,2]

print(list_1 is list_2)
print(list_1 == list_2)

#Output
# False ye memory ka location check karta hai
# True ye value check karta hai