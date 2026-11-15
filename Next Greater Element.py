a = list(map(int, input().split()))

result = [-1] * len(a)
stack = []

for i in range(len(a)):
    while stack and a[i] > a[stack[-1]]:
        result[stack.pop()] = a[i]

    stack.append(i)

print(*result)
