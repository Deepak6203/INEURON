# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement


str1 = input("Enter First String ")
str2 = input("Enter Second String ")

match (str1,str2):
    case (str1,str2) if str1 == str2:
        print("Identical String")
    case (str1,str2) if str1 > str2:
        print("{} Comes After {}".format(str1,str2))    
    case (str1,str2) if str1 < str2:
        print("{} Comes After {}".format(str2,str1))

print()