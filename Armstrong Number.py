n = int(input())
temp = n
s = 0

while n:
    r = n % 10
    s += r ** 3
    n //= 10

if s == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
