import sys
from collections import defaultdict
import copy

n, m = map(int, sys.stdin.readline().split())

root = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(index, first, second):
    if index == first:
        paths[0] = copy.deepcopy(visited)
        check[0] = 0

    if index == second:
        paths[1] = copy.deepcopy(visited)
        check[1] = 0

    if sum(check) == 0:
        return None

    for next_index in graph[index]:
        if next_index not in visited:
            visited.append(next_index)
            dfs(next_index, first, second)
            visited.pop()
            if sum(check) == 0:
                return None

for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())

    paths = [[root], [root]]
    check = [1, 1]

    visited = [root]

    dfs(root, first, second)

    answer = 0

    for i in range(min(len(paths[0]), len(paths[1]))):
        if paths[0][i] == paths[1][i]:
            answer = paths[0][i]

        else:
            break

    print(answer)