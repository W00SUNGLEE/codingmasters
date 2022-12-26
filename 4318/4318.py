import sys

n = int(sys.stdin.readline())

soldier_list = list(map(int, sys.stdin.readline().split()))

soldier_list.sort()

answer = 0

for i in range(n):
    tmp = soldier_list[i] * (n-i)

    if tmp > answer:
        answer = tmp

print(answer)