def search(a, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return search(a, low, mid - 1, key)
    else:
        return search(a, mid + 1, high, key)

a = list(map(int, input().split()))
key = int(input())

print(search(a, 0, len(a) - 1, key))
