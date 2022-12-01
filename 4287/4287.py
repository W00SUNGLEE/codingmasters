import sys

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = list(map(int, sys.stdin.readline().split()))

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    else:
        if dp[x][y] == -1:
            dp[x][y] = 0

            for xi, yi in move:
                new_x = x + xi
                new_y = y + yi

                if 0 <= new_x < n and 0 <= new_y < m:
                    if matrix[new_x][new_y] < matrix[x][y]:
                        dp[x][y] += dfs(new_x, new_y)

    return dp[x][y]


dfs(0, 0)

print(dp[0][0]%998244353)