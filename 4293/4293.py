import sys

INF = int(1e9)

n, e = map(int, sys.stdin.readline().split())

graph = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = c
    graph[b - 1][a - 1] = c



def dfs(x, visited):
    if visited == (1 << n) - 1:
        return 0

    if dp[x][visited] != INF:
        return dp[x][visited]

    for i in range(0, n):
        if not graph[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]

answer = sys.maxsize

for i in range(n):
    dp = [[INF] * (1 << n) for _ in range(n)]
    print(dfs(i, 1 << i))
    print(dp)
    answer = min(answer, dfs(i, 1 << i))

print(answer)