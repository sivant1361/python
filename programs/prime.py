n=int(input("Enter number of elements:"))
p=[]
c=[]
if n==1:
    print("No prime numbers available :(")
for i in range(2,n+1):
    flag=0
    for j in range(2,int(i/2)+1):
       if(i%j==0):
            flag=1
    if(flag!=1):
        p.append(i)
    else:
        c.append(i)
if n!=1:
    print("Prime number=",p)
    print("Composite numbers=",c)