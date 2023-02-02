# 2. Write a python program to create a user class with a method to greet the user.


""" Method 1 Using Constructor """
# class User:

#     # constructor function    
#     def __init__(self, name = ""):
#         self.name = name
#         print("Good Morning {}".format(self.name))
# name = input("Enter You'r Name : ")
# obj = User(name)


""" Method 2 Using Greet Func..  """
class User:
    def greet(self, name = ""):
        self.name = name
        print("Good Morning {}".format(self.name))
name = str(input("Enter You'r Name : "))
obj = User()
obj.greet(name)

