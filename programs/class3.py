# write a program that a has a class faculty which inherit a class person and publications
class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
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

class faculty(person):
    def __init__(self,name,age,gender,desig,dept,no_rp,no_of_books,no_art):
        person.__init__(self,name,age,gender)
        self.desig=desig
        self.dept=dept
        self.pub=publications(no_rp,no_of_books,no_art)
    def display(self):
        person.display(self)
        print("Designation=",self.desig)
        print("Department=",self.dept)
        self.pub.display()
f=faculty("Siva",18,"Male","TIC","AI and ML",22,1,3)
f.display()