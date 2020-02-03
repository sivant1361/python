n=int(input("Enter number of elements:"))
a=[]
for i in range(n):
    a.append((input(f"Element {i+1}:")))
print("Original list:",a)
print("Sorted list:",sorted(a))
print("Popped list:",a.pop())
print("Popped at specific location(0):",a.pop(0))
print("check",'3' in a)
print("Multiply by 10:",a*2)
a[0]='13'
print("List=",a)
del a[0:3]
print("Deleted at specific location:",a)
