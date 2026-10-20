a = list(map(int, input().split()))

even = odd = 0

for x in a:
    if x % 2 == 0:
        even += x
    else:
        odd += x

print("Even:", even)
print("Odd:", odd)
