# 9. Write a python program to create a function to check whether a number falls in a
# given range


def test_range(n):
    if n in range(10,50):
        print( " %s in the range : "%str(n))
    else :
        print(" %s Out Of Range : "%str(n))
n=int(input("Enter A Numbrs B/w 10 To 50 : "))
test_range(n)