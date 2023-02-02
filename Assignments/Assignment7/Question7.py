# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement

n = int(input("Enter Number "))
match n:
    case n if n > 0:
        print("Positive No")
    case n if n < 0:
        print("Negative No")
        
    case n if n == 0:
        print("Zero No")
        