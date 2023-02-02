# 6. Write a python program to create 3 user objects and find the youngest of all


class User:
    def youngestUser(self, age1, age2, age3):
        self.age1 = age1
        self.age2 = age2
        self.age3 = age3
        if( self.age1 < self.age2 and self.age1 < self.age3):
            print("The Youngest Age is Amit")
        elif( self.age2 < self.age1 and self.age2 < self.age3):
            print("The Youngest Age is Ram")
        else:
            print("The Youngest Age is Vijay")


age1 = int(input("Give the Age of 1 Person :"))
age2 = int(input("Give the Age of 2 Person :"))
age3 = int(input("Give the Age of 3 Person :"))

obj = User()
obj.youngestUser(age1, age2, age3)