import sys

n = int(sys.stdin.readline())

answer = 0
tmp = 1

while tmp < n:
    answer += 1
    tmp += answer

print(answer)