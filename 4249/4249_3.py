import sys

n = int(sys.stdin.readline())

land_list = list(map(int, sys.stdin.readline().split()))

if n == 2 or n == 3:
    print(sum(land_list))

else:
    answer = 0

    for i in range(n):
        tmp = land_list[i]
        land_list[i] = 0

        dp = list()

        dp.append(land_list[0])
        dp.append(max(land_list[1], land_list[0]))
        dp.append(max(dp[0]+land_list[2], dp[1]))

        for j in range(3, n):
            dp.append(max(dp[j-3]+land_list[j], dp[j-2]+land_list[j], dp[j-1]))

        answer = max(dp[n-1] + tmp, answer)

        land_list[i] = tmp

    print(answer)