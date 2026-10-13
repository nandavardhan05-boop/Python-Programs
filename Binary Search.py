a = list(map(int, input().split()))
key = int(input())

low, high = 0, len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == key:
        print("Found")
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")
