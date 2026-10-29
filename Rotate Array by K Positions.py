a = list(map(int, input().split()))
k = int(input())

k = k % len(a)

result = a[-k:] + a[:-k]

print(result)
