class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = list(map(int, input().split()))

head = None
tail = None

for x in a:
    new = Node(x)

    if head is None:
        head = new
        tail = new
    else:
        tail.next = new
        tail = new

prev = None
current = head

while current:
    nxt = current.next
    current.next = prev
    prev = current
    current = nxt

head = prev

while head:
    print(head.data, end=" ")
    head = head.next
