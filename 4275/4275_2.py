import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

apple_list = list(map(int, sys.stdin.readline().split()))

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    matrix[a][b] = 1
    matrix[b][a] = 1

count_list = [0 for _ in range(n)]

visited = [0 for _ in range(n+1)]

def dfs(index, count):
    count_list[count] += apple_list[index-1]

    for i in range(1, n+1):
        if matrix[index][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, count+1)

visited[1] = 1
dfs(1, 0)

dp = [count_list[0]]

if n == 1:
    print(dp[0])

elif n > 1:
    dp.append(max(count_list[1], count_list[0]))

    for i in range(2, n):
        dp.append(max(dp[i-2]+count_list[i], dp[i-1]))

    print(dp[n-1])