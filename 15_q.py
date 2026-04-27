lst=list(map(int,input().split()))
lst2=[]
for ch in lst:
    if ch %5==0 and ch%7==0:
        lst2.append(ch)

print(lst2)
