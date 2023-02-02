# 6. Write a python program to append elements from another list to the current list.
# ( firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )


firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]



""" Method 1: Using the append() """
firstlist.append(secondlist)
print ("Final List : \n", firstlist)



""" Method 2: Using Concatenation(+) Operator """
# final_list = firstlist + secondlist
# print(final_list)

""" Method 3: Using extend() Method """
# firstlist.extend(secondlist)
# print ("Final List : \n", firstlist)


""" Method 4: Using itertools.chain() Method """
# import itertools
# # Adding the second list using itertools.chain() function
# firstlist = list(itertools.chain(firstlist, secondlist))
# print ("Final list : ", firstlist)