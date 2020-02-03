def function(name="unknown"):
    print(f"Hello it's me the functions!It's you {name} hereby to learn me :)")
    age=int(input("Enter your age:"))
    return age

name=input("Enter your name:")
age=function(name)
print("The function says your age is "+str(age))