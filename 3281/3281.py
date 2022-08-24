import sys

n, k = map(int, sys.stdin.readline().split())

ad_list = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(0, len(ad_list)):
    tmp = ad_list[i:i+k]
    if 0 not in tmp:
        answer = max(sum(tmp), answer)

print(answer)