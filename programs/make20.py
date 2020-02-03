def make20(i,j):
    if(i+j==20 or i==20 or j==20):
        print("Valid numbers:)")
    else:
        print("Invalid numbers:(")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
make20(a,b)