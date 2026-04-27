N= int(input())
l=len(str(N))
temp=N
sum=0
while N>0:
    digit=N%10
    sum=sum+digit
    N=N//10
    
print(sum)


