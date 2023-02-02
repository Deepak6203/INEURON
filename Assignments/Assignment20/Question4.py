# 4. Write a python program to create a function that checks whether a passed string is palindrome or not


def palindrome(n):
    return(str(n) == str(n)[::-1])


strings = str(input("Enter String Check Palindrome Or/Not : "))
print(palindrome(strings))



