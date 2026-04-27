n=0
while n<101:
    n+=1
    if n%3==0 and n%5==0:
        print("fizz buss")
    elif n%3==0:
        print("fizz")
    elif n%5==0:
        print("buss")

    else:
        print(n)
