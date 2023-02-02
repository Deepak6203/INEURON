# 6. Write a recursive python function to calculate the factorial of a number.?


def factorial(n):
   if n < 1:
       return 1
   else:
       returnNumber = n * factorial(n - 1)  # recursive call
#      print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

print(factorial(4))
