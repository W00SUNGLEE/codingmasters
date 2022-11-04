import sys

n = int(sys.stdin.readline())

student_list = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp[0] = 1
dp2[0] = 1

answer = 0

for i in range(1, n):
    dp[i] = 1
    dp2[i] = 1

    for j in range(i):
        if student_list[j] < student_list[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

        if student_list[j] > student_list[i] and dp2[j] + 1 > dp2[i]:
            dp2[i] = dp2[j] + 1

    answer = max(dp[i]+dp2[i]-1, answer)


print(dp, dp2)
print(answer)
