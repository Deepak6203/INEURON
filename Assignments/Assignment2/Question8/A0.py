# Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
# value to it. Write a python script to import A1 module in A0 and print value of the
# variable created in A0.py

# import A1
# print("This File Is A0 : ",A1.var)


from A1 import var
print("This File Is A0 : ",var)


# PS D:\IneuronWeb\Assignment2> & C:/Users/deepa/AppData/Local/Programs/Python/Python310/python.exe d:/IneuronWeb/Assignment2/Question8/A0.py
# This File Is A0 :  I M A1 File