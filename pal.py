s=input()
l=len(s)-1
res=""
temp=s

for ch in s:
    if ch==s[l]:
        l=l-1
        res=res+ch
if res==temp:
    print("palindrom")
else:
    print("not palidrome")
