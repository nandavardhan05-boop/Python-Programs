 a = list(map(int, input().split()))

current = maximum = a[0]

for i in range(1, len(a)):
    current = max(a[i], current + a[i])
    maximum = max(maximum, current)

print(maximum)
