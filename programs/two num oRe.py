def OrE2(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    else:
        if a<b:
            return b
        else:
            return a

a=int(input("Enter a="))
b=int(input("Enter b="))
r=OrE2(a,b)
print("The num is ",r)