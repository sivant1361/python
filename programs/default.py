def prog(name,c="python"):
    print("Name:",name)
    print("Course:",c)

n=input("Enter your name:")
ch=input("Do you want to enter the course(y/n):")
if(ch=='y' or ch=='Y'):
    course=input("Enter the course:")
    prog(n,course)
else:
    prog(n)
