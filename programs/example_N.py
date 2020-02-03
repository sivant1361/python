fn=input("Enter the filename:")
with open(fn) as file:
    text=file.read()
    ct=0
    cs=0
    cn1=0
    for char in text:
        if char=="\t":
            ct+=1
        if char==" ":
            cs+=1
        if char=="\n":
            cn1+=1
print("tab",ct)
print("space",cs)
print("new line",cn1)
