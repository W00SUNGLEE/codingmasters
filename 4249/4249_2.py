import sys

n = int(sys.stdin.readline())

land_list = list(map(int, sys.stdin.readline().split()))

if n == 2 or n == 3:
    print(sum(land_list))

else:

    dp = list()

    dp.append([land_list[0], 0])

    if land_list[0] > land_list[1]:
        dp.append([land_list[0], land_list[1]])
    else:
        dp.append([land_list[1], land_list[0]])

    if dp[0][0]+land_list[2] > dp[1][1]:
        dp.append([dp[0][0]+land_list[2], max(land_list[1], dp[0][1])])

    elif dp[0][0]+land_list[2] == dp[1][1]:
        dp.append([dp[0][0] + land_list[2], max(land_list[1], land_list[2], dp[0][1], dp[1][1])])

    else:
        dp.append([dp[1][0], max(land_list[2], dp[1][1])])

    for i in range(3, n):
        if dp[i-1][0] > dp[i-2][0]+land_list[i] and dp[i-1][0] > dp[i-3][0] + land_list[i]:
            dp.append([dp[i-1][0], max(dp[i-1][1], land_list[i])])

        elif dp[i-1][0] == dp[i-2][0]+land_list[i] and dp[i-1][0] > dp[i-3][0] + land_list[i]:
            dp.append([dp[i - 1][0], max(dp[i - 1][1], land_list[i], dp[i - 2][1], land_list[i-1])])

        elif dp[i-1][0] > dp[i-2][0]+land_list[i] and dp[i-1][0] == dp[i-3][0] + land_list[i]:
            dp.append([dp[i - 1][0], max(dp[i - 1][1], land_list[i], dp[i - 3][1], land_list[i-1], land_list[i-2])])

        elif dp[i-2][0]+land_list[i] > dp[i-1][0] and dp[i-2][0]+land_list[i] > dp[i-3][0] + land_list[i]:
            dp.append([dp[i-2][0]+land_list[i], max(dp[i - 2][1], land_list[i-1])])

        elif dp[i-2][0]+land_list[i] > dp[i-1][0] and dp[i-2][0]+land_list[i] == dp[i-3][0] + land_list[i]:
            dp.append([dp[i - 2][0] + land_list[i], max(dp[i - 2][1], land_list[i - 1], dp[i - 3][1], land_list[i-1], land_list[i-2])])

        elif dp[i-3][0] + land_list[i] > dp[i-1][0] and dp[i-3][0] + land_list[i] > dp[i-2][0]+land_list[i]:
            dp.append([dp[i - 3][0] + land_list[i], max(dp[i - 3][1], land_list[i-1], land_list[i-2])])

        elif dp[i-1][0] == dp[i-2][0]+land_list[i] and dp[i-1][0] == dp[i-3][0] + land_list[i]:
            dp.append([dp[i - 1][0], max(dp[i - 1][1], land_list[i], dp[i - 2][1], land_list[i - 1], dp[i - 3][1], land_list[i-1], land_list[i-2])])

    print(max(sum(dp[n-1]), dp[n-2][0]+max(dp[n-2][1], land_list[n-1]), dp[n-3][0] + max(dp[n-3][1], land_list[n-1], land_list[n-2])))

    print(dp)