l=list(input())
a=[]
for ch in l:
   
    if ch.isdigit():
        n=int(ch)
        if n%2!=0:
            s=n**2
            a.append(s)
print (a)

