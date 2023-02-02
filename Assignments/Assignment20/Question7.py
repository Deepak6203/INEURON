# 7. Write a python program to access a function inside a function.


def OutFun(): # outer function  
    print("It Is Outer Function")  
      
    def InFun(): # inner function  
        print("It Is inner Function")  
    InFun() # call inner   
  
OutFun() # call outer function 

