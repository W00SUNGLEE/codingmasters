import sys

sys.setrecursionlimit(10**6)


n, m = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[b][a] = 1

tmp = [0]
visited = [0 for _ in range(n+1)]

def dfs(index):
    result = 1
    if visited[index] == 1:
        return 0

    else:
        visited[index] = 1

        for i in range(1, n+1):
            if matrix[index][i] == 1:
                result += dfs(i)
        return result

result_list = list()

for i in range(n+1):
    visited = [0 for _ in range(n + 1)]
    result_list.append(dfs(i))

answer_list = list()

for i in range(n+1):
    if result_list[i] == max(result_list):
        answer_list.append(i)

for i in range(len(answer_list)):
    print(answer_list[i], end=" ")