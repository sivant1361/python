import re
d={}
k=""
ecom=["sivant1313@gmail.com","sivant@gmail.com","sivant13@yahoo.com","sivant1313@reddif.com"]
for i in ecom:
    j= re.findall(r"[@]\w+[.]\w+",i)
    k=k.join(j)
    if k not in d:
        d[k]=1
    else:
        d[k]=d[k]+1
    print(d)
