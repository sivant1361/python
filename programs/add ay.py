import re
def adday(word):
    if word[0] in 'aeiouAEIOU':
        print(word+"ay")
    else:
        l=re.findall(".",word)
        print("W=",w)
        print(word[1:]+w+"ay")

w=input("Enter a word:")
adday(w)