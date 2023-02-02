# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Enter Choice")

choice = int(input())

match choice:
    case 1:
        print("Enter Two No")
        a,b = int(input()),int(input())
        print("Sum (+)",a+b)

    case 2:
        print("Enter Two No")
        a,b = int(input()),int(input())
        print("Sub (-) ",a-b)
    case 3:
        print("Enter Two No")
        a,b = int(input()),int(input())
        print("Mul (*) ",a*b)

    case 4:
        print("Enter Two No")
        a,b = int(input()),int(input())
        print("Div (/) ",a/b)

    case _:
        print("Invalid Input ")