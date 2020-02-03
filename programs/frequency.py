msg=input("Enter a string:")
msg=msg.lower()
dict = {}
for word in msg:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]=dict[word]+1
print(dict)
for key,val in dict.items():
    print(key,"#"*val)
