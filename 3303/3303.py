import sys

a, b, D, d = map(int, sys.stdin.readline().split())

longLine = max(a, b)

dp = [[sys.maxsize, -sys.maxsize] for _ in range(longLine + 1)]

for i in range(d, D + 1):
    if i <= longLine:
        dp[i][0] = 1
        dp[i][1] = 1

for i in range(1, longLine):
    if dp[i][1] > 0:
        for j in range(d, D + 1):
            if i + j <= longLine:
                dp[i + j][0] = min(dp[i][0] + 1, dp[i + j][0])
                dp[i + j][1] = max(dp[i][1] + 1, dp[i + j][1])

if dp[a][1] > 0 and dp[b][1] > 0:
    print("{} {}".format((dp[a][0] + dp[b][0]) * 2, (dp[a][1] + dp[b][1]) * 2))
else:
    print(-1)