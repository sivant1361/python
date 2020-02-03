try:
    f=open("Error.txt",mode='w')
    a=int(input("Enter something:"))
    f.write(str(a))
    f=open("Err.txt",mode='r')
    str=f.read()
    print(str)
except ValueError:
    print("It's a value error!!!")
except OSError:
    print("It's a os error!!!")
finally:
    print("Terminated!!!")