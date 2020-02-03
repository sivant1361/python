q=[]
a=[]
ch='y'
import random

while ch=='y' or ch=='Y':
    n=int(input("Enter number of questions to be added:"))
    for i in range(n):
        q.append(input(f"Question {i+1}:"))
        a.append(input(f"Answer {i+1}:"))
        print("\n")

    ch=input("Do you want to enter more(y/n):")

while ch=='y' or ch=='Y':
    ques=input("\nEnter a question:")
    flag=0
    for i,j in zip(q,a):
        if(i==ques):
            print("The answer is:",j)
            flag=1
    if(flag==0):
        ans=(input("Question not found!Enter the answer :) "))
        q.append(ques)
        a.append(ans)
    ch = input("Do you want to ask more(y/n):")