import re
ch=input("Enter the string:")
result=re.findall(r'\b[aeiouAEIOU]\w+',ch)
print(result)

#$=last word
result=re.findall(r'\w+$',ch)
print("Last word:",result)

#^=first word
result=re.findall(r'^\w+',ch)
print("First word:",result)

# dot operator=split th words
chr=input("Enter a word")
l=re.findall('.',chr)
print(l)
