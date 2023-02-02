# 6. Write a python program to create a  function and print a list
#  where the values are square of numbers between 1 and 30


def printValues():
	l = list()
	for i in range(1,30):
		l.append(i**2)
	print(l)

printValues()
