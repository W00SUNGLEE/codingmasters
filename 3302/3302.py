import sys

n, m = map(int, sys.stdin.readline().split())

answer = [0 for _ in range(n+1)]

for _ in range(m):
    cost, tmp_len = map(int, sys.stdin.readline().split())
    cost //= tmp_len

    tmp = list(map(int, sys.stdin.readline().split()))

    for i in range(tmp_len):
        answer[tmp[i]] += cost

for i in range(1, n+1):
    print(answer[i], end=" ")
print()