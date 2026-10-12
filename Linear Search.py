a = list(map(int, input().split()))
key = int(input())

for i in range(len(a)):
    if a[i] == key:
        print("Found at", i)
        break
else:
    print("Not Found")
