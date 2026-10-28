n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        print(a[top][i], end=" ")
    top += 1

    for i in range(top, bottom + 1):
        print(a[i][right], end=" ")
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(a[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(a[i][left], end=" ")
        left += 1
