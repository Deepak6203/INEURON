# 8. Write a python script to check if a string contains only numbers.


string1 = '12345567890'
string2 = 'abcdefghijklmnop'
print("Initial Strings : ", string1, string2)

#For String 1 Check
if string1.isdigit():
	print("String1 Only Numbers")
else:
	print("String1 doesn't contains Only numbers")

#For String 2 Check
if string2.isdigit():
	print("String2 Only numbers")
else:
	print("String2 doesn't contains Only numbers")
