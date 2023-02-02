# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# # use bin() method)


def decToBinary(num):
	
	if num >= 1:
		decToBinary(num // 2)
	print(num % 2, end = '')

num = int(input("Enter A Number : "))
decToBinary(num)#Function call
