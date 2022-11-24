import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

apple_list = list(map(int, sys.stdin.readline().split()))
apple_dic = defaultdict(list)

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    apple_dic[a].append(b)
    apple_dic[b].append(a)

visited = [0 for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

def dfs(index):
    visited[index] = 1
    dp[index][0] = 0
    dp[index][1] = apple_list[index-1]

    for i in apple_dic[index]:
        if visited[i] == 0:
            dfs(i)

            dp[index][0] += max(dp[i][0], dp[i][1])
            dp[index][1] += dp[i][0]

dfs(1)

answer = max(dp[1][0], dp[1][1])

print(answer)