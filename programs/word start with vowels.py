import re
ch=input("Enter the string:")
l=ch.split()
print(l)
p=r'[aeiouAEIOU]'
for i in range(len(l)):
    ch=l[i]
    if(re.search(p,ch[0])):
        print(ch)