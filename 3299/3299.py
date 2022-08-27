import sys

n, a = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(n+1)]

arr[a] = 1

m = int(sys.stdin.readline())

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    if arr[x] == 1:
        arr[y] = 1

    if arr[y] == 1:
        arr[x] = 1

print(sum(arr))