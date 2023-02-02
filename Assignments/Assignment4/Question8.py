# Write a python script to calculate simple interest



# A	=	final amount
# P	=	initial principal balance
# r	=	annual interest rate
# t	=	time (in years)
# S.I. = P × R × T   r/100.

print("Enter Three No to Caluculate Avg : ")
p = int(input("Enter Initial Principal Balance : "))
r = int(input("Enter Annual Interest Rate : "))
t = int(input("Enter Time (In Years) : "))

SI = (p*r*t)/100

print("Simple Intrest Rate : ",SI)