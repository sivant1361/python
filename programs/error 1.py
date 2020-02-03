while 1:
    try:
        a=int(input("Enter a number:"))
        print("The square of the given number is:",a**2)
        break
    except:
        print("You bagah!!!You have entered an incorrect answer:")
        continue
    finally:
        print("Mission completed:)")