# 5. Write a Python script to find the smallest number in a given list of numbers.


""" Method 1 """
# list1 = [10, 34, 45, 64, 87, 20, 4, 45, 99]
# print("Min No is : ", min(list1))


""" Method 2 """
list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
	ele = int(input("Enter elements: "))
	list1.append(ele)
print("Min Number is : ", min(list1))