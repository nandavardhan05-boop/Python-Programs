a = list(map(int, input().split()))
n = len(a) + 1

print(n * (n + 1) // 2 - sum(a))
