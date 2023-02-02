# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values){Not Cmp}



class Laptop():
    def  __init__( self, brand, ram, cpu, hdd ):
        self.brand = brand
        self.ram   = ram
        self.cpu   = cpu
        self.hdd   = hdd        


    #Sshow Configuration
    def showConfig( self, brand, ram, cpu, hdd ):
        # self.brand = brand
        # self.ram   = ram
        # self.cpu   = cpu
        # self.hdd   = hdd
        print("\nGiven Brand Is : ", self.brand)
        print("\nGiven RAM   Is : ", self.ram)
        print("\nGiven CPU   Is : ", self.cpu)
        print("\nGiven HDD   Is : ", self.hdd)



brand = str(input("Give the Brand Name : "))
ram = str(input("Give the Ram Info     : "))
cpu = str(input("Give the Cpu Info     : "))
hdd = str(input("Give the HDD info     : "))

obj = Laptop()
obj(brand, ram, cpu, hdd).showConfig()