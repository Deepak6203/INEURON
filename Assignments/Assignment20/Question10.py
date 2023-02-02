# 10. Write a python program to create a function to check whether a 
# string is an anagram or not.



def anagrams(s1, s2):
    if(sorted(s1)==sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

s1=input("Enter first string:")#anagram
s2=input("Enter second string:")#nagaram
anagrams(s1, s2)





# Case 1:
# Enter first string:anagram
# Enter second string:nagaram
# The strings are anagrams.
 
# Case 2:
# Enter first string:hello
# Enter second string:world
# The strings aren't anagrams.