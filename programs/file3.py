a=input("Enter the file name:")
w=input("Enter the word to be searched:")
k=0
with open(a,mode='r') as f:
    str=f.read()
    l=str.split()
    for i in l:
        if w==i:
            k=k+1
    print(f"The number of word '{w}' in the given file is :{k}")