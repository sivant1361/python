s=int(input("Enter the salary:"))
g=input("Enter the gender(m/f):")
r=0
if(s<=10000):
    r=2
if(g=="m"):
    r=r+5
elif(g=='f'):
    r=r+10
s+=(r*s)/100
print("Salary=",s)
