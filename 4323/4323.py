import sys

money, n = map(int, sys.stdin.readline().split())

marry_list = list(map(int, sys.stdin.readline().split()))

answer = 0

marry_list.sort(reverse=True)

for i in range(n):

    if money >= marry_list[i]:
        money -= marry_list[i]
        answer += 1

    else:
        continue

print(answer)