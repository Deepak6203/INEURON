# 2. Write a python program to access the items of a dictionary by referring to its key
# name.


info = {
"Name": "Deepak",
"Gender": "Male",
"Year": 2002,
}


""" Way 1 """
x = info.get("Name")
print(x)#Deepak

""" Way 2 """
x = info["Gender"]
print(x)#Male
