import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

answer = [0]

def dfs(x, y):
    gas = matrix[x][y]

    if x == n-1 and y == n-1:
        answer[0] += 1
        return None

    if gas == 0:
        return None

    if x + gas < n:
        matrix[x][y] = 0
        dfs(x+gas, y)
        matrix[x][y] = gas

    if y + gas < n:
        matrix[x][y] = 0
        dfs(x, y+gas)
        matrix[x][y] = gas

dfs(0, 0)

print(answer[0])