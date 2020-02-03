import re
ch=input("Enter a word:")
k=len(ch)
str=""
l=re.findall(".",ch)
if(ch[k-1]=='f'):
    l.pop()
    for i in l:
        str+=i
    str+="ves"
elif(ch[k-2]=='f'):
    l.pop()
    l.pop()
    for i in l:
        str+=i
    str+="ves"
elif(ch[k-1]=='y'):
    l.pop()
    for i in l:
        str+=i
    str+="ies"
elif(ch[k-1]=='h'):
    str+=ch
    str+="es"
else:
    str+=ch+"s"
print(str)
