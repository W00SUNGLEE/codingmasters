import sys

n = int(sys.stdin.readline())

dp = [0, 1, 3]

for i in range(3, n+1):
    dp.append(2*dp[i-2] + dp[i-1])

print(dp[n]%796796)