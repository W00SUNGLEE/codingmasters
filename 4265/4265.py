import sys

sys.setrecursionlimit(10**6)

move = [(1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

answer = [0]

def dfs(x, y, count):
    if x == n-1 and y == m-1:
        answer[0] = max(count, answer[0])
        return None

    for xi, yi in move:
        new_x = x+xi
        new_y = y+yi

        if 0 <= new_x < n and 0 <= new_y < m:
            if matrix[new_x][new_y] >= 0:
                next_count = matrix[new_x][new_y]
                matrix[new_x][new_y] = -1
                dfs(new_x, new_y, count+next_count)
                matrix[new_x][new_y] = next_count

count = matrix[0][0]
matrix[0][0] = -1
dfs(0, 0, count)

print(answer[0])
