# 2. Write a python script to check whether a given number is Prime or not

prime = int(input("Enter A Number : "))

if prime > 1:
	for i in range(2, int(prime/2)+1):
		# If num is divisible by any number between 2 and n / 2, it is not prime
		if (prime % i) == 0:
			print(prime, "Is Not A Prime Number")
			break
	else:
		print(prime, "Is A Prime Number")
else:
	print(prime, "Is Not A Prime Number")
