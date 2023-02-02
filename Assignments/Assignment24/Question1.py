# 1. Write a python program to create a user class with 3 properties : name, age, email?



class User:
    def personal_details(self):
        name, age, email = "Deepak", 21, "deepak@gmail.com"
        address = "Lakhisarai, Bihar, India"
        print("Name: {}\nAge: {}\nEmail: {}\nAddress: {}".format(name, email, age, address))


sammy = User()#Creeate User Obj
sammy.personal_details()