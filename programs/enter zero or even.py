class prompt(Exception):

    def print(self):
        print("The number is lesser than zero!!!")

try:

    num=int(input("Enter a number:"))

    if(num>=0):
        print(num)
    else:
        p=prompt()
        p.print()

except:
    print("Error!!!")
