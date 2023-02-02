# 6. Write a python program to check whether a given string is a multiword string or single
# word string using match case statement


s = input("Enter A String")
s.strip()#ye age or pichhe ke space remove kar deta hai 
match s:
    case s if ' ' in s:
        print("Multiword String")
    case s if ' ' not in s:
        print("Single word String\n")


