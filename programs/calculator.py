def sum(a,b):
    print("\nSum=",a+b)

def diff(a,b):
    print("\nDifference=",a-b)

def prod(a, b):
    print("\nProduct=", a*b)

def div(a, b):
    print("\nDivide=",format(a/b,'0.2f'))

print("**********Menu**********")
print("1.sum")
print("2.difference")
print("3.product")
print("4.division")
ch=int(input("Enter the choice:"))
if ch<5 and ch>0:
    print("\nEnter any two numbers:")
    a=int(input("a="))
    b=int(input("b="))
if(ch==1):
    sum(a,b)
elif(ch==2):
    diff(a,b)
elif(ch==3):
    prod(a,b)
elif(ch==4):
    div(a,b)
else:
    print("\nNo calculation for english professors!!!")