class name(Exception):
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Hello {self.name} :)")

try:
    uname=(input("Enter the name:"))
    raise name(uname)
except name as r:
    r.display()