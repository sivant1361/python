ch=int(input("Area:\n1.rectange\n2.triangle\n3.circle\n4.square\nEnter choice:"))
if (ch==1):
    a = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    area=a*b
    print("Area of rectangle=",area)
elif(ch==2):
    a = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    area=(a*b)/2
    print("Area of triangle=", area)
elif(ch==3):
    a = int(input("Enter the value of side:"))
    area=(22*a**2)/7
    print("Area of circle=",area)
elif(ch==4):
    a = int(input("Enter the value of side:"))
    area=a**2
    print("Area of square=",area)
else:
    print("Invalid Input!!!")