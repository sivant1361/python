while 1:
    try:
        a=input("Enter the name:")
        b=int(input("Enter the age:"))
        if b>=18:
            print(a.capitalize(),"you are eligible to vote:)")
        else:
            print(a.capitalize(),"you are not eligible to vote:(")
    except:
        print("Some error has occured:")
    else:
        break