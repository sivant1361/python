name=input("Enter a string:")
print("Break statement:")
for i in name:
    if (i=='a'):
        break
    print(i)
print("\nContinue statement:")
for i in name:
    if (i=='a'):
        continue
    print(i)
print("\nPass statement:")
for i in name:
    if (i=='a'):
        pass
    print(i)