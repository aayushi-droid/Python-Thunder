'''
Problem statement: Write a function that takes the base and height of a triangle and return its area.
Problem Link: https://edabit.com/challenge/3CaszbdZYGN4otQD8
'''
print("================================================================================")    
print("\n")
print("""Welcome to area and paremeter finder </>
\n
Committed by : Koshal67 
GitHub Link : https://github.com/Koshal67/
\n""")
print("================================================================================")    
print("\n")

print(" I want to find : ")
print("""(1) Paremeter
(2) Area """)

user = str(input("Enter your choice by entering preffered number : "))
print("\n")
print("================================================================================")    
if user == "1" :
    print("""I want to find the paremeter of : """)
    print("""(1) Square
    (2) Rectangle
    (3) Triangle
    (4) Circle
    """)
    user2 = str(input("Enter your choice by entering preffered number : "))
    if user2 == "1" :
        side = float(input("Enter the side of the Square : " ))
        oresult = side*4
        result = str(oresult)
        print("Paremeter of Square = " +result+ " : ")

    elif user2 == "2" :
        l = float(input("Enter the length of the Rectangle : "))
        b = float(input("Enter the breadth of the Rectangle : "))
        oresult = 2*(l+b)
        result = str(oresult)
        print("Paremeter of the rectangle = "+result+ " : ")

    elif user2 == "3" :
        side1 = float(input("Enter the 1st side of the Triangle : "))
        side2 = float(input("Enter the 2nd side of the Triangle : "))
        side3 = float(input("Enter the 3rd side of the triangle : "))
        oresult = side1+side2+side3
        result = str(oresult)
        print("Paremeter of the Triangle = "+result+ " : " )

    elif user2 == "4" :
        r = float(input("Enter the radius of the Triangle :"))
        oresult = (2*22/7*r)
        result = str(oresult)
        print("Circumfrence of the circle = "+result+ " : " )

    else :
        print("Please enter a valid option : ")

elif user == "2" :
    print("""I want to find the area of : """)
    print("""(1) Square
    (2) Rectangle
    (3) Triangle
    (4) Circle
    """)
    user2 = str(input("Select your choice by entering preffered number : "))
    if user2 == "1" :
        side = float(input("Enter the side of the square :"))
        oresult = side*side
        result = str(oresult)
        print("Are of Square = "+result+" : " )

    elif user2 == "2" :
        length = float(input("Enter the length of the rectangle : "))
        breadth = float(input("Enter the breadth of the rectangle : "))
        oresult = length*breadth
        result = str(oresult)
        print("Area of the Rectangle = "+result+" : ")

    elif user2 == "3" :
        b = int(input("Enter the base of the Triangle : "))
        h = int(input("Enter the height of the Triangle : "))
        oresult = (b*h)/2
        result = str(oresult)
        print("Area of the Triangle = "+result+ " : ")

    elif user2 == "4" :
        r = float(input("Enter the radius of the Circle : "))
        oresult = 22/7*(r*r)
        result = str(oresult)
        print("Area of the circle = " +result+ " : ")

    else :
        print("Please enter a valid option : ")

else :
    print("Please enter a valid option : ")
    
    
    
