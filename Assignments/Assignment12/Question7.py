# Write a python script to check whether a given pair of numbers are co-Prime
# numbers or not.
# EX {a = 5 , b = 6 --> Co-Prime} {a = 8 , b = 16 --> Not Co-Prime}  



def Gcd(a, b):
	if (a == 0 or b == 0): return 0
	# base case
	if (a == b): return a
	# a is greater
	if (a > b):
		return Gcd(a - b, b)
	return Gcd(a, b - a)

def coPrime(a, b):	
	if ( Gcd(a, b) == 1):
		print("Co-Prime")
	else:
		print("Not Co-Prime")	

a = int(input("Enter First No  : "))
b = int(input("Enter Second No : "))
coPrime(a, b)