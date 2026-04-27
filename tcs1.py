s = input()

if s.isdigit():
    n = int(s)
    c = 0
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if (i + j) % 2 == 0:
                c += 1
    print(c)
else:
    print("Invalid")

