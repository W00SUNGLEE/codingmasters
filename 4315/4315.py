import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if len(graph[i]) == 0:
        print("no")

    else:
        graph[i].sort()

        for j in graph[i]:
            print(j, end=" ")

        print()