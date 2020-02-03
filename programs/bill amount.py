print("**********BILLING SYSYTEM**********")
a=[]
print("1.milk\n2.ghee\n3.milkshake\n4.ice cream")
print("\nEnter the quantity of each item:")
for i in range(4):
    a.append(int(input(f"   Item {i+1}:")))
amount=a[0]*30+a[1]*40+a[2]*25+a[3]*20
print("\nAmount=",amount)
if(amount>=300):
    print("Discount Amount+_=",(amount*5)/100)
    amount+=(amount*5)/100
print("GST=2.5% & TAX=1%")
print("Net amount=",amount+(3.5*amount)/100)