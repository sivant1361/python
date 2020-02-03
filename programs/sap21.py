def vote(a,n="Indian"):
    if(a>=18 and n=="Indian"):
        print("Eligible to vote :)")
    else:
        print("Not eligible to vote :(")

age=int(input("Enter the age:"))
ch=input("Do you want to enter the nationality(y/n):")
if(ch=='y' or ch=='Y'):
    b=input("Enter nationality:")
    vote(a=age,n=b)
else:
    vote(age)