import re
k=0
a=input("Enter the file name:")
with open(a,mode='r') as f:
    str=f.read()
    c=re.findall("\w",str)
    for i in c:
        if i.isalnum():
            k=k+1
    print("Number of character is:",k)