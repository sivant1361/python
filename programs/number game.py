import random
class vtl(Exception):
    def dis(self):
        print("The entered value is larger than the expected value:")

class vts(Exception):
    def dis(self):
        print("The entered value is smaller than the expected value:")

num=random.randint(0,20)
flag=0
k=0
print("**********Guessing Game:**********\n")
name=input("Enter your name:")
print(name.capitalize(),"welcome to the number game:)\n")
while True:
    gn=int(input("Enter the number:"))
    if(num==gn):
        flag=1
    else:
        if(gn>num):
            v1=vtl()
            v1.dis()
        elif(gn<num):
            v=vts()
            v.dis()
        k=k+1
    if(k==0 and flag==1):
        print("You are the best:)")
    elif(k == 1 and flag==1):
        print("You are the second best:)")
    elif(k>10):
        print("Better luck next time:(")
        break
    if(flag==1):
        print(f"\nNumber found at the {k+1}th attempt!!!")
        break