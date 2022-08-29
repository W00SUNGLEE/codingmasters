import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(n+1)]

j = 1
for i in range(4, n+1, 4):
    arr[i] = j**2
    j += 1

j = 1
for i in range(6, n + 1, 4):
    arr[i] = arr[i-2] + j
    j += 1

for i in range(5, n+1, 2):
    arr[i] = arr[i-1]

print(arr)
