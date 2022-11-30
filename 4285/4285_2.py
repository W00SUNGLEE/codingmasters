import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

child_dict = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a not in child_dict[b]:
        child_dict[b].append(a)

matrix = list()

for key, value in child_dict.items():
    matrix.append(value)

visited = [0 for _ in range(n+1)]
answer = [0]

def dfs(index):
    if index == len(matrix):
        tmp = 0
        for i in range(len(visited)):
            if visited[i] > 0:
                tmp += 1

        answer[0] = max(tmp, answer[0])
        return None

    else:
        check = 0
        for i in range(len(matrix[index])):
            if visited[matrix[index][i]] == 0:
                visited[matrix[index][i]] += 1
                dfs(index+1)
                visited[matrix[index][i]] -= 1
                check += 1

        if check == 0:
            dfs(index+1)

dfs(0)
print(answer[0])
