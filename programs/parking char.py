ch=int(input("1.car\n2.bike\n3.van\nEnter choice:"))
k=0
if ch==1:
    t = int(input("Enter the duration:"))
    cost=20*t
elif ch==2:
    t = int(input("Enter the duration:"))
    cost=15*t
elif ch==3:
    t = int(input("Enter the duration:"))
    cost=30*t
else:
    print("Free cost for nadarajar service :)")
    k=1
if(k!=1):
    print("Cost=",cost)
