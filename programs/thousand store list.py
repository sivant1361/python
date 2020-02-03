s=[]
b=[]
r=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(r):
    n=int(input(f"Element {i+1}:"))
    if(n>=1000):
        b.append(n)
    else:
        s.append(n)
print("Bigger values=",b)
print("Smaller values=",s)