pw=input("Enter a password : ")
l=len(pw)
count=0
upper=0
lower=0
num=0
spl=0
i=0

while i <l:
    count+=1
    if 'A'<=pw[i]<='Z':
        upper+=1
    elif 'a'<=pw[i]<='z':
        lower+=1
    elif '0'<=pw[i]<='9':
        num+=1
    else:
        spl+=1
    i+=1

if 8<= count <=16 and upper >=1 and lower >=1 and spl >=1 and num >=1:
    print("STRONG PASSWORD: ",pw)
else:
    print("WEAK PASSWORD :",pw)
