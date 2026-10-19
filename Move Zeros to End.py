a = list(map(int, input().split()))

result = [x for x in a if x != 0]
result += [0] * (len(a) - len(result))

print(result)
