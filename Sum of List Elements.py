def total(a, n):
    if n == 0:
        return 0
    return a[n - 1] + total(a, n - 1)

a = list(map(int, input().split()))
print(total(a, len(a)))
