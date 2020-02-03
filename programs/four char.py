import re
def fourchar(word):
    k=len(word)
    if(k>4):
        word+="ing"
    elif(k==4 and word[k-1]=='y'):
        l = re.findall(".", word)
        l.pop()
        word=""
        for i in l:
            word+=i
        word+="ly"
    return word

w=input("Enter a word:")
word=fourchar(w)
print(word)