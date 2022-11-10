import sys
from collections import defaultdict

n, q = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

parent = [i for i in range(n+1)]
friend = [1 for _ in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
        friend[a] += friend[b]

    else:
        parent[a] = b
        friend[b] += friend[a]

for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] == 1:
        if query[1] == query[2]:
            continue

        if query[1] not in graph[query[2]]:
            graph[query[1]].append(query[2])
            graph[query[2]].append(query[1])

            if find_parent(parent, query[1]) == find_parent(parent, query[2]):
                continue

            else:
                union_parent(parent, query[1], query[2])

    elif query[0] == 2:
        print(friend[find_parent(parent, query[1])] - len(graph[query[1]]) - 1)