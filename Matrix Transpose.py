n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    for i in range(n):
        print(a[i][j], end=" ")
    print() 
