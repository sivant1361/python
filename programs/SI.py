p=int(input("Principle amount="))
r=int(input("rate of interest="))
t=int(input("Number of years="))
ch=int(input("1.Simple interest\n2.Compound interest(1 or 2):"))
if (ch==1):
    si=(p*r*t)/100
    print("Simple interest=",si)
elif (ch==2):
    ci=(p*((1+(r/100))**t))-p
    print("Compound interest=",ci)
else:
    print("Invalid input!!!")