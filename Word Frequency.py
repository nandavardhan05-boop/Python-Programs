s = input().split()

for word in set(s):
    print(word, s.count(word))
