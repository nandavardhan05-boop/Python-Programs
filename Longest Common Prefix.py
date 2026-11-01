a = input().split()

prefix = a[0]

for word in a[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)
