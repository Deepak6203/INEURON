# Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle. Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side. This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.



# Validity of Triangle given sides
# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Reading Three Sides
side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))

# Function call & making decision

if is_valid_triangle(side_a, side_b, side_c):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')



# Run 1:
# -----------------
# Enter length of side a: 2
# Enter length of side b: 2
# Enter length of side c: 4
# Triangle is Valid.

# Run 2:
# -----------------
# Enter length of side a: 2
# Enter length of side b: 4
# Enter length of side c: 15
# Triangle is Invalid.