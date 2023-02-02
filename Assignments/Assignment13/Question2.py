# 2. Write a python script to get the data type of a list


"""First Method """
# list1=[1,2,3,4,5,6]
# list2 = ["Ankit","Amit","Aman"]
# list3 = ['11', '22', 'deepak', 'raj', 'singh']

# print("List 1 : ", type(list3))
# print("List 2 : ", type(list1))
# print("List 3 : ", type(list2))


"""Second Method """
list1 = [1,'f', 1.1, 1.01]
print([type(i) for i in list1])

# for i in list1:
#     print(type(i))