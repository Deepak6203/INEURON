# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.


n = int(input())
match n:
    case n if n%2 == 0:
        pass
    case n if n<0 and n%2:
        pass
    case n if n>0 and n%2:
        pass
