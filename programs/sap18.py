f=open("file2.txt",mode='a')
str=input("Enter a string:")
f.write(str)
f.write('\n')
f.close()
f=open("file2.txt",mode='r')
fstr=f.read()
t=0
s=0
n=0
for i in range(len(fstr)):
    if(fstr[i]==' '):
        s=s+1
    elif(fstr[i]=='\n'):
        n=n+1
    elif(fstr[i]=='\t'):
        t=t+1
print("Number of spaces=",s)
print("Number of tabs=",t)
print("Number of newline=",n)
f.close()
