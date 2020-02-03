ch='y'
a=[]
while ch=='y':
    n=int(input("Enter number of elements:"))
    for i in range(n):
        b=int(input(f"Enter element {i+1}:"))
        if b>100:
            a.append("EXCESS")
        else:
            a.append(b)
    print("\nThe list is:")
    for i in a:
        print(i)
    ch=input("\nDo you want to enter more(y/n):")