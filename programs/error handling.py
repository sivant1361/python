try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a+b
    print(c)
except(TypeError,ValueError):
    print("Type error or Value error!!!")
finally:
    print("Misson completed!!!")