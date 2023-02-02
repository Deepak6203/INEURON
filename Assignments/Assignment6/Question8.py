# 8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

print("Enter Value a,b and c of a quadratic equation")
a,b,c = int(input()),int(input()),int(input())

d=b**2-4*a*c
if d>0:
    print("Real and distinct roots ")
elif d==0:
    print("Real and Equal Roots")
else:
    print("Imaginary roots ")