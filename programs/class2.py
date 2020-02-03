class person:
    def __init__(self,f,l):
        self.fn=f
        self.ln=l
    def pn(self):
        print("The name of the student is ",self.fn,self.ln)

class std(person):
    print("Student Class:)")

f=input("Enter first name:")
l=input("Enter last name:")
s=std(f,l)
s.pn()