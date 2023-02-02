# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday


s = input("What Is Your Favourite colour ")
l1 = ["yellow","blue","orange","white","black","red",] 
for colour in l1:
    if colour in s:
        c = colour
        break
else:
    c ="Other"

match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")        
print()