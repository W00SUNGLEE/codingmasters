import sys

n = int(sys.stdin.readline())

tmp = n

arr = [3, 5, 17, 257, 65537]

for i in range(len(arr)):

    if n % arr[i] == 0:
        n //= arr[i]

if n == 1:
    print("YES")
else:

    while n % 2 == 0:
        n //= 2

    if n == 1:
        print("YES")
    else:
        print("NO")