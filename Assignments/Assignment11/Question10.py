# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

def dectoOct(decimal):
    if(decimal > 0):
        dectoOct((int)(decimal/8))
        print(decimal%8, end='')
        
decimal = int(input("Enter a decimal number: "))
print("Octal Number : ", end='')
dectoOct(decimal)