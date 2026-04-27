'''def greet():
    print("santoo")
greet()

def san(name):
    print("i love u", name)
san("chubby")

def add (a,b):
    return(a+b)

print(add(10,20))

# check odd or even
def eo(n):
    if n%2==0:
        print("even",n)
    else:
        print("odd",n)
    return
n=int(input())

eo(n)

# check largest of two number

def large(n1,n2):
    if n1>n2:
        return ("n1 is larger" , n1)
    else:
        return("n2 is larger " , n2)

n1=int(input())
n2=int(input())
print(large(n1,n2))

#factorial

def f(n):
    fact=1
    k=n
    while k >0:
        fact=fact*k
        k=k-1   
    return fact
n=int(input())
print(f(n))

# sum of list
def l_sum(l):
    s=0
    for i in l:
        s=i+s
    return s
lst=list(map(int,input().split()))
print(l_sum(lst))
      
# palindrome

def pal(s):
    a=len(s)-1
    temp=s
    res=""
    for i in s:
        if i==s[a]:
            a=a-1
            res=res+i
    if res==temp:
        print("palindrome")
    else:
        print("not palindrome")

s=input()
pal(s)'''

#count_vowels
def cv(s1):
    count=0
    for e in s1:
        if e.lower() in "aeiou":
            count+=1
    return count
s1=input()
print(cv(s1))
        
