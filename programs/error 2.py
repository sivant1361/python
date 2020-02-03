while 1:
    try:
        k=int(input("Enter the limit:"))
        for j in range(k):
            print(j+1)
            for k in range(15000000):
                pass
    except:
        print("Error has occured!!!")
    else:
        print("Dead end :( The clock has stopped!!!")
        break

