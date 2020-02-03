class Siva():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def print(self):
        print("\nInside class!!!")
        print("a=",self.a,"b=",self.b)

a=int(input("Enter a="))
b=int(input("Enter b="))
s=Siva(a,b)
s.print()
print("\nClass variables:")
print("\ta=",s.a)
print("\tb=",s.b)
