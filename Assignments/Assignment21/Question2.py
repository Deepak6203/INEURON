# 2. Write a recursive python function to print first N natural numbers in reverse order

def reNumber(N):
	if (N <= 0):
		return
	else:
		print(N, end = " ")
		reNumber(N - 1)
		

N = 5
reNumber(N)