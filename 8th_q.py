n=int(input())
count=0
for i in range (2,n+1):
    if i*i==n:
        count+=1
        break

if count>=1:
    print(i,"is a perfect square")
else:
    print(n,"is not a perfect square")
