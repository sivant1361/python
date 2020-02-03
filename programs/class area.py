class circle:
    def __init__(self,r):
        self.a=r
    def area(self):
        return (22*a*a)/7

class rectangle:
    def __init__(self,r,v):
        self.a=r
        self.b=v
    def area(self):
        return a*b

ch=input("Select area of circle or rectangle(c/r):")
if(ch=='r'):
    a=int(input("Enter length:"))
    b=int(input("Enter breadth:"))
    c=rectangle(a,b)
    r=c.area()
elif(ch=='c'):
    a = int(input("Enter radius:"))
    c=circle(a)
    r=c.area()
else:
    print("Invalid Input!!!")
print("Area=",r)
