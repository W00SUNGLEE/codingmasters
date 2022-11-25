import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    for j in range(i+a, n+1):
        if dp[i] + b > dp[j]:
            dp[j] = dp[i] + b

print(dp[n])
