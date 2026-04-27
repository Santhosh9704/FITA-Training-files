# Number of shoes
x = int(input())

# List of shoe sizes
sizes = list(map(int, input().split()))

# Number of customers
n = int(input())

money = 0

for i in range(n):
    size, price = map(int, input().split())
    
    if size in sizes:
        money += price
        sizes.remove(size)  # remove sold shoe

print(money)
