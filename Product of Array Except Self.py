 a = list(map(int, input().split()))

result = []

for i in range(len(a)):
    product = 1

    for j in range(len(a)):
        if i != j:
            product *= a[j]

    result.append(product)

print(result)
