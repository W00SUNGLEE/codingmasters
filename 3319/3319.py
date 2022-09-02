import sys

p, q = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())

arr = list()

for i in range(n+1):
    p *= 10
    tmp = p // q
    arr.append(tmp)
    p -= tmp * q

if arr[n] > 4:
    arr[n-1] += 1

for i in range(n-1, -1, -1):
    if arr[i] == 10:
        arr[i] = 0
        arr[i-1] += 1
        continue

    else:
        break

print("0.", end="")

for i in range(n):
    print(arr[i], end="")

print()