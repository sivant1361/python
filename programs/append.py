name=input("Enter the name:")
str=""
i=0
l=name.split()
for i in range(len(l)-1):
    name=l[i]
    str+=name[0].upper()+"."
str+=l[i+1]
print(str)