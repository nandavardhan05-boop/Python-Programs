n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += a[i][k] * b[k][j]

for row in result:
    print(*row)
