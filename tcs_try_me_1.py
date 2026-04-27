s=input()

if s.isdigit():
    n=int(s)
    c=0
    for i in range(n):
        for j in  range (n):
            if i<=j and (i+j)%2==0:
                c+=1
    print(c)
else:
    print("Invalid message")
