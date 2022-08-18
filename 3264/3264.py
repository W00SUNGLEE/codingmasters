import sys

a, b, c = map(int, sys.stdin.readline().split())

if a**2 > (b**2) * c:
    print("NO")

else:
    print("YES")