# 9. Write a Python script to print indices of all occurrences of a given element in a given
# list.


list1 = [eval (x) for x in input("Enter List Elements : ").split(',')]

element = eval(input("Enter Element Value : "))
index = 0
while index < len(list1):
    if list1[index] == element:
        print(index, end=" ")
    index += 1
    

#                      [0]     [4][5]   [8]
# Enter List Elements : 1,2,3,4,1,1,4,22,1
# Enter Element Value : 1
# 0 4 5 8 