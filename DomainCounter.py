import re
#domain counter
l=["xyz@gmail.com@a.wow","pqr@mail.com", "w@hotmail.in", "xyz@mail.in"]
def countit():
    d={}
    regex="@\w+\.\w+$"
    for i in l:
        a=re.findall(regex, i)[0]
        b=re.match(regex, i)
        print(b.group())
        print(b.group(1))
        if a in d:
            d[a]+=1
        else:
            d[a]=1
    print(d)
