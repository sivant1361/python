a=input("Enter the file name:")
with open(a,mode='r') as f:
    str=f.read()
    l=str.split()
    k=len(l)
    print(f"Number of words ={k}")