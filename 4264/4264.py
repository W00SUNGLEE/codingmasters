import sys

n = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = 1

    for j in range(i):
        if input_list[j] < input_list[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))