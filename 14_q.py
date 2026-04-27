A=list(map(int,input().split()))
count=0
for ch in A:
    for n in A+1:
        if ch!=n:
            count+=1
print(count)
        
