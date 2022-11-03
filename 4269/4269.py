import sys

sys.setrecursionlimit(10**6)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

answer = [sys.maxsize]

matrix[0][0] = 2

visited = [[[sys.maxsize, sys.maxsize] for _ in range(m)] for _ in range(n)]

def dfs(x, y, skill, count):
    if count > visited[x][y][skill]:
        return None

    else:
        visited[x][y][skill] = count

        if x == n-1 and y == m-1:
            answer[0] = min(count, answer[0])
            return None

        else:
            for xi, yi in move:
                new_x = x + xi
                new_y = y + yi

                if 0 <= new_x < n and 0 <= new_y < m:
                    if matrix[new_x][new_y] == '0':
                        matrix[new_x][new_y] = '2'
                        dfs(new_x, new_y, skill, count+1)
                        matrix[new_x][new_y] = '0'

                    elif matrix[new_x][new_y] == '1' and skill == 1:
                        dfs(new_x, new_y, skill-1, count+1)

dfs(0, 0, 1, 1)

if answer[0] == sys.maxsize:
    print(-1)

else:
    print(answer[0])