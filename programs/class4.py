'''
bank account:
    owner
    balance
    methods:
        deposit
        withdraw
'''
from os import system,name
class bankaccount:

    def __init__(self,o,bal):
        self.owner=o
        self.balance=bal

    def od(self):
        print("***********************************")
        print("Owner details:")
        print("\tName:",self.owner)
        print("\tBalance:",self.balance)
        print("***********************************")

    def withdraw(self,wa):
        if(self.balance>=1500 and wa<=self.balance):
            self.balance=self.balance-wa
            print("\nNetbalace after withdrawal=",self.balance)
        else:
            print("Minimum balance required:(")

    def deposit(self,da):
        self.balance+=da
        print("\nNetbalance after deposit=",self.balance)

a=input("Enter owner name:")
b=int(input("Enter initial balance:"))
ba=bankaccount(a,b)
ba.od()
ch='y'
while ch=='y' or ch=='y':
    c=input("\nEnter withdraw or deposit(w/d):")
    if(c=='w' or c=='W'):
        w=int(input("Enter withdraw amount:"))
        ba.withdraw(w)
        ba.od()
    elif(c=='d' or c=='D'):
        d = int(input("Enter deposit amount:"))
        ba.deposit(d)
        ba.od()
    else:
        print("No services offered for audience :)")
    ch=input("Do you want to continue(y/n):")
