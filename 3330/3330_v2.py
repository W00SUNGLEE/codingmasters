import sys

n = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))
card.reverse()

dp = [[-sys.maxsize, -sys.maxsize] for _ in range(n+1)]

dp[1][1] = card[0]

if n > 1:
    dp[2][1] = card[0] + card[1]

if n > 2:
    dp[3][1] = card[0] + card[1] + card[2]

for i in range(1,n):
    if dp[i][0] > -sys.maxsize:
        dp[i + 1][1] = max(dp[i][0] + card[i], dp[i + 1][1])
        if i + 1 < n:
            dp[i + 2][1] = max(dp[i][0] + card[i] + card[i + 1], dp[i + 2][1])
        if i + 2 < n:
            dp[i + 3][1] = max(dp[i][0] + card[i] + card[i + 1] + card[i + 2], dp[i + 3][1])

    if dp[i][1] > -sys.maxsize:
        dp[i+1][0] = max(dp[i][1]-card[i], dp[i+1][0])
        if i + 1 < n:
            dp[i + 2][0] = max(dp[i][1] - card[i] - card[i+1], dp[i + 2][0])
        if i + 2 < n:
            dp[i + 3][0] = max(dp[i][1] - card[i] - card[i+1] - card[i+2], dp[i + 3][0])

print(max(dp[n]))