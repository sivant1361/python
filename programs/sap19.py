def num():
    while True:
        try:
            a =int(input("Enter a="))
            print("The number is ",a)
        except :
            print("You bagah!!!you had did an error to check me:)\n")
            continue
        else:
            print("Yes thank you:)")
            break
        finally:
            print("Mission completed!!!\n")
num()
