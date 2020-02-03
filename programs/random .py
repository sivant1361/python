q=[]
a=[]
ch='y'
import random
n=0

while ch=='y' or ch=='Y':
    n=int(input("Enter number of questions to be added:"))
    for i in range(n):
        q.append(input(f"Question {i+1}:"))
        a.append(input(f"Answer {i+1}:"))
    ch=input("Do you want to enter more(y/n):")

ch='y'

while ch=='y' or ch=='Y':
    k=random.randint(0,n-1)
    print("Question:", q[k])
    ans=input("Enter the answer:")
    for i,j in zip(q,a):
        if(i==q[k] and ans==j):
            print("Correct answer :)")
        else:
            print("The answer is:",j)
    ch= input("Do you want to ask more(y/n):")