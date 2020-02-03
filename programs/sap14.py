import re

def match(str):
    pattern=input("Enter string to match:")
    if re.match(pattern,str):
        print("Match found:)")
    else:
        print("Match not found:(")

def replace(str):
    pattern=input("Enter a value to replace:")
    word=input("Enter the word from the string:")
    a=re.sub(word,pattern,str,1)
    print(a)

def search(str):
    pattern=input("Enter string to match:")
    if re.search(pattern,str):
        print("Match found:)")
    else:
        print("Match not found:(")

str=input("Enter a string:")
ch=int(input("Do you want to 1.match 2.search 3.replace:"))
if ch==1:
    match(str)
elif ch==2:
    search(str)
elif ch==3:
    replace(str)
else:
    print("Invalid input!!!")