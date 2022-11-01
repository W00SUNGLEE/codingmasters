import sys

n, m = map(int, sys.stdin.readline().split())

answer = 1
tmp_n = n+m-1
tmp_m = m

for i in range(m):
    answer *= tmp_n % 1000000007
    answer %= 1000000007
    answer *= pow(tmp_m, -1, 1000000007) % 1000000007
    answer %= 1000000007
    tmp_n -= 1
    tmp_m -= 1

print(answer % 1000000007)