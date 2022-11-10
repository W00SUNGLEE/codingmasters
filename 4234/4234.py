import sys

n, k = map(int, sys.stdin.readline().split())

store_list = list()

sum_candy = 0

dp = [-1 for i in range(k+101)]

for _ in range(n):
    candy, price = map(int, sys.stdin.readline().split())
    store_list.append([candy*price, candy])
    sum_candy += candy

if sum_candy < k:
    print(-1)

else:
    store_list.sort()

    dp[0] = 0

    answer_list = list()

    for i in range(n):
        for j in range(k-1, -1, -1):
            if dp[j] > -1:
                if dp[j+store_list[i][1]] == -1:
                    dp[j+store_list[i][1]] = dp[j] + store_list[i][0]
                else:
                    dp[j+store_list[i][1]] = min(dp[j]+store_list[i][0], dp[j+store_list[i][1]])

    answer = sys.maxsize
    for i in range(k, k+100):
        if dp[i] >= 0:
            answer = min(dp[i], answer)

    print(answer)