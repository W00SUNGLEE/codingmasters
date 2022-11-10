import sys

k = int(sys.stdin.readline())

for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())

    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n):
        dp[i+1][0] = i+1

    for i in range(m):
        dp[0][i+1] = i+1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

    print(dp[n][m])