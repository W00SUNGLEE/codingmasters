import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+m+1)]

for i in range(1, m+1):
    tmp = list(map(int, sys.stdin.readline().split()))

    graph[n+i] = tmp

    for j in range(len(tmp)):
        graph[tmp[j]].append(n+i)

deq = deque()

visited = [0 for _ in range(n+m+i)]
visited[1] = 1

deq.append((1, 1))

answer = -1

while deq:
    index, count = deq.popleft()

    if index == n:
        answer = count
        break

    for i in range(len(graph[index])):
        if visited[graph[index][i]] == 0:
            visited[graph[index][i]] = 1

            if graph[index][i] > n:
                deq.append((graph[index][i], count))

            else:
                deq.append((graph[index][i], count+1))

print(answer)