# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value




list1_keys = ["Amit", "Ankit", "Suman", "Abhi", "Sunil"]
list2_values = [1, 2, 3, 4, 5]

# Original keys-value lists
print("Original key OF list   : " + str(list1_keys))
print("Original value Of list : " + str(list2_values))

# convert lists to dictionary
res = {}
for key in list1_keys:
	for value in list2_values:
		res[key] = value
		list2_values.remove(value)
		break

# Printing resultant dictionary
print("Result Of dictionary is : " + str(res))
