# 1. Write a python script to store multiple items in a single variable
#  ( Items are “Java”,“Python”,  “SQL”,  “C” ) using list


"""First Method"""
# lists = []
# item = int(input("Enter Numbers How Many Items Store : "))
# for i in range(item):
#     items = eval(input("Enter Items :"))
#     lists.append(items)

# print(lists)


"""second Method"""
lists = []
item = int(input("Enter Numbers How Many Items Store : "))
for i in range(item):
    items = str(input("Enter Items :"))
    lists.append(items)

print("Items are",tuple(lists))


