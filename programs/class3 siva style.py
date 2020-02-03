class person:
    def __init__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

class publications:
    def __init__(self,no_rp,no_of_books,no_art):
        self.no_rp=no_rp
        self.no_of_books=no_of_books
        self.no_art=no_art
    def display(self):
        print("Number of research program published=",self.no_rp)
        print("Number of books published=",self.no_of_books)
        print("Number of articles published=",self.no_art)

class faculty(person,publications):
    def __init__(self,name,age,gender,desig,dept,no_rp,no_of_books,no_art):
        person.__init__(self,name,age,gender)
        publications.__init__(self,no_rp, no_of_books, no_art)
        self.desig=desig
        self.dept=dept

    def display(self):
        person.display(self)
        print("Designation=",self.desig)
        print("Department=",self.dept)
        publications.display(self)

n=input("Enter name:")
a=int(input("Enter age:"))
g=input("Enter gender:")
d=input("Enter degination:")
c=input("Enter course:")
r=int(input("Enter number of research programs:"))
b=int(input("Enter number of books published:"))
ar=int(input("Enter number articles published:"))
print('\n')
f=faculty(n,a,g,d,c,r,b,ar)
f.display()