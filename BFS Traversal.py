from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input())

visited = [False] * n
queue = deque([start])
visited[start] = True

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
