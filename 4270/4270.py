import sys

n = int(sys.stdin.readline())

p = 10007

dp = [0, 0, 1]

if n < 3:
    print(dp[n])

else:
    for i in range(3, n+1):
        dp.append(((i-1)*((dp[i-1]%p+dp[i-2]%p)%p))%p)

    print(dp[n])