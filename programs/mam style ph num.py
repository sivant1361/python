import re
n=int(input("Enter  number of phone numbers:"))
list=[]
for i in range(n):
    list.append((input(f"Number {i+1}:")))
for i in list:
    result=re.findall(r'[6-9]{1}[0-9]{9}',i)
    if result:
        print(result)