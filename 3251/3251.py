import sys

arr = list(map(int, sys.stdin.readline().split()))

answer = "P"

for i in range(len(arr)):
    if arr[i] < 40:
        answer = "F"
        break

if sum(arr) / len(arr) < 60:
    answer = "F"

print(answer)