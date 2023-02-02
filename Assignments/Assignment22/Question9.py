# 9. Write a recursive python function to print octal of a given decimal number?


def decimaltoOctal(deciNum):
	octalNum = 0
	countval = 1
	dNo = deciNum
	while (deciNum != 0):
		# decimals remainder is calculated
		remainder = deciNum % 8
		# storing the octalvalue
		octalNum += remainder * countval
		# storing exponential value
		countval = countval * 10
		deciNum //= 8
	print(octalNum)


if __name__ == '__main__':
	n = int(input("Enter No To Convert Decimal To Octal : "))
	decimaltoOctal(n)