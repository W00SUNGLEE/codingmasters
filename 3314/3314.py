import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

tmp = sum(arr) % n
avg = sum(arr) // n

answer = 0

for i in range(n):
    answer += abs(avg-arr[i])

print((answer-tmp) // 2 + tmp)
