def count_factors(N):
    if N == 0:
        return 0  
    count = 1
    i = 2
    while i * i <= N:
        exponent = 0
        while N % i == 0:
            N //= i
            exponent += 1
        count *= (exponent + 1)
        i += 1
    if N > 1:
        count *= 2 
    return count
