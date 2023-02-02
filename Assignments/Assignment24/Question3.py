# 3. Write a python program to create 2 objects of the user class and assign different
# values.


class User:
    def greet(self, name = ""):
        self.name = name
        print("Good Morning {}".format(self.name))
obj1 = User()
obj2 = User()
print("OBject 1 : ")
obj1.greet("Deepak")
print("OBject 2 : ")
obj2.greet("Sudhir")