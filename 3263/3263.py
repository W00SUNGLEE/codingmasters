import sys

n, m = map(int, sys.stdin.readline().split())

if m <= n/25:
    print("YES")

else:
    print("NO")