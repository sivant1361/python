a=int(input("Enter mark 1:"))
b=int(input("Enter mark 2:"))
c=int(input("Enter mark 3:"))
d=int(input("Enter mark 4:"))
total=a+b+c+d
avg=total/4
print("Total=",total)
print("Average=",avg)
if avg>=75:
    print("Distinction")
elif avg>= 60 and avg<75:
    print("First division")
elif avg>=50 and avg<60:
    print("Second division")
elif avg>=40 and avg<50:
    print("Third division")
else:
    print("Fail")
