import sys

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

answer_list = [0 for _ in range(v+1)]

for i in range(1, v + 1):
    answer_list[find(i)] = 1

print(sum(answer_list))