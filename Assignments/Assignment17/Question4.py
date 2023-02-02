# 4. Write a Python script to find if “Python” is present in the set  
# thisset = {"Java", "Python", "Django"}


thisset = {"Java", "Python", "Django"}
def check(thisset=thisset):
    if "Python" in thisset:
        pass
        return(True)
    return(False)
print("Present Or/Not : ",check())