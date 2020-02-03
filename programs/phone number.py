import re
pattern=r"[06789]"
n=int(input("Enter  number of phone numbers:"))
list=[]
for i in range(n):
    list.append((input(f"Number {i+1}:")))
for i in list:
    if(re.search(pattern,i[0]) and len(i)==10):
        print(i,"is valid number!")
    else:
        print(i,"is invalid number!")