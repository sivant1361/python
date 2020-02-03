import re
password=[]

while 1:
    flag=1
    pas=input("Enter a password:")
    if (re.search((r"['a'-'z']"), pas)):
        pass
    else:
        flag = 0
        print("One small letter should be used!")
    if(re.search((r"['A'-'Z']"), pas) or pas[0].isupper()):
        pass
    else:
        flag=0
        print("One capital letter should be used!")
    if (re.search((r"[0-9]"),pas)):
        pass
    else:
        flag=0
        print("One special character should be used!")
    if (re.search((r"[$#@]"), pas)):
        pass
    else:
        flag=0
        print("One number should be used!")
    if (len(pas)>=6):
        pass
    else:
        flag=0
        print("Password length is too small(min=6)!!!")
    if(flag==1):
        print("Password Accepted :)")
        password.append(pas)
        break
    else:
        print("Password Decline :(")
print("\nThe registered passwords are the following:",password)