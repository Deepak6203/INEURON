# 3. Write a python program to create a function that prints the even numbers
#  from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" Method 1 """
def p_Even(lst):
    even_lst = []
    for itm in lst:
        if itm % 2 == 0:
            even_lst.append(itm)
    return(even_lst)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(p_Even(list1))


""" Method 2 """
# def p_even(lst):
#     return [x for x in lst if x % 2 == 0]

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(p_even(list1))


