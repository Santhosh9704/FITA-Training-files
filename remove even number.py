n=list(map(int,input().split()))

a=[]

for ch in n:
    if ch%2!=0:
        a.append(ch)
print(a)
