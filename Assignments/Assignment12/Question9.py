# 9. Write a python script to calculate LCM of two numbers

print(" Check LCM")
num1 = int(input("Enter 1 No : "))
num2 = int(input("Enter 2 No : "))
max  = max(num1, num2)
for i in range(max, 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        LCM = i
        break
print("Lcm Of", num1, "And", num2, "Is : ", LCM)