n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(a[i][j] + b[i][j], end=" ")
    print()
