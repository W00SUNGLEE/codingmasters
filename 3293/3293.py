import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sort_arr = arr.copy()

sort_arr.sort()

index = [0, 0]

for i in range(n):
    if arr[i] != sort_arr[i]:
        index[0] = i
        break

for i in range(n-1, -1, -1):
    if arr[i] != sort_arr[i]:
        index[1] = i
        break

print(index[1]-index[0]+1)