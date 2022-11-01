import sys

n = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

a_list.sort(reverse=True)
b_list.sort(reverse=True)

answer = 0

for i in range(n):
    answer += a_list[i] * b_list[i]

print(answer)