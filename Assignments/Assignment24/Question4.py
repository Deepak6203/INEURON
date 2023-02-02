# 4. Write a python program to init default values for user object using __init__ method.


class User:

    # constructor function    
    def __init__(self, name = ""):
        self.name = name
        print("Hi {}".format(self.name))
name = input("Enter You'r Name : ")
obj = User(name)