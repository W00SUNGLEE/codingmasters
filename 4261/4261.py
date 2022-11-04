# 이분 매칭
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp)):
        graph[i].append(tmp[j])

selected = [-1] * (m + 1)

def bimatch(N):
    if visited[N]:
        return False
    visited[N] = True

    for num in graph[N]:
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = N
            return True

    return False

for i in range(n+1):
    visited = [False] * (n+1)
    bimatch(i)

result = 0
for i in range(1, m+1):
    if selected[i] > 0:
        result += 1

print(result)