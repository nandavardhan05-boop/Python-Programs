a = list(map(int, input().split()))
target = int(input())

d = {}

for i in range(len(a)):
    needed = target - a[i]

    if needed in d:
        print(d[needed], i)
        break

    d[a[i]] = i
