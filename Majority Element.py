 a = list(map(int, input().split()))

for x in a:
    if a.count(x) > len(a) // 2:
        print(x)
        break
