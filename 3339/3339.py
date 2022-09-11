import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

matrix = [[0 for _ in range(221)] for _ in range(221)]
matrix[x1+100][y1+100] += 1
answer = [0]

def dfs(x, y, x2, y2, count, n):
    if count == n:
        if x == x2 and y == y2:
            answer[0] += 1
        return None

    for a, b in move:
        xi = x + a
        yi = y + b

        if matrix[xi+100][yi+100] == 0:
            matrix[xi + 100][yi + 100] += 1
            dfs(xi, yi, x2, y2, count+1, n)
            matrix[xi + 100][yi + 100] -= 1

dfs(x1, y1, x2, y2, 0, n)

print(answer[0])