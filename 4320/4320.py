import sys

sys.setrecursionlimit(10**5)

n, m = map(int, sys.stdin.readline().split())

vistied = [0 for _ in range(n+1)]
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    matrix[a][b] = 1
    matrix[b][a] = 1

def dfs(index):
    print(index, end=" ")
    vistied[index] = 1

    for i in range(1, n+1):
        if matrix[index][i] == 1 and vistied[i] == 0:
            dfs(i)

dfs(1)
