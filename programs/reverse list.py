n=int(input("Enter number of elements:"))
a=[]
for i in range(n):
    a.append((input(f"Element {i+1}:")))
print("List=",a[::-1])
print(a.reversed())
