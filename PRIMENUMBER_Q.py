n=int(input())
count=0
for i in range (2,n):
    if n//i==0:
        count+=1
    else:
        count=0
if count<=1:
    print("prime number")
else:
    print("Not prime number")
