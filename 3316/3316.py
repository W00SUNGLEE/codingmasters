import sys

n = int(sys.stdin.readline())

arr = list()

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

answer = [-1, -1]

for i in range(1, 31):
    tmp = 0
    for j in range(n):
        if arr[j][0] <= i <= arr[j][1]:
            tmp += 1

    if tmp > answer[0]:
        answer[0] = tmp
        answer[1] = i

print(answer[1])