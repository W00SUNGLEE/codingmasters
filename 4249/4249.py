import sys

n = int(sys.stdin.readline())

land_list = list(map(int, sys.stdin.readline().split()))

dp = list()

dp.append([land_list[0], 0])

if land_list[0] > land_list[1]:
    dp.append([land_list[0], land_list[1]])
else:
    dp.append([land_list[1], land_list[0]])

dp.append([land_list])

for i in range(2, n):
    if dp[i-2][0]+land_list[i] > dp[i-1][1]:
        dp.append([dp[i-2][0]+land_list[i], max(land_list[i-1], dp[i-2][1])])

    elif dp[i-2][0]+land_list[i] == dp[i-1][1]:
        dp.append([dp[i - 2][0] + land_list[i], max(land_list[i - 1], land_list[i], dp[i - 2][1], dp[i - 1][1])])

    else:
        dp.append([dp[i - 1][0], max(land_list[i], dp[i - 1][1])])


print(max(dp[n-1][0]+dp[n-1][1], dp[n-2][0]+ dp[n-2][1]))