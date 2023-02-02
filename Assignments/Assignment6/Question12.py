# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part

x = complex(input("Enter A Complex No "))
print(x.real) if x.real > x.imag else print(x.imag)

# PS D:\IneuronWeb\Assignment6> python Question12.py
# Enter A Complex No 3+4j
# 4.0