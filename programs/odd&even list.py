n=int(input("Enter number of elements:"))
a=[]
odd=[]
even=[]
for i in range(n):
    a.append(int(input(f"Enter element {i+1}:")))
for j in a:
    if(j%2==0):
       even.append(j)
    else:
        odd.append(j)
print("Odd list:",odd)
print("Even list:",even)
